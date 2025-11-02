import requests
import os 
import joblib
import json 
import pandas as pd

def create_embedding(input_list):
    r = requests.post("http://localhost:11434/api/embed", json={
        "model": "bge-m3",
        "input": input_list,
    })
    embed = r.json()["embeddings"]
    return embed

jsons = os.listdir("jsons")
chunk_id = 0
chunk_dict = []

with open("jsons/chunk_data.json", "r") as f:
    contents = json.load(f)

# Use batching here instead of embedding all at once
batch_size = 50
embeddings = []
for i in range(0, len(contents), batch_size):
    batch = [c["text"] for c in contents[i:i+batch_size]]
    batch_embeddings = create_embedding(batch)
    embeddings.extend(batch_embeddings)
    print(f" Processed {i+len(batch)} / {len(contents)} chunks")


for j, chunk in enumerate(contents):
    chunk["chunk_id"] = j + 1
    chunk["chunk_embeddings"] = embeddings[j]
    chunk_dict.append(chunk)

print(" All chunks processed successfully!")
print(chunk_dict) 
df = pd.DataFrame.from_records(chunk_dict)
joblib.dump(df, "embeddings.joblib")