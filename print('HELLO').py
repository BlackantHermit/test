def request_view(response):  #显示需要爬取的页面
      import webbrowser  #调用默认浏览器
      request_url = response.url  
      base_url = '<head><base herf="%s">'%(request_url)  #完整显示页面
      base_url = base_url.encode()
      content  = response.content.replace(b"<head>",base_url)
      tem_html = open('tmp.html','wb')
      tem_html.write(content)
      tem_html.close()
      webbrowser.open_new_tab("tmp.html")

import requests

response = requests.get("https://www.souhu.com/")
request_view(response)
