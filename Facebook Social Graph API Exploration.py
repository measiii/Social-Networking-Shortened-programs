# pip install requests

import requests

access_token = "EAAR0ZAhPwkuEBRDFIvojUZCZBAwsOtUGIfNTZBK5DCZAShuczZAnTqbMmSdu114x4kAkrqoH4e90snkctj7jP7iRk7mMlTk0kSY8fdIr9YZAupvSDZBCW23YMR3mRkCNsZADZBoKNquDk5kO4sNaRbfVZCV3NwG3YjiYQeQGB4FQW9Hb6ZC533zjpc8ZCozO2exEdLZBr6"

url = "https://graph.facebook.com/me?access_token=" + access_token

response = requests.get(url)
data = response.json()

print("Name:", data["name"])
print("ID:", data["id"])
