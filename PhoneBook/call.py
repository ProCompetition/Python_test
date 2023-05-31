'''
path = 'call.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()
'''

def open_file_read(path):
    with open(path, 'r') as file:
        main_list = file.readline()
        main_list_str = [x.rstrip().split(':') for x in main_list]
        return main_list_str

print(open_file_read('phone.txt'))

def open_file_write(path,file):
    with open(path, 'w') as file:
        file.writelines([':'. join('x') for x in file])
list_for_look = [[]]
def look_list(list_for_look):
    print([' '.join(x) for x in list_for_look], end = '\n')

look_list(list_for_look)

