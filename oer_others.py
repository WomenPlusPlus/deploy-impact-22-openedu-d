# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 16:50:10 2022

@author: MBhargava
"""

import requests
from bs4 import BeautifulSoup
import pandas as pd

keywords = ["Railways",
            "Bananas",
            "Deceit",
            "Furniture",
            "Sailor",
            "Dreams",
            "Haunted",
            "corruption",
            "kings",
            "Hamlin",
            "golden",
            "vertigo",
            "Mirage",
            "crash",
            "Skiing",
            "Chritmas",
            "Example",
            "Outrage",
            "Paddle",
            "Popular",
            "Random",
            "Games",
            "exercise",
            "flame",
            "symptoms"
            "Myths",
            "Bucket",
            "oven",
            "tricks",
            "wealth",
            "Labels",
            "factory",
            "Melody",
            "dysfunction",
            "systems",
            "Fantasy",
            "suspension",
            "Economy",
            "Determination",
            "Passages",
            "Constellations",
            "particles",
            "Belief",
            "Expansion",
            "Confession",
            "Aviation",
            "Breath"
            ]


#Retrieve all the links that we will then use as base_url to get the short description
dflist  = []

for k in keywords:
    base_url = "https://www.oercommons.org/search?f.search=" + k
    print(base_url)
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, "html.parser")
    data = soup.find_all("div", class_="abstract-full")
    short_text =[d.get_text(strip=True) for d in data]
    topic = len(short_text) * [k]
    df = pd.DataFrame()
    df["topic"] = topic
    df["short_text"] = short_text
    print(len(df), k)
    dflist.append(df)
    
maindf = pd.concat(dflist)

    