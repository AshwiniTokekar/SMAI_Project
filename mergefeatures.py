#!/usr/bin/python3
import json
import sys
from collections import defaultdict
import csv
authdiv=defaultdict(int)
ProAuth=defaultdict(int)
sociality = defaultdict(int)
hindex = defaultdict(int)

def main():
	writer = open("./Dataset/final.json","w")
	f=open("./Dataset/final.csv","w")
	writer2 = csv.writer(f)
    
	reader_paperwise = open("./Dataset/papercontentfeatures.json")
	pap = reader_paperwise.readlines()
	reader_authwise = open("./Dataset/authorwisefeatures.json")
	authors = reader_authwise.readlines()
	dataset = open("./Dataset/jsonfiles/dataset.json")
	data = dataset.readlines()
	
	for a in authors:
		obj = json.loads(a)
		authdiv[obj["author"]] = int(obj["Diverstiy"])
		ProAuth[obj["author"]] = int(obj["Productivity"])
		sociality[obj["author"]] = int(obj["sociality"])
		hindex[obj["author"]] = int(obj["hindex "])
	for i in range(len(data)):
		obj = json.loads(data[i])
		paper_wise = json.loads(pap[i])
		auth = obj["authors"]
		avgh=0
		avgsoc=0
		avgprod=0
		avgdiv=0
		for a in auth:
			avgh +=hindex[a]
			avgsoc+=sociality[a]
			avgprod+=ProAuth[a]
			avgdiv+=authdiv[a]
		avgh/=len(auth)
		avgsoc/=len(auth)
		avgprod/=len(auth)		
		avgdiv/=len(auth)
		temp_list = []
		temp_list.append(paper_wise["B1"])
		temp_list.append(paper_wise["B2"])
		temp_list.append(paper_wise["B3"])
		temp_list.append(paper_wise["B4"])
		temp_list.append(paper_wise["B5"])
		temp_list.append(paper_wise["total_cite"])
		temp_list.append(paper_wise["team size"])
		temp_list.append(paper_wise["Ref count"])
		temp_list.append(avgh)
		temp_list.append(avgsoc)
		temp_list.append(avgprod)
		temp_list.append(avgdiv)
		if paper_wise["category"] == "PI":
			temp_list.append(1)
		elif paper_wise["category"] =="PL":	
			temp_list.append(2)
		elif paper_wise["category"] =="MI":
			temp_list.append(3)
		elif paper_wise["category"] =="MD":
			temp_list.append(4)
		else:
			temp_list.append(5)

		obj_w = json.JSONEncoder().encode({"B1" : paper_wise["B1"], "B2" : paper_wise["B2"],"B3" : paper_wise["B3"],"B4" : paper_wise["B4"],"B5" : paper_wise["B5"],"total_cite" : paper_wise["total_cite"],"category" : paper_wise["category"],"avghindex":avgh,"avgsociality":avgsoc,"avgproductivity":avgprod,"avgdiversity":avgdiv,"team size" : paper_wise["team size"],"Ref count" : paper_wise["Ref count"]})
	#	obj_n=temp_list
	#	print temp_list
		writer.write(obj_w+"\n")
		writer2.writerow([temp_list])
	writer.close()
	f.close()

main()

