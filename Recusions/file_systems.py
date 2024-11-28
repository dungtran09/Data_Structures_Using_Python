import os

sizePath = os.path.getsize(os.getcwd())

print(sizePath)

path = os.getcwd()

listFiles = os.listdir(path)

isDict = os.path.isdir(os.getcwd())

print(listFiles)
