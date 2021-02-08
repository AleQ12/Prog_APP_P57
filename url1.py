# -*- coding: utf-8 -*-
"""
Created on Wed Jan 27 08:03:46 2021

@author: USUARIO
"""

import urllib.parse
import requests
main_api = "https://www.mapquestapi.com/directions/v2/route?"
orig = "Quito"
dest = "Guayaquil"
key = "i6rS3UyzOvPp577i65MUIGluTEUJASnC"
url = main_api + urllib.parse.urlencode({"key": key, "from":orig, "to":dest})
json_data = requests.get(url).json()
print(json_data)