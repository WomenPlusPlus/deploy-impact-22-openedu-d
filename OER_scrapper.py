# -*- coding: utf-8 -*-
"""
Created on Sat Nov  5 13:00:39 2022

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
            "Biography"]

#Retrieve all the links that we will then use as base_url to get the short description
k = keywords[0]
p = 1
dflist  = []

for k in keywords:
    #base_url = "https://www.oercommons.org/search?batch_size=" + str(p) & "&sort_by=search&view_mode=summary&f.search=" + k + "&f.material_types=lecture"
    base_url= "https://www.oercommons.org/search?batch_size=140&sort_by=search&view_mode=summary&f.search=social+studies"
    print(base_url)
    res = requests.get(base_url)
    soup = BeautifulSoup(res.text, "html.parser")
    data = soup.find_all("div", class_="abstract-full")
    short_text =[d.get_text(strip=True) for d in data]
    topic = len(short_text) * [k]
    df = pd.DataFrame()
    df["topic"] = topic
    df["short_text"] = short_text
    dflist.append(df)
        
for i in range(len(dflist)):
    print(len(dflist[i]), keywords[i])    
    

maindf = pd.concat(dflist)
maindf.to_csv("c:/d/PM/WPP/oercommons.csv")

        
        