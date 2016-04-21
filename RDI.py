import json
from collections import defaultdict
import unicodedata
import sys

print "calculating RDI"    
# calculating RDI     
writer = open("./Dataset/RDI.json","w")
papers =defaultdict(list)
p_id=[]
conference = defaultdict(str)
with open(sys.argv[1]) as reader :
  data = reader.readlines()
  for d in data:
  	temp = json.loads(d)
  	p_id.append(temp["id"])
  	papers[temp["id"]]=temp["citations"]
  	conference[temp["id"]] =unicodedata.normalize('NFKD', temp["conference"]).encode('ascii','ignore')
print "Data Load"

for p in p_id:
	print p
	conf_list=set() 
	for c in papers[p] :
		conf_list.add(conference[c])
	obj = json.JSONEncoder().encode({"id" : unicodedata.normalize('NFKD', p).encode('ascii','ignore') , "RDI" : list(conf_list) })
	writer.write(obj+"\n")
reader.close()
writer.close()
