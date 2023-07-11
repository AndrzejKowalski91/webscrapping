url = 'https://www.pepper.pl/'
response = requests.get(url)
if response.status_code == 200:
    print('request OK')
else:
    print('request nie ok')
content = response.text
