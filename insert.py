#!/usr/bin/env python

import pandas as pd
import os
from sqlalchemy import create_engine

'''
Script will load all of the Drugs@FDA data into a postgres database by 
the name of `fda_nme`

Assumes that data was downloaded and extracted into the directory `raw/` 
and that a postgres server is running on local host with write privileges 
for user running this script.
'''


# connect to DB
# assumes current user has read/write access
conn = create_engine('postgresql://localhost/fda_nme')


for file in os.listdir('raw'):
    
    # filename without extension
    name = os.path.splitext(file)[0]
    
    # read data
    df = pd.read_csv('raw/'+file, sep='\t', encoding = "ISO-8859-1")
    
    # insert data
    print("Loading data for %s" %name)
    df.to_sql(name, con=conn, if_exists='replace')

