import requests

request_bbc_status_code = requests.get("https://www.bbc.co.uk/iplayer/live/bbcnews")

# Check the outcome of our api call

if request_bbc_status_code.status_code == 200:
    print("Successful")

else:
    print("Unsuccessful")




# check the header

# print(request_bbc_status_code.headers)

# check the content available

# print(request_bbc_status_code.content)