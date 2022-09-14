from urllib import request


url = request.urlopen("https://www.google.com")
html = url.read()
status = url.getcode()
webURL = url.geturl()

print("The URL is ",webURL)
print("Status code : ",status)
print("Headers : ",url.headers)