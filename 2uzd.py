"""
Iegūt ziņas, izmantojot rss no google.lv.

"""

import feedparser
rss_url = 'https://news.google.com/rss?hl=en-LV&gl=LV&ceid=LV:en'
feed=feedparser.parse(rss_url)
for entry in feed.entries:
    print("Virsraksts:", entry.title)
    print("Saite:", entry.link)
    print("\n")