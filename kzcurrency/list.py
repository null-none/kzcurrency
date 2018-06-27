import urllib
from xml.dom import minidom

class KZCurrency(object):

    def __init__(self):
        self.url = 'http://www.nationalbank.kz/rss/rates_all.xml'

    def parse(self):
        usock = urllib.urlopen(self.url) 
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