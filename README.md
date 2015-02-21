currently finds sqli other things coming when I find time :(

Two versions:
--first version uses mysqldb if you happen to have a lovely big database of attack strings
--Second version for us poor people who don't have a big db of attack strings, uses a regex to find them

requirements:
-scapy. I used scapy to extract the packet payload because it's a fantastic tool you should check it out: http://wwwsecdev.org/projects/scapy/
-If you are using the first version then you will need to install MySQLdb for python. You can get it from apt-get or pip

Nice site for getting regexs to match bad strings: http://regexlib.com/Search.aspx?k=sql&c=0&m=0&ps=20&p=2&AspxAutoDetectCookieSupport=1
