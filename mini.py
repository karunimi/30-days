# IT IS A MINI PROJECT DONE BY KARTHIKAA.R FROM CSE(Cyber security) 2nd Year
#I have created an student database with some details and displayed them
# I have also made an option to search an element from that details(for strings)
#also search is available for searching through their RRN



from elasticsearch import Elasticsearch
import pprint
es = Elasticsearch([{'host':'34.93.110.192','port':9200}])

# es.indices.create(index="database")
# a=es.indices.exists(index="database")
# print(a)

# doc_1={"name":"karthikaa",
#     "RRN":2101,
#     "Branch":"B.Tech",
#     "Department":"CSE(Cyber security)",
#     "year":"second year",
#     "DOB":"21-05-2004",
#     "gmail":"karthikaa@gmail.com"}
# doc_2={"name":"sarath.c.k",
#     "RRN":2102,
#     "Branch":"B.Tech",
#     "Department":"CSE(Cyber security)",
#     "year":"second year",
#     "DOB":"20-10-2003",
#     "gmail":"sarath@gmail.com"}
# doc_3={ "name":"nimitha",
#     "RRN":2103,
#     "Branch":"B.Tech",
#     "Department":"CSE(Cyber security)",
#     "year":"second year",
#     "DOB":"05-05-2003",
#     "gmail":"nimitha@gmail.com"}
# doc_4={ 
#     "name":"chitra",
#     "RRN":2104,
#     "Branch":"B.Tech",
#     "Department":"CSE(Cyber security)",
#     "year":"second year",
#     "DOB":"08-05-2004",
#     "gmail":"chitra@gmail.com"}
# doc_5={ "name":"varshini",
#     "RRN":2105,
#     "Branch":"B.Tech",
#     "Department":"CSE(Cyber security)",
#     "year":"second year",
#     "DOB":"25-07-2004",
#     "gmail":"varshini@gmail.com"}

# es.index(index="database", id=1, body=doc_1)
# es.index(index="database", id=2, body=doc_2)
# es.index(index="database", id=3, body=doc_3)
# es.index(index="database", id=4, body=doc_4)
# es.index(index="database", id=5, body=doc_5)

# for i in range(1,6):
#   res=es.get(index="database",id=i)
#   print(res["_source"])

#THIS PART IS FOR SEARCHING STUDENTS WITH THIER NAME
a=str(input("enter name:"))
body = {
    "from":0,
    "size":2000,
    "query": {
        "match": {
            "name":a
        }
    }
}
res = es.search(index="database", body=body)
print(res)


#THIS PART IS FOR SEARCHING STUDENTS WITH THEIR GMAILS
b=str(input("enter gmail:"))
body = {
    "from":0,
    "size":2000,
    "query": {
        "match": {
            "gmail":b
        }
    }
}
res = es.search(index="database", body=body)
print(res)


#THIS PART IS FOR SEARCHING STUDENTS WITH THEIR DOB
z=int(input("enter DOB to be searched:"))
body={
    "from":0,
    "size":2000,
    "query":{
        "match_phrase":{
            "DOB":z
        }
    }
}

res = es.search(index="database",body=body)
pprint.pprint(res["hits"]['hits'][0]["_source"])


#THIS PART IS FOR SEARCHING RRN
n=int(input("enter RRN to be searched:"))
body={
    "from":0,
    "size":2000,
    "query":{
        "match_phrase":{
            "RRN":n
        }
    }
}

res = es.search(index="database",body=body)
pprint.pprint(res["hits"]['hits'][0]["_source"])
#print(res['hits']['hits'][0]["_source"])