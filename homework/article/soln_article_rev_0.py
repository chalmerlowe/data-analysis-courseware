# NOTE: this does not cover all the functionality in the instructions.
# It DOES cover each type of functionality.


from datetime import datetime

class Article:
    
    def __init__(self):
        self.author = ''
        self.title = ''
        self.content = ''
        self.datetime = str(datetime.now())
        self.tags = []
        self.status = 'Draft'
        
    def set_author(self, author):
        self.author = author

    def set_status(self, published=True):
        if published:
            self.status = 'Published'
            self.set_publish_date()
        else:
            self.status = 'Draft'

    def set_publish_date(self):
        self.datetime = str(datetime.now())
        
    def set_tags(self, tag):
        self.tags.append(tag)

articles = []

article1 = Article()
article1.set_author('William Shakespeare')
article1.set_tags('tragedy')
article1.set_status()

articles.append(article1)

article2 = Article()
article2.set_author('JRR Tolkien')
article2.set_tags('fantasy')
article2.set_status()

articles.append(article2)

for entry in articles:
    output = '''{}
    {}
    {}
    {}'''.format(entry.author, entry.tags, entry.status, entry.datetime)
    print(output)
    print()