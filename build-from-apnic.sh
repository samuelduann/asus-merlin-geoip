#!/bin/bash

ip_data_uri="http://ftp.apnic.net/stats/apnic/delegated-apnic-latest"

tempDir=`mktemp -d`
if [ $? -ne 0 ]; then
    echo "mktemp failed"
    exit 1
fi 

wget ${ip_data_uri} -P ${tempDir}
if [ $? -ne 0 ]; then
    echo "file ${ip_data_uri} download failed"
    rm -rf ${tempDir}
    exit 1
fi

python3 build_geoip.py apnic ${tempDir}/delegated-apnic-latest
if [ $? -ne 0 ]; then
    echo "build geoip failed"
fi

rm -rf ${tempDir}
