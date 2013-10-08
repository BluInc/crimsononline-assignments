import datetime

class Content(object):
    '''
    Required properties:
        - title
        - subtitle
        - creator
        - publication date
    Required methods:
        - show
        - matches_url (question 1d)
    '''
    def __init__(self,title,subtitle,creator,date):
        self.title = title
        self.subtitle = subtitle
        self.creator = creator
        self.date = date

    @classmethod
    def from_url(cls,content_list,url):
        for content in content_list:
            if matches_url(content,url):
                return content
        return None

    @classmethod
    def posted_after(cls,content_list,date):
        return [x for x in content_list if x.date > date]


    def show(self):
        print 'title: '+self.title
        print 'subtitle: '+self.subtitle
        print 'creator: '+self.creator
        print 'date: '+self.date

    def matches_url(self,url):
        if re.match('http://thecrimson.com/.*/[0-9]{4}/[0-9]{2}/[0-9]{2}/.*/')
            prop = url.split('/')
            content_type = prop[3].lower()
            content_date = datetime.datetime.strptime(prop[6]+prop[5]+prop[4]).date()
            content_slug = prop[7].lower()
            if self.date == content_date and self.slug.lower() == content_slug:
                if content_type == 'article' and isinstance(self,Article) or 
                content_type == 'picture' and isinstance(self,Picture):
                    return True
        else:
            return False

class Article(Content):
    '''
    Required properties:
        - All properties of Content
        - related_image
    Required methods:
        - All methods of Content
    '''
    def __init__(self,title,subtitle,creator,date,related_image):
        super(Content, self).__init__(title,subtitle,creator,date)
        self.related_image = related_image

    def show(self):
        print 'headline: '+self.title
        print 'teaser: '+self.subtitle
        print 'creator: '+self.creator
        print 'date: '+self.date
        self.related_image.show()

class Picture(Content):
    '''
    Required properties:
        - All properties of Content
        - image_file
    Required methods:
        - All methods of Content
    '''
    def __init__(self,title,subtitle,creator,date,image_file):
        super(Content, self).__init__(title,subtitle,creator,date)
        self.image_file = image_file

    def show(self):
        print 'title: '+self.title
        print 'caption: '+self.subtitle
        print 'creator: '+self.creator
        print 'date: '+self.date
        Image.open(self.image_file).show()
'''
Question 1e
'''
def from_url(c_lst, url):
    pass

'''
Question 1e
'''
def posted_after(c_lst, dt):
    pass
