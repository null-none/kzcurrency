import sys

if sys.version_info[0] == 3:
    from urllib.request import urlopen
else:
    # Not Python 3 - today, it is most likely to be Python 2
    # But note that this might need an update when Python 4
    # might be around one day
    from urllib import urlopen
from xml.dom import minidom

class KZCurrency(object):

    def __init__(self):
        self.url = 'http://www.nationalbank.kz/rss/rates_all.xml'

    def parse(self):
        usock = urlopen(self.url) 
        xmldoc = minidom.parse(usock)                              
        usock.close()                                              
        return xmldoc.toxml()

    def list(self):
        result = []
        xml = minidom.parseString(self.parse())
        for item in xml.getElementsByTagName("item"):
            result.append(item.getElementsByTagName("title")[0].firstChild.data)
        return result

    def get(self, title):
        result = {}
        xml = minidom.parseString(self.parse())
        for item in xml.getElementsByTagName("item"):
            if title == item.getElementsByTagName("title")[0].firstChild.data:
                result = {
                    'title': item.getElementsByTagName("title")[0].firstChild.data,
                    'pubDate': item.getElementsByTagName("pubDate")[0].firstChild.data, 
                    'description': item.getElementsByTagName("description")[0].firstChild.data,
                    'quant': item.getElementsByTagName("quant")[0].firstChild.data,              
                }
        return result

    def rates(self):
        result = []
        xml = minidom.parseString(self.parse())
        for item in xml.getElementsByTagName("item"):
            result.append({
                'title': item.getElementsByTagName("title")[0].firstChild.data,
                'pubDate': item.getElementsByTagName("pubDate")[0].firstChild.data, 
                'description': item.getElementsByTagName("description")[0].firstChild.data,
                'quant': item.getElementsByTagName("quant")[0].firstChild.data,              
            })
        return result
