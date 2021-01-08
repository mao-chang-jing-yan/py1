import re

"""
<a class="px14" href="/views/specific/2929/bookDetail.jsp?dxNumber=000004302625&amp;d=A3EB4E78C6F9296602ABEB73921A0082&amp;fenlei=1817040302" target="_blank"><img alt="封面" border="1" height="110" src="https://unicover.duxiu.com/coverNew/CoverNew.dll?iid=6A6A686D6E6E686972715F9DAEB1A2AE5F6A3538333035333939" width="75"/></a> 
"""
s = "href = '/views/specific/2929/bookDetail.jsp?dxNumber=000004302625&amp;d=A3EB4E78C6F9296602ABEB73921A0082&amp;fenlei=1817040302 " \
    "' src = 'https://unicover.duxiu.com/coverNew/CoverNew.dll?iid=6A6A686D6E6E686972715F9DAEB1A2AE5F6A3538333035333939"
pattern = re.compile(r'href=\'[A-Za-z0-9]\'')  # 查找数字
result1 = pattern.findall('runoob 123 google 456')
# result2 = pattern.findall('run88oob123google456', 0, 10)
url = re.compile(r'<h2.*?><a\b[^>]+\bhref=\\"([^"]*)"[^>]*>.+?</a></h2>').findall(s)

result2 = pattern.findall(s)
# print(result1)
# print(result2)
print(url)