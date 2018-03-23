import masscan

mas = masscan.PortScanner()
mas.scan('172.0.8.78/24', ports='22,23,80,8080,443')
print (mas.scan_result)