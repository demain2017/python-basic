import json

str = """
[{
    "name": "Bob",
    "gender": "male",
    "birthday": "1992-10-18"
}, {
    "name": "Selina",
    "gender": "female",
    "birthday": "1995-10-18"
}]
"""

#print(type(str))
data = json.loads(str) #调用loads()方法将字符串转换为JSON对象----调用dumps()方法将JSON对象转化为字符串
#print(data)
#print(type(data))
print(data[0]['name'])
print(data[0].get('name'))
