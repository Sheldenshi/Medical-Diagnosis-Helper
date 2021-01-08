from serpapi import GoogleSearch
import requests
import re
from bs4 import BeautifulSoup

def trade_spider(diseaseList, symptom):
    global numArticles
    index = 0
    for disease in diseaseList:
        # print('\033[95m' + disease)
        params = {
            "engine": "google",
            "q": disease +  " " + symptom,
            "api_key": "76a69f550e73865d1b68c3fd384e14ac2fe7089ec1d2bd187668d3e08e59631f",
            "location": "United States"
        }
        search = GoogleSearch(params)
        results = search.get_dict()
        organic_results = results['organic_results']
        numArticles[index] = len(organic_results)
        for result in organic_results:
            link = result["link"]
            get_single_item_data(link, index, symptom)
        index += 1


def get_single_item_data(item_url, index, symptom):
    global count
    global numArticlesWithWord
    searched_word = symptom
    source_code = requests.get(item_url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text,"html.parser")
    if soup is None or soup.body is None:
        return
    results = soup.body.find_all(string=re.compile('.*{0}.*'.format(searched_word)), recursive=True)
    if len(results) == 0:
        return
    numArticlesWithWord[index] += 1
    # print(item_url)
    # print('\033[92m' + 'Found the word "{0}" {1} times\n'.format(searched_word, len(results)))
    for content in results:
        for sentence in content.split("."):
            if sentence.__contains__(searched_word):
                count[index] += 1
                print("\n" + sentence.strip())
symptoms = ["burning"]
diseases = ["vitamin d deficiency", "multiple sclerosis"]

for symptom in symptoms:
    count = [0] * len(diseases)
    numArticles = [0] * len(diseases)
    numArticlesWithWord = [0] * len(diseases)
    trade_spider(diseases, symptom)
    # for ind in range(len(diseases)):
    #     print('\033[95m' + diseases[ind] + ": " + str(numArticlesWithWord[ind]) + " of " + str(
    #         numArticles[ind]) + " links mentions word")

suspectedDisease = diseases[count.index(max(count))]
print('\033[95m' + 'The suspected disease is ' + suspectedDisease)