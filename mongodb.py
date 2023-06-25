from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
uri = "mongodb+srv://barbarosyabaci:IxZzHfcoVPQShAGZ@cluster0.nor6m32.mongodb.net/?retryWrites=true&w=majority"
# Create a new client and connect to the server
client = MongoClient(uri, server_api=ServerApi('1'))
# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

import pandas as pd
db = client["Sites"]
Random_Tokyo = db["Random_Tokyo"]
df_tokyo = pd.read_csv("Random_Tokyo.csv",  index_col=False)
df_tokyo.reset_index(inplace=True)
df_tokyo_dict = df_tokyo.to_dict("records")

# Random_Tokyo.insert_one({"index":"Tokyo_Random","data":df_tokyo_dict})

filter = { 'Site Name': 'Barbaros_2'}
newvalues = { "$set": { 'Site Name': 'New' } }
result = Random_Tokyo.update_one(filter,newvalues,upsert = True)

print(result.matched_count)

Random_Tokyo.delete_one({"index":"Tokyo_Random_2"})

data_from_db = Random_Tokyo.find_one({"index":"Tokyo_Random"})

df = pd.DataFrame(data_from_db["data"])
df.set_index("Site Name",inplace=True)
print(df)









