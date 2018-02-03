f = open("data.txt", "a+")
f.write("\nLine 4")
f.write("\nLine 5")
f.close()

f = open("data.txt", "r")
lines = f.readlines()
print(lines[3])
print(lines[4])
f.close()

