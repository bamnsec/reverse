import socket
from termcolor import colored

print(colored('''


 ______    _______  __   __  _______  ______    _______  _______
|    _ |  |       ||  | |  ||       ||    _ |  |       ||       |
|   | ||  |    ___||  |_|  ||    ___||   | ||  |  _____||    ___|
|   |_||_ |   |___ |       ||   |___ |   |_||_ | |_____ |   |___
|    __  ||    ___||       ||    ___||    __  ||_____  ||    ___|
|   |  | ||   |___  |     | |   |___ |   |  | | _____| ||   |___
|___|  |_||_______|  |___|  |_______||___|  |_||_______||_______|

''', 'green'))
print('\n')
print(colored('A Simple Script To Perform Reverse DNS Lookups On A List of IPs', 'green'))

print('\n')
list = input('Enter Target List: ')
print('\n')
#print('Target List: ' + list)
targets = open(list, 'r')
print('-' * 30)
for ip in targets:
    try:
        print('\n')
        print(colored('[*] IP: ' + ip, 'yellow'))
        rev_dns = socket.gethostbyaddr(ip)
        print('\n')
        print(colored('[+] Hostname: ' + rev_dns[0], 'green'))
        print('\n')
        print('-' * 30)
        print('\n')
    except socket.herror:
        print('\n')
        print(colored('[!] Reverse DNS Lookup Error', 'red'))
        print('\n')
        print('-' * 30)
        pass

print('-' * 30)
print('\n')
print('[*] Reverse DNS Lookups Complete')
print('\n')
