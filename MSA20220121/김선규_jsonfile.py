#06파일의 with를 전부 try~exception으로 변경
import json

try:
    jsonFile = open("datalab\\mydata.json", "rb")
    tempData = json.load(jsonFile)
    reusltData1 = tempData["name"]
    reusltData2 = tempData["age"]
    reusltData3 = tempData["address"]
    reusltData4 = tempData["email"]
    reusltData5 = tempData["empcheck"]
except Exception as error:
    print("오류 : " + error)
else:
    jsonFile.close()


jsonData1 = {
        "empid": 12345678,
        "name" : "홍길동",
        "info" : [
            {"date1": "2022-01-21", "home": "서울시"},
            {"dep": "개발", "email": "aaa@aaa.co.kr"}
        ]
    }

try:
    writeFile_1 = open("datalab\\mydata2.json", "w")
    json.dump(jsonData1, writeFile_1)
except Exception as error:
    print("오류 : " + error)
else:
    writeFile_1.close()

try:
    writeFile_2 = open("datalab\\mydata3.json", "w", encoding="utf-8")
    json.dump(jsonData1, writeFile_2, ensure_ascii=False)
except Exception as error:
    print("오류 : " + error)
else:
    writeFile_2.close()

try:
    writeFile_3 = open("datalab\\mydata4.json", "w")
    json.dump(jsonData1, writeFile_3, ensure_ascii=False, indent=4)
except Exception as error:
    print("오류 : " + error)
else:
    writeFile_3.close

try:
    writeFile_4 = open("datalab\\mydata5.json", "w", encoding="utf-8")
    json.dump(jsonData1, writeFile_4, ensure_ascii=False, indent=4)
except Exception as error:
    print("오류 : " + error)
else:
    writeFile_4.close

temp = 0
