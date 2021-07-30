import ipaddress
from random import getrandbits
import ipaddress
from ipaddress import IPv4Address, IPv4Network, IPv4Interface

bytes1 = getrandbits(8)
bytes2 = getrandbits(8)
bytes3 = getrandbits(8)
bytes4 = getrandbits(8)
bytes5 = getrandbits(32)
print(type(bytes1))
#print(IPv4Network(bytes5).hosts())
print ("Hosts:", IPv4Network(bytes5).hosts())
addr = [bytes1,bytes2,bytes3,bytes4]
#print(str(addr).split('.'))
#print(type(addr))
print(*addr, sep=".")
#print(addr[0],".",addr[1],".",addr[2],".",addr[3],sep="")
print(format(bytes1,'08b'), format(bytes2,'08b'), format(bytes3,'08b'), format(bytes4,'08b'))

#net1 = ipaddress.IPv4Network("10.16.3.65/23")
ifc = IPv4Interface("10.16.3.65/23")
print(ifc.network)
#for addr1 in net1:
#     print(addr1)

while True:
    try:
        a = IPv4Interface(input('Enter IP address: '))
        #a1 = IPv4Network("10.16.3.65/23")
        #print("Hosts: ", list(a1.hosts()))
        print(a , "Netmask:", a.netmask, "Network:", a.network, "Hosts:", "Host mask:", a.hostmask)
        #print(IPv4Network(a).hosts())
        #n = a.hosts()
        #print(n)
        #b = int(a)
        #print(type(b))
        #print(format(b,'08b'))
       #break
    except ValueError:
        print("Introdu o adresa valida")
        continue

print(a)



"""def split_address(address):
    if ":" in address:
        split = address.split(":")
        address = split[0]
        port = int(split[1])
        return {"address": address, "port": port}
    else:
        return {"address": address}

split_address(25.244.52.85)

"""