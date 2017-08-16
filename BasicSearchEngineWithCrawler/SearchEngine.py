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
    def get_all_links(url):
        soup = SearchEngine.spider(url)
        expression = re.compile(r'http[s]?://')
        links_list = []
        links_dict = {}
        if type(soup) is str:
            return links_list , links_dict
        else:
            elements = soup.findAll('a')
            for element in elements:
                if re.search(expression, str(element.get('href'))):
                    href = element.get('href')
                    title = str(element.string)
                    links_dict[href] = title
                    links_list.append(href)
                else:
                    href = base_url + str(element.get('href'))
                    title = str(element.string)
                    links_dict[href] = title
                    links_list.append(href)
                    
            return links_list , links_dict

    @staticmethod
    def results(relevant_links, keyword):
        result_links = {}
        for link in list(relevant_links.keys()):
            condition = re.search(keyword, relevant_links[link])
            if condition and re.search(r"java", str(link)) is None:
                href = link
                title = relevant_links[link]
                result_links[href] = title
                
        return result_links

    @staticmethod
    def union(list1, list2, dict1, dict2):
        for link in list2:
            if link not in list1:
                list1.append(link)
        for key in list(dict2.keys()):
            if key not in list(dict1.keys()):
                dict1[key] = dict2[key]

    @staticmethod
    def search(keyword):
        to_crawl_links = [base_url]
        crawled_links = []
        crawled_links_with_titles = {}
        while to_crawl_links and len(crawled_links_with_titles)<1000:
            url = to_crawl_links.pop()
            condition1 = re.search(r"http://ad.doubleclick.net/", str(url))
            condition2 = re.search(r".cms", str(url))
            condition3 = re.search(r"http://advertise.indiatimes.com/", str(url))
            condition4 = re.search(r"http://timesofindia.indiatimes.commailto:TIFM.Leads@timesinternet.in", str(url))
            condition5 = re.search(r"http://timesofindia.indiatimes.com/policy", str(url))
            condition6 = re.search(r"http://www.indiatimes.com", str(url))
            if url not in crawled_links and condition1 is None and condition2 is None and condition3 is None and condition4 is None and condition5 is None and condition6 is None:
                links , links_with_titles = SearchEngine.get_all_links(url)
                SearchEngine.union(to_crawl_links, links, crawled_links_with_titles, links_with_titles)
                crawled_links.append(url)

        result_links = SearchEngine.results(crawled_links_with_titles, keyword)
        return result_links
    
