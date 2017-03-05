import re
import requests
from bs4 import BeautifulSoup

currentPage=1
val=()

while currentPage:

    url = 'http://www.assembly.go.kr/assm/memact/congressman/memCond/memCondListAjax.do?currentPage='+str(currentPage)+'&rowPerPage=6'
    html = requests.get(url)
    plaintext=html.text
    soup = BeautifulSoup(plaintext,"html.parser")

    for member_tag in soup.select('.memberna_list dl dt a'):
        name = member_tag.text
        link = member_tag['href']

    if val!=name:
       val=name
    else:
        break


    matched=re.search('\d+',link)
    if matched:
        member_id =matched.group(0)
    else:
        member_id=None


    print(name+member_id)
    currentPage += 1

