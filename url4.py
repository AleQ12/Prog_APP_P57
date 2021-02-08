# -*- coding: utf-8 -*-
"""
Created on Fri Jan 29 08:03:46 2021

@author: USUARIO
"""

import urllib.parse
import requests

main_api = "https://www.mapquestapi.com/directions/v2/route?"
while True:
    orig = input("Locatizacion de inicio:")
    if orig == "quit" or orig == "q":
        break
    dest = input("Destino: ")
    if dest == "quit" or dest == "q":
        break
    key = "i6rS3UyzOvPp577i65MUIGluTEUJASnC"
    url = main_api + urllib.parse.urlencode({"key": key, "from": orig, "to": dest})
    print ("URL: " + (url))
    
    
    json_data = requests.get(url).json()
    json_status = json_data["info"]["statuscode"]
    

    if json_status == 0:
        print("API Status: " + str(json_status) + " = A successful route call.\n")
        print("Directions from: " + (orig) + " to " + (dest))
        print("Trip Duration:  " + str(json_data["route"]["formattedTime"]))
        print("Kilometres:     " + str("{:.2f}".format((json_data["route"]["distance"])*1.61)))
        print("Fuel(Gal):      " + str("{:.2f}".format((json_data["route"]["fuelUsed"])*3.78)))
        print("================================================")
        for each in json_data["route"]["legs"][0]["maneuvers"]:
            print((each["narrative"]) + " ("+ str("{:.2f}".format((each["distance"])*1.61) + " Km)"))
        print("================================================")
    elif json_status == 402:
        print("************************************************")
        print("For status Code: " + str(json_status) + ";Invalid user inputs for one or both locations.")
        print("************************************************\n")
        print("================================================")
    else:
        print("***************************************************************")
        print("For Status Code: " + str(json_status) + ", Refer to:")
        print("https://developer.papquest.com/documentation/directions-api/status-codes")
        print("****************************************************************\n")