import json
import sys
def process_json():
    filename=input("Enter the json file name to read\n")
    with open(filename,"r") as fh:
        json_content=json.load(fh)
        for ele in json_content:
            for key, val in ele.items():
                if key=="Source URL":
                    print(key, val)
            sys.exit(0)

if __name__=="__main__":
    process_json()
