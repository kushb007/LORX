import requests

apiToken = "a907a3e1b6bc9d3174d157536908d5a7"
company = "microsoft"


response = requests.get("https://tf689y3hbj.execute-api.us-east-1.amazonaws.com/prod/authorization/search?q="+ company +"&token=" + apiToken)
print(response.json()[0]['company_name'])
print("Environmental Grade: " + str(response.json()[0]['environment_score']))
print("Social Grade: " + str(response.json()[0]['social_score']))
print("Goverance Grade: " + str(response.json()[0]['governance_score']))
print("Total Grade: " + str(response.json()[0]['total']))
print(response.json())