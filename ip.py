import urllib3

http = urllib3.PoolManager(10)

url = "https://api.ipify.org/"
print("h")
response = http.connection_from_url( url)
print(dir(response))
print(response.request_encode_body())