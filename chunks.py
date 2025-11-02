import json

with open("jsons/text.json","r") as f :
   text =  json.load(f)
    
chunks = []
chunk_size = 1000
chunk_overlap = 200

start = 0
while start < len(text):
    end = start + chunk_size
    chunk = text[start:end]
    chunks.append(chunk)
    start +=( chunk_size-chunk_overlap)

chunk_data = [{
    "chunk_id": i+1,
    "text": chunk}for i,chunk in enumerate(chunks)
              ]

with open("jsons/chunk_data.json","w") as f:
    json.dump(chunk_data,f) 
# for i in text:
#   chunks_size = text.split(".")
#   chunks.append({
    
#  })
   