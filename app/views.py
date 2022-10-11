from django.http import JsonResponse, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from pyppeteer import launch
from requests.models import PreparedRequest
from .scraper import scraper
from .chromium_downloader import chromium_exe

duck_url = 'https://duckduckgo.com/'
is_next_null = False

async def search_query(query, start):
  browser = await launch(
    headless=False,
    handleSIGINT=False,
    handleSIGTERM=False,
    handleSIGHUP=False,
    executablePath=chromium_exe,
    defaultViewport=None,
    args=[
      '--start-maximized',
      # '--start-fullscreen'
    ]
  )
  page = await browser.newPage()
  
  await page.goto(duck_url, {'waitUntil': 'networkidle0'})
  await page.waitForSelector('form')

  # the site opens into two versions and the search form selectors are different
  if await page.querySelector('#searchbox_input'):
    # whitish site version
    # await page.waitForSelector('#searchbox_input')
    await page.type('#searchbox_input', query) # type the query into the input field
    await page.click('#searchbox_homepage button[type="submit"]') # click on the search button

  else:
    # pinkish site version
    # await page.waitForSelector('#search_form_input_homepage')
    await page.type('#search_form_input_homepage', query)
    await page.click('#search_button_homepage')
    
  await page.waitForNavigation() # wait for results to load
  await page.waitForSelector('#links')

  # the while loop login deals with paginations
  while True:
    # get the current number of results and if the results are less than starting news, then click on more results
    current_num_results = await page.evaluate(f'''() => document.querySelectorAll('a[data-testid="result-extras-site-search-link"] > img').length''')
    

    if(current_num_results < start):
      try: 
        await page.click('.result--more__btn')
        await page.waitForSelector('.result--more__btn', {'timeout': 5000})
      except:
        # exception will occur when there are no more result because more results button will not be present in the DOM
        break
    
    else: break

  # extract the page source
  html = await page.content()

  global is_next_null
  # check if there are more results
  if not (await page.querySelector('.result--more__btn')):
    is_next_null = True

  await browser.close()
  return html



async def api_search(req, format=None):
  # extract the query string from the url

  query = req.GET.get('q')
  start = req.GET.get('start')
  if not start: start = 0
  else: start = int(start)

  if not query:
    return JsonResponse({'error': 'Search query not provided'})

  # search the query using pyppeteer
  html = await search_query(query, start)

  # extract the information from html by scraping using beautiful soup
  info = scraper(html, query, start, is_next_null)

  # handle there are no more results
  if info['next']:
    url = req.build_absolute_uri().split('?')[0]
    pr = PreparedRequest()
    pr.prepare_url(url, {'q': query, 'start': str(info['next'])})
    info['next'] = pr.url


  return JsonResponse(info)
  # return JsonResponse(serializer.data, safe=False)
  # return Response('data', status=status.HTTP_200_OK)


