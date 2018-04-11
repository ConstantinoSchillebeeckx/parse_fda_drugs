# Parse FDA drugs

A quick script to download the [Drugs@FDA](https://www.fda.gov/Drugs/InformationOnDrugs/ucm079750.htm) data into a Postgres database; a similar repo for the [FDA Orange Book](https://www.accessdata.fda.gov/scripts/cder/ob/) is [also available](https://github.com/ConstantinoSchillebeeckx/parse_fda_orange).

This script will also parse the [Orphan Drug Database](https://www.fda.gov/forindustry/developingproductsforrarediseasesconditions/howtoapplyfororphanproductdesignation/ucm586177.htm).

A glossary of terms is found [online](https://www.fda.gov/drugs/informationondrugs/ucm079436.htm).

![schema](schema.png "schema")

## To run

**NOTE:** project assumes python3

```
pip install -r requirements.txt
./run.sh
```

**NOTE:** 

- no foreign key constraints are established between tables.
- all table names and table attributes are formatted with underscores and lowercase; for example the table name `ApplicationDocs` is created as `application_docs`.
- the `Products.txt` table has extra trailing tabs in lines 34517-24519 which were manually removed so that `insert.py` could run properly.
- the archive [fda_drugs_2018-04-09.zip](fda_drugs_2018-04-09.zip) is provided as a refernce for a set of data that currently works with this repo including the line fix mentioned above; note that these data are otherwise updated on a **weekly basis**.
