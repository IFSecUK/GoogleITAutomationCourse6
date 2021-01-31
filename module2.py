#! /usr/bin/env python3

import os
import requests

list_of_files = os.listdir("/data/feedback")
#print(list_of_files)
fields = ["title", "name", "date", "feedback"]

for file in list_of_files:
  with open("/data/feedback/{}".format(file)) as f:
    lines = f.read().strip().split("\n")
    data_dict = {}
    i = 0
    for line in lines:
      data_dict[fields[i]] = line
      i += 1
    response = requests.post("http://35.239.53.9/feedback/", json=data_dict)
    print(response.status_code)
  f.close()

