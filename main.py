import newspaper
import pymongo

from Article import Article
import db_helpers

news_papers = ['https://www.theguardian.com/uk', 'https://www.bbc.com/', 'https://www.independent.co.uk/', 'https://www.ft.com/', 'https://www.foxnews.com/', 'https://www.infowars.com/', 'https://www.newswars.com/']
for url in news_papers:
    print('scraping: ', url)
    paper = newspaper.build(url=url, language="en", memoize_articles=False)

    print(len(paper.articles))

    i = 0
    for article in paper.articles:
        try:
            article.download()
            article.parse()
            article.nlp()

        except:
            print('EXCEPTION!')
        
        finally:
            text = article.text.split()
            meta_keywords = article.meta_keywords
            keywords = article.keywords
            summary = article.summary
            authors = article.authors
            title = article.title
            html = article.html
            published_dt = article.publish_date
            url = article.url
            
            #self, title_, text_, authors_, url_, summary_, meta_keywords_, nlp_keywords_, published_datetime_
            art = Article(title, text, authors, url, summary, meta_keywords, keywords, published_dt, html)
            db_helpers.saveObjToDB('test_articles', art)
            """
            print('text: ', article.text.split())
            print('keywords: ', article.keywords)
            print('summary: ', article.summary)
            print('html: ', article.html.encode())
            i = i + 1
            """
            


