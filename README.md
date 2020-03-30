用于生成asus-merlin固件可用的geoip文件(geoipdb.bin, geoipdb.idx)

为什么需要单独写一个工具呢，xt_geoip不是自带了build工具么（/usr/lib/xtables-addons/xt_geoip_build），问题是asus-merlin使用的xt_geoip版本很老，数据文件格式和位置都不一样，也没有找到特别趁手的工具，而且Maxmind也不再提供直接的ip数据库下载链接了。

支持两种格式的IP地址文件：

1、Maxmind Legacy (https://legacy-geoip-csv.ufficyo.com/)

    ./build-from-maxmind.sh

2、APNIC (http://ftp.apnic.net/stats/apnic/delegated-apnic-latest)

    ./build-from-apnic.sh

根据偏好选择上面的某一个命令运行完毕，在当前目录下就会生成geoipdb.bin和geoipdb.idx文件，复制到/var/geoip目录下即可。

Q：选择Maxmind还是APNIC?

A： 我也还没来得及作详细的测试，简单的观察：APNIC的数据量看似比Maxmind小，那是因为APNIC只涵盖亚太区国家的数据，而且只比较中国区的地址段数目，APNIC明显更多（8485 vs 6065）。我们通常的使用场景是判断IP是否中国区即可，所以我选择APNIC。考虑到Maxmind是个商业公司，是否会通过人工的编辑使数据更精准，这个就不好说了。
