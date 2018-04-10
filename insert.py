#!/usr/bin/env python

import pandas as pd
import os, re, sys
import utils
from utils import camel_case_to_underscore_lower as camel
from sqlalchemy import create_engine

'''
Script will load all of the Drugs@FDA data into a postgres database of
the name defined by the first sys.argv:
python insert.py table_name

Assumes that data was downloaded and extracted into the directory `raw/` 
and that a postgres server is running on local host with write privileges 
for user running this script.
'''





assert len(sys.argv) == 2, "You must provide a database name."


# connect to DB
# assumes current user has read/write access
conn = create_engine('postgresql://localhost/' + sys.argv[1])


for file in os.listdir('raw'):
    
    # filename without extension
    name = camel(os.path.splitext(file)[0])
    
    # read data
    df = pd.read_csv('raw/'+file, sep='\t', encoding = "ISO-8859-1")
    df.columns = [camel(l) for l in df.columns]
    
    # insert data
    print("Loading data for %s ..." %name)
    df.to_sql(name, con=conn, if_exists='replace', index=False)

