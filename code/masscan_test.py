import masscan

# C'est la méthode simple et non rapide
masscan 192.168.0.0/16 --port 23,22

# C'est la méthode la plus rapide qui permet de faire un scan très rapide d'un réseau et des ports ouverts
masscan 192.168.0.0/16 --port 23,22,80,443 --banners --rate 10000 --heartbleed
# masscan 10.0.0.0/8 -p443 -S 10.1.2.53 --rate 100000 --heartbleed
# 10.0.0.0/8 = the network you want to scan, which is all 10.x.x.x
# -p443 = the port(s) you want to scan, in this case, the ones assigned to SSL
# -S 10.1.2.53 = an otherwise unused local IP address to scan from
# –rate 100000 = 100-packets/second, which scans the entire Class A range in a few minutes ===> Influe la précision et le nombres de résultats trouvés ??
# –heartbleed = the new option that reconfigures masscan to look for this vulnerability
# --banners demande à afficher les bannieres quand trouver

masscan 192.168.0.0/16 --port 23,22,80,443 --rate 5000 -oJ test.json
# pour diriger le résultat vers un json exploitable

mas = masscan.PortScanner()
mas.scan('172.0.8.78/24', ports='22,23,80,8080,443')
print (mas.scan_result)