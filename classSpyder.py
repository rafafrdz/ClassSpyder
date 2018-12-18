import urllib.request as url
class Spyder(object):
    def __init__(self,url):
        self.url = str(url)
    def __getHtml(self):
        dir = url.urlopen(self.url)
        html = str(dir.read())
        return html
    def __getUrls(self):
        urls = []
        html = self.__getHtml()
        while True:
            pos = html.find('href="')
            if pos == -1:
                break
            html = html[(pos + 6):]
            urls.append(html[:html.find('"')])
        return urls
    def __busca(self,cosa):
        return [x for x in self.__getUrls() if str(cosa) in x]
    def getLink(self):
        return self.__busca("http")
    def getPdf(self):
        return self.__busca(".pdf")
    def getLinktoTxt(self):
        fich = open("links.txt",'w')
        link = self.getLink()
        for i in link:
            fich.write(str(i)+"\n")
        fich.close()
        return fich
    def getPdftoTxt(self):
        fich = open("pdfs.txt",'w')
        link = self.getPdf()
        for i in link:
            fich.write(str(i)+"\n")
        fich.close()
        return fich
#Ejemplo
sp1 = Spyder("https://es.wikipedia.org/wiki/Madrid")
sp1.getPdftoTxt()
sp1.getLinktoTxt()