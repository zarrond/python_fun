import requests
get_response = requests.get(url='http://google.com')
post_data = {'username':'joeb', 'password':'foobar'}
# POST some form-encoded data:
post_response = requests.post(url='http://httpbin.org/post', data=post_data)