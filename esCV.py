from datetime import datetime
import matplotlib.pyplot as plt
from elasticsearch import Elasticsearch
from email.mime import image
import cv2 as cv
import sys
import numpy as np
es = Elasticsearch(hosts="http://localhost:9200")
black_image = np.zeros((500,1000,3), np.uint8)
black_image= black_image+200
culoareCautata = [8, 244, 255 ]
#hsv
#HSVculoareCautata = np.uint8([[[90, 255, 255 ]]])
#hhcc=[int(HSVculoareCautata[0][0][0]),int(HSVculoareCautata[0][0][1]),int(HSVculoareCautata[0][0][2])] 
#culoareCautata =cv.cvtColor(HSVculoareCautata,cv.COLOR_HSV2BGR)
#BGRculoareCautata = [int(culoareCautata[0][0][0]),int(culoareCautata[0][0][1]),int(culoareCautata[0][0][2])]


#culoareCautata = [int(cv.cvtColor(HSVculoareCautata,cv.COLOR_HSV2BGR)[0][0][0]),int(cv.cvtColor(HSVculoareCautata,cv.COLOR_HSV2BGR)[0][0][1]),int(cv.cvtColor(HSVculoareCautata,cv.COLOR_HSV2BGR)[0][0][2])]
#print("Conversie "+str(hhcc) +"->"+ str(BGRculoareCautata))
#cv.circle(black_image, [10,10], 10,BGRculoareCautata , -1)

cv.circle(black_image, [10,10], 10, culoareCautata, -1)
 
cv.putText(black_image, str(culoareCautata) + " <- Culoare cautata " , (20, 20), cv.FONT_HERSHEY_PLAIN, 1, (10,10, 10), 1)


resp = es.search(index="my-index-000001", query={"script_score": {
      "query" : {
        "bool" : {
          "filter" : {
            "term" : {
              "status" : "published" 
            }
          }
        }
      },
      "script": {
        "source": "cosineSimilarity(params.query_vector, 'my_dense_vector')", 
        "params": {
          "query_vector": culoareCautata
        }
      }
    }})
print("Got %d Hits:" % resp['hits']['total']['value'])
numar=0
for hit in resp['hits']['hits']:
    if(numar<10):
        #print("%(my_dense_vector)s %(status)s" % hit["_source"])
        numar=numar+1
       
        culoareCautata=[int(hit["_source"]["my_dense_vector"][0]),int(hit["_source"]["my_dense_vector"][1]),int(hit["_source"]["my_dense_vector"][2])]
        
        #hsv
        #HSVculoareCautata = np.uint8([[[int(hit["_source"]["my_dense_vector"][0]), int(hit["_source"]["my_dense_vector"][1]), int(hit["_source"]["my_dense_vector"][2]) ]]])        
        #hhcc=[int(HSVculoareCautata[0][0][0]),int(HSVculoareCautata[0][0][1]),int(HSVculoareCautata[0][0][2])] 
        #culoareCautata =cv.cvtColor(HSVculoareCautata,cv.COLOR_HSV2BGR)
        #BGRculoareCautata = [int(culoareCautata[0][0][0]),int(culoareCautata[0][0][1]),int(culoareCautata[0][0][2])]
        textT=str(hit["_source"]["my_dense_vector"])+" \t "+ str(hit["_score"]) +" \t "+ str(numar) +" \t "+ str(hit["_id"]) 
        print(textT)
        #print("Conversie "+str(hhcc) +"->"+ str(BGRculoareCautata))
        #culoareCautata = [int(cv.cvtColor(HSVculoareCautata,cv.COLOR_HSV2BGR)[0][0][0]),int(cv.cvtColor(HSVculoareCautata,cv.COLOR_HSV2BGR)[0][0][1]),int(cv.cvtColor(HSVculoareCautata,cv.COLOR_HSV2BGR)[0][0][2])]

        cv.circle(black_image, [10,50+30*numar], 10, culoareCautata, -1)
        cv.putText(black_image, str(textT), [30,55+30*numar], cv.FONT_HERSHEY_PLAIN, 1, (10,10, 10), 1)
        #print( hit["_score"])
        #print( hit["_source"]["my_dense_vector"])
cv.imshow("Display black_image", black_image)
k = cv.waitKey(0)
if k == ord("s"):
    cv.imwrite("c://STUFF/cautari.png", black_image)