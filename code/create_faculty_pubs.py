#Use faculty dataset to find their publications

#Publications up to 2002, number of citations

import pandas as pd
from scholarly import scholarly
from tqdm import tqdm
import time
import random 

data = []

faculty_df = pd.read_csv('../data/Surnames_faculty_data.csv')

names = faculty_df['fname'] + " " + faculty_df['lname']

#for i in tqdm(range(len(names))):
#for j in tqdm(range(611)):
for i in tqdm(range(10)):
    search_results = scholarly.search_author(names[i])
    author = scholarly.fill(next(search_results))

    publications = author['publications']

    for pub in publications:
        bib = pub['bib']
        title = bib['title']
        journal = bib['citation']
        year = journal[-4:]
        citations = pub['num_citations']
        data.append([names[i],title,journal,year,citations])

    time.sleep(random.randint(1,10))


faculty_pubs = pd.DataFrame(data)

print(faculty_pubs)
