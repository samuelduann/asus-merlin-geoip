用于生成asus-merlin固件可用的geoip文件(geoipdb.bin, geoipdb.idx)

为什么需要单独写一个工具呢，xt_geoip不是自带了build工具么（/usr/lib/xtables-addons/xt_geoip_build），问题是asus-merlin使用的xt_geoip版本很老，数据文件格式和位置都不一样，也没有找到特别趁手的工具，而且Maxmind也不再提供直接的ip数据库下载链接了。

支持两种格式的IP地址文件：

1、Maxmind Legacy (https://legacy-geoip-csv.ufficyo.com/)

    ./build-from-maxmind.sh

2、APNIC (http://ftp.apnic.net/stats/apnic/delegated-apnic-latest)

    ./build-from-apnic.sh
