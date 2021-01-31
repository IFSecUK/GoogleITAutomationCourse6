#! /usr/bin/env python3

import os
import requests
#Import the necessary modules required for the challenge.


list_of_files = os.listdir("/data/feedback")
#list all the files and store in the variable.
fields = ["title", "name", "date", "feedback"]
#List of keys

for file in list_of_files:
  with open("/data/feedback/{}".format(file)) as f:
    lines = f.read().strip().split("\n")
    #Remove all the whitespace characters and store a list of all the lines in the variable.
    data_dict = {}
    #Initialize a empty dictionary
    i = 0  #Counter variable
    for line in lines:
      data_dict[fields[i]] = line
      i += 1
      #setting the content and saving it with the respective key.
    response = requests.post("http://35.239.53.9/feedback/", json=data_dict)
    #Call the post method of the requests module and set the json attribute with the obtained dictionary.
    print(response.status_code)
  f.close()


