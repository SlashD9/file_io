f = open('newfile.txt', 'a')
lines = ['hello', 'world', 'welcome', 'to', 'file io']
f.writelines(lines)
f.close()