import pandas as pd


# Transform the json data to a csv file
def get_csv():
    df = pd.read_json('data.json')
    df.to_csv('data.csv',index=False)
