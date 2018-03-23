from netmiko import Netmiko

my_device = {
    'host': '193.253.188.120:10443',
    'username': 'tibco-admin',
    'password': 'Tibco#44BLV',
    'device_type': 'fortinet',
}

net_connect = Netmiko(**my_device)

output = net_connect.send_command("show full-configuration")

print(output)

#Sortie Fichier
#sys.stdout = open(FortiConf.txt)

#with open('FortiConf.txt', 'w') as f
    #print ('Filename:', filename, file=f)

net_connect.disconnect()