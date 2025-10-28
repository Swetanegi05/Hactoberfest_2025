filename = input("Enter file name:")

with open(filename, 'r') as f:
    data = f.read()
lines = data.split("\n")
words = data.split()
print(" Total lines:" , len(lines))
print(" Total words:", len(words))
