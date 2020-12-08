import datetime

class Article:
    def __init__(self, title_, text_, authors_, url_, summary_, meta_keywords_, nlp_keywords_, published_datetime_, html_):
        self.title = title_
        self.text = text_
        self.authors = authors_,
        self.url = url_
        self.summary = summary_,
        #keywords from html <meta> tag
        self.meta_keywords = meta_keywords_
        #keywords generated by perfroming nlp on article
        self.nlp_keywords = nlp_keywords_
        self.published_datetime = published_datetime_
        self.html = html_.encode()
        
    

"""
   "title": "Headline...   BREAKING NEWS!",
    "text": "In this edition of BREAKING NEWS! We have yet more BREAKIKNG NEWS! All the BREAKING NEWS! We have it. BREAKING NEWS! (NOW Featuring HEADLINES)",
    "authors": ["Sam Smith", "George Henry"],
    "url": "https://www.bbc.com",
    "summary": "summary of article",
    "keywords": ["headline", "BREAKING", "NEWS"],
    "published_datetime": datetime.datetime.now()
""" 
