import requests


# responce = requests.post('http://localhost:8000/advertisement', 
#                          json={"title": "ad_1",
#                                "descr": "Ad descr 1",
#                                "price": 1337,
#                                "author": "Legend"
#                                })
# print(f"Responce: {responce.text}")
# print(f"HTTP code: {responce.status_code}")

# responce = requests.post('http://localhost:8000/advertisement', 
#                          json={"title": "ad_2",
#                                "descr": "Ad descr 2",
#                                "price": 7331,
#                                "author": "Legend"
#                                })
# print(f"Responce: {responce.text}")
# print(f"HTTP code: {responce.status_code}")

# responce = requests.post('http://localhost:8000/advertisement', 
#                          json={"title": "3rd AD",
#                                "descr": "Ad descr 3",
#                                "price": 12345,
#                                "author": "Clown"
#                                })
# print(f"Responce: {responce.text}")
# print(f"HTTP code: {responce.status_code}")


# responce = requests.patch('http://localhost:8000/advertisement/2', 
#                          json={"title": "FIXED ADVERTISEMENT",
#                                "descr": "Ad descr FIXED",
#                                "price": 98765
#                                })
# print(f"Responce: {responce.text}")
# print(f"HTTP code: {responce.status_code}")

# responce = requests.get('http://localhost:8000/advertisement/?author=Clown&description=four')
# print(f"Responce: {responce.text}")
# print(f"HTTP code: {responce.status_code}")

# responce = requests.get('http://localhost:8000/advertisement/5/')
# print(f"Responce: {responce.text}")
# print(f"HTTP code: {responce.status_code}")

# responce = requests.delete('http://localhost:8000/advertisement/5/')
# print(f"Responce: {responce.text}")
# print(f"HTTP code: {responce.status_code}")