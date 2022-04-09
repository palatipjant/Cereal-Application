from gnews import GNews
import webbrowser

google_news = GNews()
google_news = GNews(language='th', country='thai', period='1d', max_results=10, exclude_websites=['google.com', 'bbc.com'])
news = google_news.get_news('covid')


for i in range (3) :

    print(news[i]['title'])
    print(news[i]['published date'])
    print(news[i]['url']+"\n")



url = news[2]['url']

webbrowser.open(url,new=1)