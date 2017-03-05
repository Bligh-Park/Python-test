import pandas as pd

#url_tmpl = 'http://companyinfo.stock.naver.com/v1/company/ajax/cF1001.aspx?cmp_cd=%s&fin_typ=%s&freq_typ=%s'
url_tmpl = 'http://companyinfo.stock.naver.com/company/c1010001.aspx?cmp_cd==%s&fin_typ=%s&freq_typ=%s'
url = url_tmpl % ('005930', '4', 'Y') # 삼성전자, 4(IFRS 연결), Y:년 단위

#'http://companyinfo.stock.naver.com/company/c1010001.aspx?cmp_cd=005930&fin_typ=4&freq_typ=Y'

dfs = pd.read_html(url)

'''
df = dfs[0]
df = df.set_index('주요재무정보')
df.head()
df.head(10) # 10개 항목만 표시(실제 32개 항목)
'''