from bs4 import BeautifulSoup as soup
from urllib.request import urlopen


class Scraper:
    @staticmethod
    def scrapwiki(s):
        # searchtext = input("Enter Search Text : ")
        searchtext = s
        try:
            my_url = 'https://en.wikipedia.org/wiki/' + searchtext
            uClient = urlopen(my_url)
            page_html = uClient.read()
            uClient.close()
            page_soup = soup(page_html, "html.parser")

            container = page_soup.findAll("div", {"class": "toc"})

            contents = container[0].findAll("li", {"class": "toclevel-1"})
            final_content = []
            for cont in contents:
                content = cont.find("span", {"class": "toctext"}).text
                print(content)
                final_content = final_content + [content]

            return final_content
        except Exception as e:
            final_content = ['Search Criteria invalid', e]
            return final_content
