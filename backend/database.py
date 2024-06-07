import asyncio
from pyairtable import Api, Table
import pandas as pd
import configparser


# configuration file parsing
config = configparser.ConfigParser()
config.read("configfile.ini")
db_cfg = config["db"]

api = Api(db_cfg["ACCESS_TOKEN"])
database_id = db_cfg["DATABASE_ID"]

# tables reading (need to be changed)
sample_table = api.table(database_id, 'Users')


def get_header(table: Table) -> list:
    '''Get the full header from airtable database'''
    
    header = set()
    for record in table.all():
        for key in record["fields"].keys():
            header.add(key)
            
    header = list(header)
    return header
    

async def load_data(table: Table, header: list, view: str = None) -> pd.DataFrame:
    '''Form a pandas dataframe from airtable database table using set of columns and view (optional)'''
    
    data = {}
    for column in header:
        data[column] = list()

    for record in table.all(view=view):
        for column in data.keys():
            if column not in record["fields"].keys():
                if column == "Активный":
                    record["fields"][column] = False
                else:
                    record["fields"][column] = ""
            data[column].append(record["fields"][column])

    data = pd.DataFrame(data)
    return data
