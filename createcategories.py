#!/usr/bin/python
import json
import sys
from collections import defaultdict
#PI = INITIAL PEAK
#PL = LATE PEAK
#MD = MONDEC
#MONINCR = MON INC
#OTH = OTHER
year=defaultdict(int)
refer = defaultdict(list)
B1 =defaultdict(int)
B2 =defaultdict(int)
B3 =defaultdict(int)
B4 =defaultdict(int)
B5 =defaultdict(int)
total =defaultdict(int)
cate =defaultdict(str)
p_id=[]
def getB1(paper_id):
	temp = refer[paper_id]
	year_p = year[paper_id]
	if year_p==0:
		return
	for t in temp:
		if year_p-year[t]<=3:
			B1[t] = B1[t]+1
	
def getB2(paper_id):
	temp = refer[paper_id]
	year_p = year[paper_id]
	if year_p==0:
		return 
	for t in temp:
		if year_p-year[t]>3 and year_p-year[t] <=6:
			B2[t] = B2[t]+1
	
def getB3(paper_id):
	temp = refer[paper_id]
	year_p = year[paper_id]
	if year_p==0:
		return 
	for t in temp:
		if year_p-year[t]>6 and year_p-year[t]<=9:
			B3[t] = B3[t]+1	

def getB4(paper_id):
	temp = refer[paper_id]
	year_p = year[paper_id]
	if year_p==0:
		return 
	for t in temp:
		if year_p-year[t]>9 and year_p-year[t]<=12:
			B4[t] = B4[t]+1
def getB5(paper_id):
	temp = refer[paper_id]
	year_p = year[paper_id]
	if year_p==0:
		return 
	for t in temp:
		if year_p-year[t]>12:
			B5[t] = B5[t]+1

def gettotal(paper_id):			
	temp = refer[paper_id]
	year_p = year[paper_id]
	if year_p==0:
		return 
	for t in temp:
		total[t] = total[t]+1
def decidecategory(paper_id):
	temp = []
	temp.append(B1[paper_id])
	temp.append(B2[paper_id])
	temp.append(B3[paper_id])
	temp.append(B4[paper_id])
	temp.append(B5[paper_id])
	if B1[paper_id]<=B2[paper_id]<=B3[paper_id]<=B4[paper_id]<=B5[paper_id]:
		return "MI"
	elif B1[paper_id]>=B2[paper_id]>=B3[paper_id]>=B4[paper_id]>=B5[paper_id]:
		return "MD"	
	elif max(temp)==B1[paper_id]:
		return "PI"
	elif max(temp)==B5[paper_id]:
		return "PL"		
	else :
		return "Oth"
def main():
		writer = open("./Dataset/categories.json","w")	
		with open(sys.argv[1]) as reader :
			data = reader.readlines()	
			for obj in data :
				obj_dict =json.loads(obj)
				p_id.append(obj_dict["id"])
				if obj_dict["year "] != '':
					year[obj_dict["id"]] = int(obj_dict["year "])
				else :
					year[obj_dict["id"]] = 0	
				refer[obj_dict["id"]] = obj_dict["citations"]
		
		for p in p_id:
			getB1(p)
			getB2(p)
			getB3(p)
			getB4(p)
			getB5(p)
			gettotal(p)	
		for p in p_id:
			if p not in B1:
				B1[p] = 0
			if p not in B2:
				B2[p] = 0
			if p not in B3:
				B3[p] = 0	
			if p not in B4:
				B4[p] = 0
			if p not in B5:
				B5[p] = 0										
		for p in p_id:
			cate[p]=decidecategory(p)
			obj = json.JSONEncoder().encode({"B1" : B1[p], "B2" : B2[p],"B3" : B3[p],"B4" : B4[p],"B5" : B5[p],"total" : total[p],"category" : cate[p]})
			writer.write(obj+"\n")	
		writer.close()	
main()				
