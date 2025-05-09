import os
import re

def notice_license_search(outfile):
    for root, dirs, files in os.walk("/root/spring-framework/"):
        for file in files:
            if file.lower().startswith(('notice', 'license')):
                filepath=os.path.join(root,file)
                with open(filepath,"r") as fh:
                    content=fh.read()
                    with open(outfile, "a") as fh1:
                        fh1.write(filepath)
                        fh1.write("\n\n")
                        fh1.write(content)
                        fh1.write("\n\n")


if __name__=="__main__":
    outfile=input("Enter the output file name\n")
    notice_license_search(outfile)
