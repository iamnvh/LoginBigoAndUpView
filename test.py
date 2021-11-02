import requests
r = requests.get('https://thuesim.xyz/api/?show=balance&token=980-857a5f5ed51f7f803f72dd2b82ec57c9').text
print(r)
""" 
print(r['Status_code']) 
""" 
