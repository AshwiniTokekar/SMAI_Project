import json
from collections import defaultdict
import unicodedata
import sys
#Calculating reference diversity index
#Creating two dictionaries for citations and conference in which paper is published.
#Then for each citation checking in conference dictionary in which conference the paper has been published and then adding to the list
print "calculating RDI"    
# calculating RDI     
writer = open("./Dataset/RDI1.json","w")
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
	obj = json.JSONEncoder().encode({"RDI" : len(list(conf_list)) })
	writer.write(obj+"\n")
reader.close()
writer.close()
