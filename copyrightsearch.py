import os
import re

def search_copyright(outfile):
    for root, dirs, files in os.walk("/root/spring-framework/"):
        for file in files:
            if file.endswith(".java"):
                filepath=os.path.join(root,file)
                with open(filepath,"r") as fh:
                    lines=fh.readlines()
                    for line in lines:
                        if re.search(r"copyright",line,re.IGNORECASE):
                            with open(outfile, "a") as fh1:
                               # fh1.write(file)
                                fh1.write(line)
                               # fh1.write(file)

if __name__=="__main__":
    outfile=input("Enter the output file name\n")
    search_copyright(outfile)

