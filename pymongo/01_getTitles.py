import pymongo

client = pymongo.MongoClient()
db = client.movie
titles = db.titles

docs = list(titles.find({'title': 'Dhoom'}))
print(f"")

for doc in docs:
    print("{")
    for key,v in doc.items():
        print(f"\t{key}: {v}")
    print("}")
