form = '{:10}{:10}{:10}{:10}'

ip = input().split('.')

print(form.format(ip[0], ip[1], ip[2], ip[3]))

form = '{:08b}  {:08b}  {:08b}  {:08b}'

#ip = [bin(int(ip[0])).split('0b')[1], bin(int(ip[1])).split('0b')[1],
#      bin(int(ip[2])).split('0b')[1], bin(int(ip[3])).split('0b')[1]]

print(form.format(int(ip[0]), int(ip[1]), int(ip[2]), int(ip[3])))
