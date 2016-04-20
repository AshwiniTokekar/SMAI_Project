#!/usr/bin/python3
import json
import sys
from collections import defaultdict
import unicodedata
#Code for finding author related features in dataset
def main():
	authors = defaultdict(set)
	conferences = defaultdict(set)
	authdiv=defaultdict(int)
	citation_count = defaultdict(int)
	citations =defaultdict(list)
	publications =defaultdict(list)
	ProAuth=defaultdict(int)
	sociality = defaultdict(int)
	hindex = defaultdict(int)
	with open(sys.argv[1]) as reader :
		data = reader.readlines()	
		for obj in data :
			obj_dict =json.loads(obj)
			auth_list = obj_dict["authors"]
			ref_list = obj_dict["citations"]
			obj_dict["id"]=unicodedata.normalize('NFKD', obj_dict["id"]).encode('ascii','ignore')
			obj_dict["conference"] = unicodedata.normalize('NFKD', obj_dict["conference"]).encode('ascii','ignore')
			for a in auth_list:
				a=unicodedata.normalize('NFKD',a).encode('ascii','ignore')
				if a!="":
					publications[a].append(obj_dict["id"])
					conferences[a].add(obj_dict["conference"])
				for b in auth_list:
					if a!=b:
						b = unicodedata.normalize('NFKD', b).encode('ascii','ignore')
						authors[a].add(b)

			for r in ref_list :
				r=unicodedata.normalize('NFKD', r).encode('ascii','ignore')
				citation_count[r]+=1	
				citations[r].append(obj_dict["id"])		

		#Sociality,Productivity,Diverstiy calculation		
		for a in authors:
		#	print "authors "+a
			sociality[a]=len(authors[a])
			ProAuth[a]=len(publications[a])
			authdiv[a]=len(conferences[a])

		#H-index calculation	
		for a in publications:
			pub_list = publications[a]
			temp=[]
			for l in pub_list:
				temp.append(citation_count[l])
			temp.sort(reverse=True)
			for i in range(len(temp)):
				if i>=temp[i]:
					hindex[a]=i
		
	#	print sociality	
	#	print publications
	#	print authors
	#	print citations
	#	print citation_count
	#	print hindex
	#	print conferences
	#	print authdiv
	writer = open("./Dataset/authorwisefeatures.json","w")
	for a in authors:
		obj = json.JSONEncoder().encode({"author": a, "hindex ":hindex[a] , "sociality" : sociality[a], "Diverstiy":authdiv[a],"Productivity":ProAuth[a]})
		writer.write(obj+"\n")
	writer.close()	
			
main()		