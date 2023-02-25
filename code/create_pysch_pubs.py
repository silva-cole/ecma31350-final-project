# Create pysch_pub_df which has all publications from top 5 psych journals between 1980 and 2002
# Journals:
    # Advances in Experimental Social Psychology
    # Annual Review of Psychology
    # Pyschological Science in the Public Interest
    # Pyschological Bulletin
    # Journal of Personality and Social Psychology
# source, https://www.scimagojr.com/journalrank.php?area=3200&year=2006
# columns: title, jcode, vol, no, pages, author1 through author5, authors(no), citations_2006, citations_all

from scholarly import scholarly
import pandas as pd

query = "Advances in Experimental Social Psychology"

# Search for the journal and retrieve its page
search_results = scholarly.search_pubs(query)
####PROBLEM WITH .fill()
journal_page = next(search_results).fill()

# Retrieve the publications from the journal page
publications = journal_page.citedby

# Create a list to store the scraped data
data = []

# Loop through each publication and extract its information
for pub in publications:
    if pub.bib['year'] >= 1980 and pub.bib['year'] <= 2002:
        row = {
            'Title': pub.bib['title'],
            'Author': pub.bib['author'],
            'Journal': pub.bib['journal'],
            'Year': pub.bib['year'],
            'Abstract': pub.bib['abstract']
        }
        data.append(row)

# Create a pandas DataFrame from the scraped data
df = pd.DataFrame(data)

# Print the DataFrame
print(df)



