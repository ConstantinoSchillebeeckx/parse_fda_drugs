# Parse FDA drugs

A quick script to download the [Drugs@FDA](https://www.fda.gov/Drugs/InformationOnDrugs/ucm079750.htm) data into a Postgres database.

To run:
```
pip install -r requirements.txt
./run.sh
```

**NOTE:** the `Products.txt` table has extra trailing tabs in lines 34517-24519 which were manually removed so that `insert.py` could run properly.
