import sys
import os

with open("file1", "w") as fh:
    fh.write("Welcome to devops\n")
    fh.write("file created")

def read_file(file):
    if os.path.isfile(file):
       with open(file, "r") as fh:
           content=fh.read()
           #print(content)
       return(content)
    else:
       print("file doesnt exist")
       return("no content")

filename=input("Enter the filename\n")
display=read_file(filename)
print(display)
sys.exit("the execution stopped")


print(sys.argv[0],sys.argv[1])
print(sys.argv[2])
#sys.exit("the execution is stopped forcefully")
print(sys.argv)
print(sys.path)
#sys.exit("the execution is stopped forcefully")
print(os.getcwd())
os.makedirs("dir", exist_ok=True)
print(os.listdir("/root"))
os.chdir("/root/dir")
print(os.getcwd())
print(os.listdir())
#files=os.listdir()
os.chdir("/root")
files=os.listdir()
print(os.getcwd())
for file in files:
    if file.endswith(".py"):
        print(file)
print(os.path.basename("/root/dir"))
print(os.path.exists("/root/dir"))
for root, dirs, files in os.walk("/root"):
    print(root)
    print(dirs)
    print(files)

