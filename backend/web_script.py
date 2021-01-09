from serpapi import GoogleSearch
import requests
import re
import numpy
from bs4 import BeautifulSoup

def trade_spider(diseaseList, symptom):
    global numArticles
    global links
    global linkIndex
    global linkCount
    for disease in diseaseList:
        params = {
            "engine": "google",
            "q": disease +  " " + symptom,
            "api_key": "76a69f550e73865d1b68c3fd384e14ac2fe7089ec1d2bd187668d3e08e59631f",
            "location": "United States"
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results = results['organic_results']
        linkCount += ([0] * len(organic_results))
        for result in organic_results:
            link = result["link"]
            if link.__contains__("wikipedia"):
                linkCount.pop()
                continue
            if links.__contains__(link):
                linkCount.pop()
                get_single_item_data(link, symptom, links.index(link))
            else:
                links.append(link)
                get_single_item_data(link, symptom, linkIndex)
                linkIndex += 1


def get_single_item_data(item_url, symptom, index):
    global linkCount
    searched_word = symptom
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    if soup is None or soup.body is None:
        return
    results = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)
    if len(results) == 0:
        return
    for content in results:
        for sentence in content.split("."):
            if sentence.__contains__(searched_word):
                linkCount[index] = len(results)

links = []
linkCount = []
linkIndex = 0

for symptom in symptoms:
    count = [0] * len(diagnoses)
    numArticles = [0] * len(diagnoses)
    numArticlesWithWord = [0] * len(diagnoses)
    trade_spider(diagnoses, symptom)

bestLink = links[linkCount.index(max(linkCount))]
rankNum = 1
ranked = numpy.argsort(linkCount)
largest = ranked[::-1][:10]
print('The following are the best 10 articles to check out based on your suspected diagnoses and related symptoms.')
for i in largest:
    print(str(rankNum) + ". " + links[i])
    rankNum += 1

def searcher(symptoms, diagnoses):
    return
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Search articles.")
    parser.add_argument("symptoms", help="Patient's symptoms.")
    parser.add_argument("diagnoses", help="Diagnosis guesses.")
    args = parser.parse_args()
    searcher(args.symptoms, args.diagnoses)

