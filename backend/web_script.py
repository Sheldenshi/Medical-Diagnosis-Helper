from serpapi import GoogleSearch
import requests
import re
import numpy
from bs4 import BeautifulSoup
import argparse

def trade_spider(symptoms, diseaseList, symptom, links, linkCount, linkIndex):
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
        for result in organic_results:
            link = result["link"]
            if link.__contains__("wikipedia"):
                continue
            if links.__contains__(link):
                get_single_item_data(symptoms, link, symptom, linkCount, links.index(link))
            else:
                linkCount.append([0] * len(symptoms))
                links.append(link)
                get_single_item_data(symptoms, link, symptom, linkCount, linkIndex)
                linkIndex += 1

def get_single_item_data(symptoms, item_url, symptom, linkCount, index):
    searched_word = symptom
    try:
        source_code = requests.get(item_url)
    except requests.exceptions.RequestException:
        return
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
                linkCount[index][symptoms.index(symptom)] = len(results)

def search(symptoms, diagnoses):
    symptoms = symptoms.replace('\n', '')
    diagnoses = diagnoses.replace('\n', '')
    symptoms = symptoms.split(',')
    diagnoses = diagnoses.split(',')
    links = []
    linkCount = []
    linkIndex = 0
    result = []
    expectedSeconds = len(symptoms) * len(diagnoses) * 12

    for symptom in symptoms:
        trade_spider(symptoms, diagnoses, symptom, links, linkCount, linkIndex)

    sumLinkCount = []
    for array in linkCount:
        sumLinkCount.append(sum(array))

    rankNum = 1
    ranked = numpy.argsort(sumLinkCount)
    largest = ranked[::-1][:10]
    for i in largest:
        relevantString = "Contains "
        for symptom in symptoms:
            relevantString += symptom + " " + str(linkCount[i][symptoms.index(symptom)]) + " times"
            if symptoms.index(symptom) == (len(symptoms) -1):
                relevantString += "."
            else:
                relevantString += ", "
        result.append([str(rankNum), links[i], relevantString])
        rankNum += 1
    return result


