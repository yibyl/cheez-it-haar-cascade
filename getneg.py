# Gets the negative images

import requests
from bs4 import BeautifulSoup
from selenium import webdriver

links = []
ids = []

driver = webdriver.Chrome()
for x in range(11):
    url = "https://picsum.photos/v2/list?page=" + str(x) +"&limit=1000"
    driver.get(url)
    content = driver.page_source
    soup = BeautifulSoup(content)
    l = []
    for i in str(soup)[1:-1].split("{"):
        l.append(i)

    for i in l[1:]:
        for j in i.split(","):
            if "\"id\"" in j:
                ids.append(j[6:-1])
            if "download_url" in j:
                links.append(j[16:-2])


def saveimg(imgurl, num):
    img_data = requests.get(imgurl).content
    with open('negative/' + str(num) + '.jpg', 'wb') as handler:
        handler.write(img_data)



for i in range(len(links)):
    saveimg(links[i], ids[i])

