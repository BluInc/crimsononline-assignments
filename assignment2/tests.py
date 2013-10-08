from question1 import *

content_list = []

# Test for from_url:
# print 'TESTING from_url'
# url1 = http://www.thecrimson.com/article/2013/10/3/bonfire-of-the-vanitas/
# url2 = http://www.thecrimson.com/article/2013/10/5/harvard-football-holy-cross/
# url3 = http://www.thecrimson.com/article/2013/10/3/faust-divestment-letter-reaffirms/
# c1 = from_url(content_list, url1)
# c2 = from_url(content_list, url2)
# c3 = from_url(content_list, url3)
# 
# print 'CONTENT MATCHING {0}:'.format(url1)
# if c1:
#     c1.show()
# print '\nCONTENT MATCHING {0}:'.format(url2)
# if c2:
#     c2.show()
# print '\nCONTENT MATCHING {0}:'.format(url3)
# if c3:
#     c3.show()
#
# print '\n'
#
# Test for posted_after:
# print 'TESTING posted_after'
# time1 = datetime.datetime.strptime('05102013').date()
# time2 = datetime.datetime.strptime('05102012').date()
# time3 = datetime.datetime.strptime('11112011').date()
# 
# print 'CONTENT POSTED AFTER {0]'.format(time1)
# for c in posted_after(content_list, time1):
#     c.show()
# print '\nCONTENT POSTED AFTER {0]'.format(time2)
# for c in posted_after(content_list, time2):
#     c.show()
# print '\nCONTENT POSTED AFTER {0]'.format(time3)
# for c in posted_after(content_list, time3):
#     c.show()
