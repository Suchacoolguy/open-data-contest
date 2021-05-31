import requests, xmltodict, json

# put your key issued from data.go.kr
key = "a6%2FEcaYI3Q3If3xB3y7ocusVv02c26cqlWtZe8pWCNW7aME6i0bJUTMWZTk1VoZ1VXOxkYw%2F2Y5KuoPILNA%2FDw%3D%3D"

# designate the dates you want to get data on
startDate = 20200520
endDate = 20200522

# make the xml file to json file
url = "http://openapi.data.go.kr/openapi/service/rest/Covid19/getCovid19SidoInfStateJson?serviceKey={}&pageNo=1&numOfRows=10&startCreateDt={}&endCreateDt={}".format(key, startDate, endDate)
content = requests.get(url).content
dict = xmltodict.parse(content)
jsonString = json.dumps(dict, ensure_ascii=False)
jsonObj = json.loads(jsonString)

# the data we want to see is under "item"
jsonObj2 = jsonObj["response"]["body"]["items"]["item"]

# test running. this code gets data of Ulsan city
for item in jsonObj2:
    if "Ulsan" in item["gubunEn"]:
        print(item)