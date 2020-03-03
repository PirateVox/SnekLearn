command1 = 'switchport trunk allowed vlan 1,2,3,5,8'
command2 = 'switchport trunk allowed vlan 1,3,8,9'

vlans = set((command1.split()[4]).split(',')) & set((command2.split()[4]).split(','))

print(list(sorted(vlans)))
