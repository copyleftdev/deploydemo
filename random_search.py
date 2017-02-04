import requests
from faker import Factory
fake = Factory.create()



fnames = []
lnames = []

for x in range(1, 1000000):
    fnames.append(fake.first_name())
    lnames.append(fake.last_name())

def search_name(fname,lname):
    url = 'https://www.spokeo.com/{}-{}'.format(fname, lname)
    r = requests.get(url)
    r.close()

for fn,ln in zip(fnames, lnames):
    search_name(fn,ln)
