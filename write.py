f = open('newfile.txt', 'a')
lines = ['hello', 'world', 'welcome', 'to', 'file io']
text = '\n'.join(lines)
f.writelines(text)
f.close()