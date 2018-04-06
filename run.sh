#/bin/sh


# download data
curl https://www.fda.gov/downloads/Drugs/InformationOnDrugs/UCM527389.zip > dl.zip
unzip dl.zip -d raw

# create postgres DB
dropdb fda_nme --if-exists
createdb fda_nme

# insert data
./insert.py
