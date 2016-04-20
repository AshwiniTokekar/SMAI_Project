#!/usr/bin/python3
from json import JSONEncoder
import sys;
#This module reads data and converts it to json objects and writes in a file
def getdata(input):
	if input=="":
		return ""
	inf = input.split("\n")
	s = ""
	title=inf[0].replace("#*","")
	authors=inf[1].replace("#@","").split(",")
	time=inf[2].replace("#t","")
	index=inf[4].replace("#index","")
	conf = inf[3].replace("#c","")
	for i in range(5,len(inf)):
		if inf[i].find("#%")!=-1:
			temp=inf[i].replace("#%","")
			if temp!="":
				s+=temp
				s+=","				
	s=s.split(",")	
	del s[-1]
	return JSONEncoder().encode({"id" :index, "title" :title, "authors": authors, "year ":time , "citations" : s, "conference":conf})
def dataextraction():
	writer=open(sys.argv[2],"w")
	with open(sys.argv[1]) as reader :
		temp =""
		for line in reader :
				if "#*" in line:		
					paper_inf = getdata(temp)
					temp=""
					if paper_inf!="":
						writer.write(paper_inf+"\n")
				print line
				temp+=line.decode('utf-8').strip()
				temp+="\n"
					
	
	reader.close()
	writer.close()

def main():
	reload(sys)  
	sys.setdefaultencoding("ISO-8859-1")
	dataextraction()
main()
