import requests
import pandas as pd
import json

SEARCH_ENDPOINT = "https://api.wikimedia.org/core/v1/wikipedia/en/search/page?q="

PAGE_DETAIL_ENDPOINT = "https://api.wikimedia.org/core/v1/wikipedia/en/page/"

QUERY_WORDS = [
    "Ontology",
    "Data Science",
    "Astrophysics",
    "Marine Biology",
    "Climate Change",
    "Psychology",
    "War",
    "Artificial Intelligence",
    "Machine Learning",
    "Scrum Master",
    "Contemporary Art",
    "Vegan Cooking",
    "Landscape Photography",
    "Switzerland",
    "European Union",
    "NATO",
    "Family Constellations",
    "Bioengineering",
    "Medicine",
    "Physics",
    "Mathematics",
    "Data Visualization",
    "Topic Modeling",
    "Antarctica",
    "Sequoia",
    "Blue Whale",
    "Matcha",
    "Solar Panels",
    "Thyroid",
    "Gender equality",
    "Education",
    "Developing country",
    "Spanish History",
    "Dog training",
    "Solar System",
    "Autoimmune disease",
]

def search_query_in_pages(search_query):
    ep = SEARCH_ENDPOINT + search_query
    res = requests.get(ep)
    return res.json()


def is_cc_sa(content_key):
    ep = PAGE_DETAIL_ENDPOINT + content_key
    res = requests.get(ep)
    record = res.json()
    cc_sa_text = record["license"]["url"]
    return "/by-sa/" in cc_sa_text


QUERIED_DATASETS = []

for query in QUERY_WORDS:
    searched_data = search_query_in_pages(query)
    jsoned_data_df = pd.read_json(json.dumps(searched_data["pages"]), orient="records")
    QUERIED_DATASETS.append(jsoned_data_df)

queried_words_datasets = pd.concat(QUERIED_DATASETS)

queried_words_datasets.to_csv('queried_datasets.csv')

# print(is_cc_sa("Open_education"))

