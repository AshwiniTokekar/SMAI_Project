import json
from collections import defaultdict
import unicodedata
import sys

team_size = defaultdict(int) 
refcount = defaultdict(int)
rdi = defaultdict(set)
papers = []
writer = open("./Dataset/papercontentfeatures.json","w")
with open(sys.argv[1]) as reader :
  data = reader.readlines()
  print "calculating team size and refcount"
  for obj in data :
    d=json.loads(obj)
    d["conference"] = unicodedata.normalize('NFKD', d["conference"]).encode('ascii','ignore')
    d["id"] = unicodedata.normalize('NFKD', d["id"]).encode('ascii','ignore') 
    print d["id"]
    temp = []
    for i in d["citations"]:
      temp.append(unicodedata.normalize('NFKD', i).encode('ascii','ignore'))
    d["citations"] = temp  
    obj = json.JSONEncoder().encode({"id" : d["id"] , "team size" : len(d["authors"]),"Ref count" : len(d["citations"]) })
    writer.write(obj+"\n")
writer.close()   

    


  

