from bs4 import BeautifulSoup

def scraper(html, query, start, is_next_null):
  soup = BeautifulSoup(html, 'lxml')

  organic_results = []
  index = 0
  for site in soup.find('div', id='links').findChildren('article'):
    index += 1

    if start and index < start: continue

    position = index
    title = site.select_one('a[data-testid="result-title-a"] > span').get_text()
    link = site.select_one('a[data-testid="result-extras-url-link"] > span').get_text()
    snippet = site.select_one('.OgdwYG6KE2qthn9XQWFC > span').get_text()
    favicon = site.select_one('a[data-testid="result-extras-site-search-link"] > img')['src'].replace('//', 'https://')

    site_links = site.select('.b269SZlC2oyR13Fcc4Iy > li')
    site_links_list = []

    for site_link in site_links:
      stitle = site_link.a.h3.get_text()
      slink  = site_link.a['href']
      site_links_list.append({
        'title': stitle,
        'link': slink
      })

    result = {
      'position': position,
      'title': title,
      'link': link,
      'snippet': snippet,
      'favicon': favicon,
    }
    if(len(site_links_list)):
      result['sitelinks'] = site_links_list

    organic_results.append(result)
  

  info = {
    'status': 'success',
    'q': query,
    'organic_results': organic_results,
  }

  if is_next_null:
    info['next'] = None
  else:
    info['next'] = index + 1


  if(start):
    return info

  inline_videos = []

  inline_videos_divs = soup.find_all('div', class_='module--carousel__item has-image has-extra-row')
  index = 0
  for video in inline_videos_divs:
    index += 1
    position = index
    title = video.select_one('.js-carousel-item-title').get_text()
    link = video.select_one('.js-carousel-item-title')['href']
    duration = video.find_all('div', class_='image-labels__label')[-1].get_text()
    platform = video.select_one('.module--carousel__gray-text').get_text()
    views = video.select_one('.module--carousel__extra-row').get_text()
    thumbnail = video.select_one('.js-carousel-item-image')['src'].replace('//', 'https://')

    inline_videos.append({
      'position': position,
      'title': title,
      'link': link,
      'duration': duration,
      'platform': platform,
      'views': views,
      'thumbnail': thumbnail
    })

  related_searches = []
  related_searches_divs = soup.select('.related-searches__item')
  for search in related_searches_divs:
    search_query = search.a.span.span.get_text().replace('\u200b', '')
    search_link = 'https://duckduckgo.com/' + search.a['href']
    search_link = search_link[0 : search_link.find('&')]

    related_searches.append({
      'query': search_query,
      'link': search_link
    })


  info['related_searches'] = related_searches

  if(len(inline_videos)):
    info['inline_videos'] = inline_videos

  return info
