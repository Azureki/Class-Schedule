import requests
import http.cookiejar as cookielib
import http.cookiejar as cookielib


headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
postdata={"svpn_name": "2016201218", "svpn_password": "612610"}
loginurl='https://ssl.hrbeu.edu.cn/por/login_psw.csp'
heusession=requests.session()
heusession.cookies=cookielib.LWPCookieJar(filename=r'C:/Users/azuki/Desktop/cookie.txt')
response=heusession.post(loginurl,postdata,headers=headers,verify=False)



url_cas='https://ssl.hrbeu.edu.cn/web/1/https/1/cas.hrbeu.edu.cn/cas/login?service=http%3A%2F%2Fone.hrbeu.edu.cn%2Finfoplus%2Flogin%3FretUrl%3Dhttp%253A%252F%252Fone.hrbeu.edu.cn%252Finfoplus%252Foauth2%252Fauthorize%253Fresponse_type%253Dcode%2526scope%253Dprofile%252Bprofile_edit%252Bapp%252Btask%252Bprocess%252Bsubmit%252Bprocess_edit%252Btriple%252Bsys_enterprise%2526redirect_uri%253Dhttp%25253A%25252F%25252Fone.hrbeu.edu.cn%25252Ftaskcenter%25252Fwall%25252Fendpoint%25253FretUrl%25253Dhttp%2525253A%2525252F%2525252Fone.hrbeu.edu.cn%2525252Ftaskcenter%2525252Fworkflow%2525252Findex%2526client_id%253D1640e2e4-f213-11e3-815d-fa163e9215bb%2526x_redirected%253Dtrue'
postdata={'username':'2016201218','password':'612610'}
response=heusession.post(url_cas,postdata,headers=headers,verify=False)

url_kb='https://ssl.hrbeu.edu.cn/web/1/http/1/edusys.hrbeu.edu.cn/jsxsd/xskb/xskb_list.do'
response=heusession.post(url_kb,headers=headers,verify=False)

url_caslogin='https://cas.hrbeu.edu.cn/cas/login'
postdata={'username':'2016201218','password':'612610','captcha':''}
response=heusession.post(url_caslogin,postdata,headers=headers,verify=False)

