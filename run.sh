#/bin/sh

# download data
curl https://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM527389.zip > dl.zip
unzip dl.zip -d raw

# create postgres DB
db="fda_nme"
dropdb $db --if-exists
createdb $db

# insert data
# NOTE: this step may fail due to a malformed Products.txt; see the README
./insert.py $db

# insert orphan drug data
./scrape_orphan_status.py $db

# create convenience view
psql -d $db -a -f views.sql
