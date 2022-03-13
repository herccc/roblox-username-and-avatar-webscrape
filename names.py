import requests

id = str('your id here')

profile_request = requests.get('https://users.roblox.com/v1/users/'+id)
profile_request_json = profile_request.json()
profile_name = profile_request_json['name']

print(profile_name)



