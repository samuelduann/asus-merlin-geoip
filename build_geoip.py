#! python3
import sys
import struct
import socket
from collections import defaultdict

def apnic2bin(filename):
    # http://ftp.apnic.net/stats/apnic/delegated-apnic-latest
    # apnic|TH|ipv4|1.0.128.0|32768|20110408|allocated
    records = defaultdict(list)
    for line in open(filename):
        if line[0] == '#':
            continue
        fields = line.strip().split('|')
        if fields[2] != 'ipv4':
            continue
        if fields[1] == '*':
            continue
        cc = fields[1]
        b = struct.unpack('!I', socket.inet_aton(fields[3]))[0]
        e = b | (int(fields[4])-1)
        records[cc].append([b, e])

    for r in records:
        records[r].sort()
        records[r] = records[r][:65535]

    with open('geoipdb.bin', 'wb') as fp:
        for r in sorted(records.keys()):
            fp.write(bytes(r[::-1], 'utf-8'))
            fp.write(len(records[r]).to_bytes(2, 'little'))
            for b, e in records[r]:
                fp.write(b.to_bytes(4, 'little'))
                fp.write(e.to_bytes(4, 'little'))
    offset = 0
    with open('geoipdb.idx', 'wb') as fp:
        for r in sorted(records.keys()):
            fp.write(bytes(r[::-1], 'utf-8'))
            fp.write(offset.to_bytes(4, 'little'))
            offset += 2 + 2 + 8 * len(records[r])

def csv2bin(filename):
    # https://legacy-geoip-csv.ufficyo.com/
    records = defaultdict(list)
    for line in open(filename):
        fields = line.strip().split(',')
        cc = fields[4][1:-1]
        records[cc].append([int(fields[2][1:-1]), int(fields[3][1:-1])])

    for r in records:
        records[r].sort()
        records[r] = records[r][:65535]

    with open('geoipdb.bin', 'wb') as fp:
        for r in sorted(records.keys()):
            fp.write(bytes(r[::-1], 'utf-8'))
            fp.write(len(records[r]).to_bytes(2, 'little'))
            for b, e in records[r]:
                fp.write(b.to_bytes(4, 'little'))
                fp.write(e.to_bytes(4, 'little'))
    offset = 0
    with open('geoipdb.idx', 'wb') as fp:
        for r in sorted(records.keys()):
            fp.write(bytes(r[::-1], 'utf-8'))
            fp.write(offset.to_bytes(4, 'little'))
            offset += 2 + 2 + 8 * len(records[r])

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print(f'usage: python {sys.argv[0]} <csv file>')
        exit(1)
    #csv2bin(sys.argv[1])
    apnic2bin(sys.argv[1])
