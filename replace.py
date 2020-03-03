NAT = "ip nat inside source list ACL interface FastEthernet0/1 overload"

NAT = NAT.replace('FastE', 'GigabitE')

print(NAT)
