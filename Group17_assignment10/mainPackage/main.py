# Name: Logan Schuster
# email: schustlt@mail.ec.edu
# Assignment Title: Assignment 10
# Due Date: 11-09-2023
# Course: IS 4010
# Semester/Year: Fall 2023
# Brief Description: This project shows we can execute an API call using a URL
# Citations:n/a
# Anything else that's relevant:n/a

import requests

if __name__ == "__main__":
    url = "https://morning-star.p.rapidapi.com/stock/v2/get-realtime-data"
    querystring = {"performanceId":"0P0000OQN8"}
    headers = {
        "X-RapidAPI-Key": "3c5a7e2a0amsh58812b33ac3f453p19111ajsn26ab0c475f52",
        "X-RapidAPI-Host": "morning-star.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)
    
    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        data = response.json()
        
        dayRangeHigh = data.get("dayRangeHigh")
        dayRangeLow = data.get("dayRangeLow")
        lastClose = data.get("lastClose")
    
        print(f"Day Range High: {dayRangeHigh}")
        print(f"Day Range Low: {dayRangeLow}")
        print(f"Last Close: {lastClose}")
        
        
        
        
        
        