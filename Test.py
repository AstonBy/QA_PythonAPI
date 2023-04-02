import random
import requests
data = {"email": "shkorkin+dev060922@alarstudios.com", "password": "1234qwertY!"}
response1 = requests.post(
    "https://qa02.happify.com/api/public/auth/?client_id=gAAAAABjEKz0b2Mp8ng0LyWd2Bh6cNiOztr8EpLmBEQqdfKp_ENEl6MI37phWegTR5w9lPXn1ldNo3_0YOuH6bfbMJMbmuO5Fw==",
    json=data
    )
access_token = response1.json()["access_token"]
print(access_token)
response2 = requests.get(
    "https://dev-connect.happify.com/api/v1/users/me/",
    params={"access_token": access_token},
    )
ses = response2.cookies.get("ses")
response2 = requests.get(
    "https://dev-connect.happify.com/api/v1/users/dialog/ha/",
     cookies={"ses": ses}
    )
conversation_id = response2.json()["conversation_id"]
turn_number = 0
while True:
    turn_number += 1
    response = requests.post(
        "https://dev-connect.happify.com/api/v1/users/dialog/",
        json={
            "conversation_id": conversation_id,
            "turn_number": turn_number,
            "client_input": random.randint(1, 3),
        },
        cookies={"ses": ses},
    )
    print(response.text)
    if response.status_code != 200:
        break
response_result = requests.get(
    "https://dev-connect.happify.com/api/v1/home/", cookies={"ses": ses}
    )
print(response_result.text)