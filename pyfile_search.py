import os
def file_search():
    for root, dir, files in os.walk("/root/"):
        for file in files:
            if file.endswith(".py"):
                print(file,root)


file_search()
