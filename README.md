用于生成asus-merlin固件可用的geoip文件(geoipdb.bin, geoipdb.idx)

为什么需要单独写一个工具呢，xt_geoip不是自带了build工具么（/usr/lib/xtables-addons/xt_geoip_build），问题是asus-merlin使用的xt_geoip版本很老，数据文件格式和位置都不一样，也没有找到特别趁手的工具，而且Maxmind也不再提供直接的ip数据库下载链接了。

支持两种格式的IP地址文件：

1、Maxmind Legacy (https://legacy-geoip-csv.ufficyo.com/)

    ./build-from-maxmind.sh

2、APNIC (http://ftp.apnic.net/stats/apnic/delegated-apnic-latest)

    ./build-from-apnic.sh

根据偏好选择上面的某一个命令运行完毕，在当前目录下就会生成geoipdb.bin和geoipdb.idx文件，复制到/var/geoip目录下即可。

Q：选择Maxmind还是APNIC?

我也还没来得及作详细的测试，简单的观察：Maxmind看似有大量人工编辑的条目，所以很多细碎的地址段；而APNIC粒度粗很多，而且只涉及亚太地区的数据，所以数据量小很多。按照我们一般会使用的路由规则，仅仅需要判断是否是中国IP，在这种场景下APNIC和Maxmind效果差别应该不大，而且APNIC数据精简很多！所以我选APNIC。
