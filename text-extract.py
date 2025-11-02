import fitz
import json

doc = fitz.open("source/sealed-nector.pdf")
text = ""
for pages in doc:
   text+= pages.get_text()
print(text)
   
with open(f"jsons/text.json","w") as f:
   json.dump(text,f)