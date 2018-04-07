import re

"""
content = 'Hello 1234567 World_This is a Regex Demo'
print(len(content))
result = re.match('^Hello\s(\d+)\s\w{10}',content)
print(result)
print(result.group())
print(result.group(1))
print(result.span())
"""

# ^$强匹配
"""

content = 'Hello 123 4567 World_This is a Regex Demo'
result = re.match('^Hello.*Demo$', content)
print(result)
print(result.group())
print(result.span())
"""

#贪婪与非贪婪
# .*匹配尽可能多的字符
# .*?匹配尽可能少的字符
"""
content = 'Hello 1234567 World_This is a Regex Demo'
#result = re.match('^He.*(\d+).*Demo$', content)
result = re.match('^He.*?(\d+).*Demo$', content)
print(result)
print(result.group(1))
"""

#compile()编译成正则表达式对象
content1 = '1111-11-11 11:11'
content2 = '2222-22-22 22:22'
content3=  '3333-33-33 33:33'
pattern = re.compile('\d{2}:\d{2}')

result1 = pattern.findall(content1)
result2 = pattern.findall(content2)
result3 = pattern.findall(content3)
print(result1,result2,result3)
 
