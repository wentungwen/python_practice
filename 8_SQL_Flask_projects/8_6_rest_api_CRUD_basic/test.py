import requests

base_url = "http://localhost:5000"

# PUT request to create a video
put_url = f"{base_url}/video/1"
put_data = {
    "name": "My Video",
    "views": 100,
    "likes": 10
}
put_response = requests.put(put_url, json=put_data)

if put_response.status_code == 201:  # Check if the request was successful
    print("Video created successfully")
else:
    print("Failed to create video")

# GET request to retrieve the video
get_url = f"{base_url}/video/1"
get_response = requests.get(get_url)

if get_response.status_code == 200:  # Check if the request was successful
    video_data = get_response.json()
    print(video_data)
else:
    print("Failed to retrieve video")
