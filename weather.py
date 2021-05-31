import json, urllib, requests

# the service key i got from data.go.kr
key = "a6%2FEcaYI3Q3If3xB3y7ocusVv02c26cqlWtZe8pWCNW7aME6i0bJUTMWZTk1VoZ1VXOxkYw%2F2Y5KuoPILNA%2FDw%3D%3D"

# you can change the input values in url, e.g. you may want to change startDt/endDt values to see the data of other dates
# visit https://www.data.go.kr/en/tcs/dss/selectApiDataDetailView.do?publicDataPk=15059093 for description of input values.
url = "http://apis.data.go.kr/1360000/AsosDalyInfoService/getWthrDataList?serviceKey={}&numOfRows=10&pageNo=1&dataType=JSON&dataCd=ASOS&dateCd=DAY&startDt=20210301&endDt=20210301&stnIds=152".format(key)
data = urllib.request.urlopen(url).read()
output = json.loads(data)

print(output)
