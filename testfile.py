import os
from shutil import copyfile
path = "/home/mininet/mininet/"
print("original list of files")
print(os.listdir(path))
print("creating the file testfile")
print(os.listdir(path))
f = open("/home/mininet/mininet/testfile.txt", "w")
f.write("This is a test")
f.close

f = open("/home/mininet/mininet/testfile.txt", "r")
print(f.read())

print("renaming testfile to changedtestfile")
print(os.listdir(path))
os.rename("/home/mininet/mininet/testfile.txt", "/home/mininet/mininet/changedtestfile.txt")
print(os.listdir(path))
print("Changing changedtestfile back to testfile")
os.rename("/home/mininet/mininet/changedtestfile.txt", "/home/mininet/mininet/testfile.txt")
print(os.listdir(path))

print("copying testfile to mininet/custom")
copyfile("/home/mininet/mininet/testfile.txt", "/home/mininet/mininet/custom/testfiletest.txt")
print(os.listdir("/home/mininet/mininet/custom"))
print("removing testfile")
os.remove("/home/mininet/mininet/testfile.txt")
print(os.listdir(path))

# alternate to shutil.copyfile

os.popen("cp /home/mininet/mininet/testf.txt /home/mininet/mininet/test2.txt")
