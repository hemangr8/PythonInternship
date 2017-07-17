import requests
import re

from bs4 import BeautifulSoup


def spider(url):
    try:
        source_code = requests.get(url)
    except:
        return "Did not visit url :" + url
    text = source_code.text
    soup = BeautifulSoup(text, "lxml")
    return soup


def results(relevant_links, keyword):
    result_links = {}
    for relevant_link in relevant_links:
        soup = spider(relevant_link)
        if type(soup) is not str:
            for link in soup.findAll('a'):
                condition1 = re.search(keyword, link.text)
                # condition2 = re.search("http://", link.text)
                if condition1 is not None:
                    href = link.get('href')
                    title = link.string
                    result_links[href] = title
                # elif condition1 is not None and condition2 is None:
                #     href = "http://timesofindia.indiatimes.com" + link.get('href')
                #     title = link.string
                #     result_links[href] = title
    return result_links


def search(keyword):
    url = "http://timesofindia.indiatimes.com"
    soup = spider(url)
    relevant_links = {}
    for link in soup.findAll('a', {'class': ' navquery lnavdata '}):
        if re.search(keyword, link.text):
            href = "http://timesofindia.indiatimes.com" + link.get('href')
            title = keyword + " Category"
            relevant_links[href] = title
            return relevant_links
        elif re.search(keyword, link.text) is None:
            href = "http://timesofindia.indiatimes.com" + link.get('href')
            title = None
            relevant_links[href] = title
    if len(relevant_links.keys()) > 1:
        return results(relevant_links, keyword)
    else:
        return relevant_links

result = search("Modi")
if result == {}:
    print("Not Found")
else:
    file_destination = r'Results.txt'
    fw = open(file_destination, 'w')
    for res in result:
        line1 = "Link:    " + str(res)
        line2 = "Title:   " + str(result[res])
        fw.write(line1 + "\n" + line2 + "\n\n\n")
    fw.close()
