import argparse
import pandas as pd
def convert_excel_json(excel_file,json_file):
    df=pd.read_excel(excel_file,sheet_name="Sheet1")
    df_strip=df.map(lambda x: x.strip() if isinstance(x,str) else x)
    df_strip.to_json(json_file,orient='records',indent=4)
    print("Excel file converted to json file successfully")
subparse=argparse.ArgumentParser(description="arguments for converting excel to json")
subparse.add_argument("excel_file",help="provide the name of excel file")
subparse.add_argument("json_file",help="provide the name of json file")
args=subparse.parse_args()
convert_excel_json(args.excel_file, args.json_file)
