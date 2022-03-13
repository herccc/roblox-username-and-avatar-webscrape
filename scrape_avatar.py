import requests

id = str('your id here')

payload = {'userId':id, 'width':420, 'height':420, 'format':"png" }
r = requests.get('https://www.roblox.com/bust-thumbnail/image?', params = payload)
avatar = r.content
