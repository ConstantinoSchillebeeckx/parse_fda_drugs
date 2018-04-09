#!/usr/bin/env python

import pandas as pd
import os, re
from sqlalchemy import create_engine

'''
Script will load all of the Drugs@FDA data into a postgres database by 
the name of `fda_nme`

Assumes that data was downloaded and extracted into the directory `raw/` 
and that a postgres server is running on local host with write privileges 
for user running this script.
'''



def camel_case_to_underscore_lower(name):
    """
    Convert a camel-case name, e.g. someCamelCase into an underscore
    delimited, lower-case version, e.g. some_camel_case. Any all
    caps name, e.g. TE, will simply be lower-cased, e.g. te

    https://stackoverflow.com/a/7322356/1153897
    """

    if name.isupper():
        return name.lower()
    else:
        name = name.replace('ID','Id').replace('_','')
        return re.sub( '(?<!^)(?=[A-Z])', '_', name ).lower()




# connect to DB
# assumes current user has read/write access
conn = create_engine('postgresql://localhost/fda_nme')


for file in os.listdir('raw'):
    
    # filename without extension
    name = camel_case_to_underscore_lower(os.path.splitext(file)[0])
    
    # read data
    df = pd.read_csv('raw/'+file, sep='\t', encoding = "ISO-8859-1")
    df.columns = [camel_case_to_underscore_lower(l) for l in df.columns]
    
    # insert data
    print("Loading data for %s" %name)
    df.to_sql(name, con=conn, if_exists='replace', index=False)

