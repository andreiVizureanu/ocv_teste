from datetime import datetime
import random
import cv2
import matplotlib.pyplot as plt
from elasticsearch import Elasticsearch
es = Elasticsearch(hosts="http://localhost:9200")




i = 1
while i < 5000:
    print(i)
    i += 1
    culoareCautata = [random.randint(1, 255), random.randint(1, 255), random.randint(1, 255)]
    doc = {
        "my_dense_vector": culoareCautata,
        "status" : "published"
    }
    resp = es.index(index="my-index-000001", document=doc)
    #print(resp['result'])



es.indices.refresh(index="test-index")
