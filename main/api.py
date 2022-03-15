import requests

r = requests.post("https://api.pushover.net/1/messages.json",
                data={
                    'token': 'awi52pkzbbgwjxfdp9xwntwsdxsfh7',
                    "user":"urvxzw4dvcz1ke62pumnumnmr3cdrz",
                    "message":"hello",
                    "priority":"2",
                    "expire":"300",
                    "retry":"30"
                
                },)

print(r.json())
