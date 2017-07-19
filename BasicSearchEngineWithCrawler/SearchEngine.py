import requests
import re
from bs4 import BeautifulSoup

base_url = "http://timesofindia.indiatimes.com"


class SearchEngine:

    @staticmethod
    def spider(url):
        try:
            source_code = requests.get(url)
        except:
            return "Did not visit url :" + url
        text = source_code.text
        soup = BeautifulSoup(text, "lxml")
        return soup

    @staticmethod
    def results(relevant_links, keyword):
        result_links = {}
        expression = re.compile(r'http[s]?://')
        for relevant_link in relevant_links:
            soup = SearchEngine.spider(relevant_link)
            if type(soup) is not str:
                for link in soup.findAll('a'):
                    condition1 = re.search(keyword, link.text)
                    condition2 = re.search(expression, str(link.get('href')))
                    if condition1 and condition2 and re.search(r"java", str(link.get("href"))) is None:
                        href = link.get('href')
                        title = link.string
                        result_links[href] = title
                    elif condition1 and condition2 is None and re.search(r"java", str(link.get("href"))) is None:
                        href = base_url + str(link.get('href'))
                        title = link.string
                        result_links[href] = title
        return result_links

    @staticmethod
    def search(keyword):
        soup = SearchEngine.spider(base_url)
        relevant_links = {}
        for link in soup.findAll('a', {'class': ' navquery lnavdata '}):
            if re.search(keyword, link.get('href')) and re.search(r"java", str(link.get("href"))) is None:
                href = base_url + link.get('href')
                title = keyword + "Category"
                relevant_links[href] = title
                return relevant_links
            elif re.search(keyword, link.text) is None and re.search(r"java", str(link.get("href"))) is None:
                href = base_url + link.get('href')
                title = None
                relevant_links[href] = title
        if len(relevant_links.keys()) > 1:
            return SearchEngine.results(relevant_links, keyword)
        else:
            return relevant_links

# result = Crawler.search("City")
# if result == {}:
#     print("Not Found")
# else:
#     file_destination = r'Results.txt'
#     fw = open(file_destination, 'w')
#     for res in result:
#         line1 = "Link:    " + str(res)
#         line2 = "Title:   " + str(result[res])
#         fw.write(line1 + "\n" + line2 + "\n\n\n")
#     fw.close()
