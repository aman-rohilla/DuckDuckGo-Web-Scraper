## DuckDuckGo Web Scraper

#### Python, Django, Django REST Framework, pyppeteer, BeautifulSoup

Extract search results of a query on duckduckgo.com with pagination and send back as json<br/>
The results include websites, inline videos and related searches<br/>

<pre>
Listen for queries on django server
Serach the query on server side using chromium and pyppeteer
Extract the information using beautifulsoup
Send back the results as json
</pre>

##### Search API Endpoint : /api/search/?q=latest+news

#### Sample Output

<pre>
{
  "status": "success",
  "q": "latest news",
  "organic_results": [
    {
      "position": 1,
      "title": "CNN - Breaking News, Latest News and Videos",
      "link": "https://www.cnn.com",
      "snippet": "View the latest news and breaking news today for U.S., world, weather, entertainment, politics and health at CNN.com.",
      "favicon": "https://external-content.duckduckgo.com/ip3/www.cnn.com.ico"
    },
    {
      "position": 2,
      "title": "NBC News - Breaking News & Top Stories - Latest World, US & Local News ...",
      "link": "https://www.nbcnews.com",
      "snippet": "Go to NBCNews.com for breaking news, videos, and the latest top stories in world news, business, politics, health and pop culture.",
      "favicon": "https://external-content.duckduckgo.com/ip3/www.nbcnews.com.ico"
    },
    {
      "position": 3,
      "title": "Latest News: top news headlines, videos and updates | NBC News",
      "link": "https://www.nbcnews.com",
      "snippet": "View the latest news and top headlines from NBCNews.com. Find videos and news articles on the latest top stories in US and world news.",
      "favicon": "https://external-content.duckduckgo.com/ip3/www.nbcnews.com.ico"
    }
  ],
  "next": "http://localhost:8000/api/search/?q=latest+news&start=11",
  "related_searches": [
    {
      "query": "latest news in world today",
      "link": "https://duckduckgo.com/?q=latest%20news%20in%20world%20today"
    },
    {
      "query": "show me today's news",
      "link": "https://duckduckgo.com/?q=show%20me%20today%27s%20news"
    },
    {
      "query": "latest much news",
      "link": "https://duckduckgo.com/?q=latest%20much%20news"
    },
    {
      "query": "breaking news around me",
      "link": "https://duckduckgo.com/?q=breaking%20news%20around%20me"
    }
  ],
  "inline_videos": [
    {
      "position": 1,
      "title": "Queen Elizabeth News Live | Kate Middleton & Prince William News Updates | Queen Funer\u2026",
      "link": "https://www.youtube.com/watch?v=ZBHldkOEZj8",
      "duration": "11:54:56",
      "platform": "YouTube",
      "views": "284K views",
      "thumbnail": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOVF.D1eJ5qyDbgY9MqnSOfGoLw%26pid%3DApi%26h%3D120&f=1"
    },
    {
      "position": 2,
      "title": "Latest news ABout Gajuwaka Conductor Jhansi|Gajuwaka Conductor Jhansi Dan\u2026",
      "link": "https://www.youtube.com/watch?v=MfcL5_sTp2g",
      "duration": "2:30",
      "platform": "YouTube",
      "views": "2.3K views",
      "thumbnail": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse4.mm.bing.net%2Fth%3Fid%3DOVF.7OyB5vp9GUOthVRNOeH5SQ%26pid%3DApi%26h%3D120&f=1"
    },
    {
      "position": 3,
      "title": "Latest News Updates | Latest Telugu News | @SumanTV Entertainment",
      "link": "https://www.youtube.com/watch?v=8htVuIqqWaA",
      "duration": "2:54",
      "platform": "YouTube",
      "views": "6.1K views",
      "thumbnail": "https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Ftse3.mm.bing.net%2Fth%3Fid%3DOVF.I9rJQoYnX8%252beBFTSUZJtGw%26pid%3DApi%26h%3D120&f=1"
    }
  ]
}
</pre>
