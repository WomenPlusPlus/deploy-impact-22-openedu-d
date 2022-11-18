# -*- coding: utf-8 -*-
"""
Created on Fri Nov  4 09:18:48 2022

@author: MBhargava
"""
import requests
from bs4 import BeautifulSoup
import pandas as pd

pages = range(1, 30)

keywords = ["Information Technology",
            "Sciences",
            "Humanities",
            "Mathematics",
            "Social Sciences",
            "Robotics",
            "Geography and History",
            "Sustainability",
            "Biography",
    ]


#Retrieve all the links that we will then use as base_url to get the short description
dflist  = []
for k in keywords:
    #loop thrugh the keywords
    keyword_urls = []
    #loop through the pages since we want a lot of data for each keyword
    for p in pages:
        suffixes= []
        links = []
        base_url = "https://merlot.org/merlot/materials.htm?keywords=" + k + "?=" + str(p)
        print(base_url)
        res = requests.get(base_url)
        soup = BeautifulSoup(res.text, "html.parser")
        data = soup.find_all('div', class_ = 'view grid-view')
        for div in data:
            arefs = div.findAll("a")
            for a in arefs:
                suffixes.append(a["href"])
        links += list(set(suffixes))
        for a in links:
            if a.startswith("#") or a =="/merlot/login.htm":
                links.remove(a)
        keyword_urls += ["https://merlot.org" + a for a in links]

    #create a dataframe with keywords, and urls
    topic = [k] * len(keyword_urls)
    df = pd.DataFrame()
    df["topic"] = topic
    df["url"] = keyword_urls
    dflist.append(df)

maindf = pd.concat(dflist)
df = maindf.drop_duplicates(subset=["url"])
df["short_text"] = ""

#loop through url list and get the short text for each url
for url in df["url"]:
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")
    data = soup.find("div", id="material_description").text
    df.loc[df["url"] == url, "short_text"] = data


        
        
        