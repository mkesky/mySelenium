import urllib.request

response = urllib.request.urlopen("http://image.so.com/v?ie=utf-8&src=hao_360so&q=%E7%8E%8B%E5%8A%9B%E5%AE%8F&correct=%E7%8E%8B%E5%8A%9B%E5%AE%8F&cmsid=8af9b6233bc334e862264489b1d13808&cmran=0&cmras=0&cn=0&gn=0&kn=50#id=0dd64fecdfdf07290fba6816906c5b03&itemindex=0&currsn=0&jdx=10&gsrc=1&fsn=110&multiple=0&dataindex=10&prevsn=0")
wang = response.read()
with open("wang.jpg",'wb') as f:
    f.write(wang)