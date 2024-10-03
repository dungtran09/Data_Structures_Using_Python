import os

sizePath = os.path.getsize(os.getcwd())

path = os.getcwd()

listFiles = os.listdir(path)

isDict = os.path.isdir(os.getcwd())

print(listFiles)

for file in listFiles:
    print(os.path.join(path, file))

