
import requests
from bs4 import BeautifulSoup as bs
import re
from multiprocessing import Process, Pool


masterloclst = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE",
                "DC", "FL", "GA", "HI", "ID", "IL", "IN", "IA",
                "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN",
                "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM",
                "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI",
                "SC", "SD", "TN", "TX", "UT", "VT", "VA", "WA",
                "WV", "WI", "WY"]

pages = set()



def getlinks(pageUrl):
    user_agent = {'User-agent': 'Mozilla/5.0'}
    global pages
    html = requests.get(target_url + pageUrl, headers=user_agent)
    soup = bs(html.content, "html.parser")

    for link in soup.findAll("a"):
        if 'href' in link.attrs:
            if link.attrs['href'] not in pages:

                newPage = link.attrs['href']
                print(newPage)
                pages.add(newPage)
                getlinks(newPage)
                if 'http://' in newPage:
                    pass
                elif 'https://' in newPage:
                    pass
                else:

                    with open('spokeo.txt', 'a+') as spokeout:
                        spokeout.write(newPage + "\n")

for eachl in masterloclst:
    target_url = "http://www.spokeo.com/{}".format(eachl)
    getlinks("")
