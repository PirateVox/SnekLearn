form = '''Protocol:               {}
Prefix:                 {}
AD/Metric:              {}
Next-Hop:               {}
Last update:            {}
Outbound Interface:     {}'''

ospf_route = 'OSPF     10.0.24.0/24 [110/41] via 10.0.13.3, 3d18h, FastEthernet0/0'

ospf_route = ospf_route.split()
ospf_route[2] = ospf_route[2].strip('[]')
ospf_route[4] = ospf_route[4].strip(',')
ospf_route[5] = ospf_route[5].strip(',')

print(form.format(ospf_route[0], ospf_route[1], ospf_route[2] ,ospf_route[4], ospf_route[5], ospf_route[6]))
