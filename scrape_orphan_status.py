#!/usr/bin/env python

import pandas as pd
from lxml import html
import requests, sys
import utils
from sqlalchemy import create_engine



assert len(sys.argv) == 2, "You must provide a database name."

# connect to DB
# assumes current user has read/write access
conn = create_engine('postgresql://localhost/' + sys.argv[1])

url = 'https://www.accessdata.fda.gov/scripts/opdlisting/oopd/OOPD_Results.cfm'

form_data = {
    'Product_name': '*',
    'RecordsPerPage': '10000', # at time of writing there are 4532 orphans
    'Search_param': 'DESDATE',
    'Output_Format': 'Detailed',
    'newSearch': 'Run Search',
    'Sort_order': 'GENNAME'
}

# get data
print("Scraping orphan drug data...")
response = requests.post(url, data=form_data)
tree = html.fromstring(response.content)
table = tree.find_class('resultstable')

if len(table) == 1:
    df = utils.xml_to_df(table[0])
    df.to_sql('orphan_drugs', con=conn, if_exists='replace', index=False)

    print("Results written to table %s.orphan_drugs" %sys.argv[1])
else:
    print("No data found")
