class Article:
    '''
    Question 2a
        Properties:
            - headline
            - content
            - creator (author)
        Methods:
            - show (print contents)
            - save (save to text file)

    Question 2b
        Methods:
            - Load article from text file

    Question 2d
        Properties:
            - related_image
        Methods:
            - modify save to save info about related picture (if it exists)
            - modify load to load info about related picture (if it exists)
            - modify show to also show the related picture (if it exist)
    '''
    import json

    headline = ''
    content = ''
    creator = ''
    related_image = None

    def __init__(self,head,cont,creat,img):
        self.headline = head
        self.content = cont
        self.creator = creat
        self.related_image = img

    def show(self):
        print 'headline: ' + self.headline
        print 'content: ' + self.content
        print 'creator: ' + self.creator
        self.related_image.show()


    def save(self):
        filename = self.creator + '-' + self.headline
        if not os.path.isfile(filename):
            with open(filename, 'w') as outfile:
                json.dumps({'headline':self.headline,'creator':self.creator,'content':self.content,
                    'related_image':self.related_image.to_json})
        else:
            print 'Please rename headline'

    def load(self,filename):
        try:
            with open(filename, 'r') as infile:
                data = json.loads(infile.read())
                return self.__init__(data['headline'],data['content'],data['creator'],
                    json.loads(data['related_image']))
        except IOError:
            print 'File does not exist'




class Picture:
    '''
    Question 2c
        Properties:
            - image_file (path to original image relative to this file)
            - creator (photographer)
         Methods
            - show (show image)
    '''
    from PIL import image
    import json

    image_file = ''
    title = ''
    creator = ''

    def __init__(self,img_f, t, c):
        self.image_file = img_f
        self.title = t
        self.creator = c

    def to_json(self):
        return {'image_file':self.image_file,'title':self.title,'creator':self.creator}

    def show(self):
        Image.open(self.image_file).show()
