# pip install requests

import requests

# Paste your access token here
access_token = "EAAR0ZAhPwkuEBRDFEDjb71w1L7XztRjlBZAgNVgOzCtuVTuZC1lB2B983NukCydVWYIruyXQYOZCGZAzhPdybxKhhCaRMwCtd2065sZCdt9ZAZAlHt9v0J8Wnazd28Xie4D4z1jG8m4TCGLZChevE9FzUeRQhKUQugiNA4Ipk3ppJyFrvD1Dj2TroW9GpUwZAt0V0STuspZCZAVjlkyfhvpNPTezGQLKmpeiO4nwmBj1Scs1nUIf4C8ZBj89DFl5AzQheoX4Ox0TZCKXQU1JzOmlkcDzzEMTyPZCOxUD5BlCBHaltRMjTGeX25qgjBuSdhLggjJ8axmJQVeikHc"

# Get basic profile data
url = "https://graph.facebook.com/me?access_token=" + access_token

response = requests.get(url)
data = response.json()

# Print output
print("Name:", data["name"])
print("ID:", data["id"])
