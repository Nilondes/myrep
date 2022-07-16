import re
import requests

template2 = r'<a.*?href=.*?:\/\/?(\w[\w.-]*)'

line = input().rstrip()
url = requests.get(line)
file = url.text
urls = re.findall(template2, file) # find all URLs in file
urlsfinal = list(set(urls))
for answer in sorted(urlsfinal):
    print(answer)









