#!/bin/bash

ip_data_uri="https://legacy-geoip-csv.ufficyo.com/Legacy-MaxMind-GeoIP-database.tar.gz"

tempDir=`mktemp -d`
if [ $? -ne 0 ]; then
    echo "mktemp failed"
    exit 1
fi 

wget ${ip_data_uri} -O - | tar -xvzf - -C ${tempDir}
if [ $? -ne 0 ]; then
    echo "file ${ip_data_uri} download failed"
    rm -rf ${tempDir}
    exit 1
fi

python3 build_geoip.py maxmind ${tempDir}/GeoIP-legacy.csv
if [ $? -ne 0 ]; then
    echo "build geoip failed"
fi

rm -rf ${tempDir}
