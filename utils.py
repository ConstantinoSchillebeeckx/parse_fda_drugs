import re

def camel_case_to_underscore_lower(name):
    """
    Convert a camel-case name, e.g. someCamelCase into an underscore
    delimited, lower-case version, e.g. some_camel_case. Any all
    caps name, e.g. TE, will simply be lower-cased, e.g. te

    https://stackoverflow.com/a/7322356/1153897
    """

    name = re.sub('\s+', '', name)
    name = name.replace('ID','Id').replace('FDA','Fda').replace('URL','Url')
    name = name.replace("&nbsp", "").replace('_','')

    if name.isupper():
        name = name.lower()
    else:
        name = re.sub( '(?<!^)(?=[A-Z])', '_', name ).lower()

    return name



from utils import camel_case_to_underscore_lower as camel
import pandas as pd
import numpy as np
def xml_to_df(table):
    '''
    Reformat the 'detailed' POST response into a Pandas dataframe
    with each row as an orphan drug
    '''

    row_dat = {}
    all_dat = []
    for l in table.xpath('//tr'):
        td = l.xpath('td')
        th = l.xpath('th')

        for i,j in enumerate(th):
            key = camel(j.text_content().strip().replace(':',''))
            value = td[i].text_content().strip()

            # if on new orphan, store previous results
            # and re-initialize row dict
            if key == 'result_number':
                if len(row_dat):
                    all_dat.append(row_dat)

                row_dat = {}

            row_dat[key] = value

    all_dat.append(row_dat)
    
    df = pd.DataFrame(all_dat)
    df.set_index('result_number', inplace=True)
    df.replace('N/A', np.nan, inplace=True)
    df.replace('TBD', np.nan, inplace=True)

    df = make_dates(df)
    
    return df

def make_dates(df):
    '''
    Convert any columns with 'date' in the name to a datetime column.
    '''

    # convert to datetime
    for l in df.columns:
        if 'date' in l.lower():
            df[l] = pd.to_datetime(df[l], infer_datetime_format=True)

    return df


def make_int(df):
    '''
    Convert any columns with 'id' in the name to a int column.
    '''

    # convert to int
    for l in df.columns:
        if 'int' in l.lower():
            df[l] = df[l].astype(int)

    return df
