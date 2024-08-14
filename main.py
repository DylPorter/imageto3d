import requests, api, time

# Upload image to the service
payload = {
    "image_url": "https://i.imgur.com/XrH1Lru.jpeg",
}

headers = {
    "Authorization": f"Bearer {api.api_key}",
}

response = requests.post(
    "https://api.meshy.ai/v1/image-to-3d", # Endpoint
    headers=headers,
    json=payload,
)

response.raise_for_status()

data = response.json()
task_id = data["result"]

print(f"Model ID: {task_id}")

# Wait for 3D model to finish generating

model = {"progress": 0}

while model["progress"] < 100:
    response = requests.get(
        f"https://api.meshy.ai/v1/image-to-3d/{task_id}",
        headers=headers,
    )
    response.raise_for_status()
    model = response.json()
    print(f'Progress: {model["progress"]}')
    time.sleep(1)

print(model)
