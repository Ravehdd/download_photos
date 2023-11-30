import requests
import os

token = "033a6c74033a6c74033a6c7480002c19bf0033a033a6c74665f88896f6349f7152a58a5"
version = 5.92
domain = "selti_seltin_sweety"#домен группы
# album_id = "299673715"
owner_id = "-214894860"# "-" + id группы
secret_token = "y6xgFprm56cKG9ZChaa9"

response = requests.get("https://api.vk.com/method/photos.getAlbums",
                        params={
                            "access_token": token,
                            "v": version,
                            "owner_id": owner_id,
                            "count": 2
                        })

data = response.json()["response"]["items"]
album_ids = []
for album_data in data:
    album_ids.append(album_data["id"])

for album_id in album_ids:
    response = requests.get("https://api.vk.com/method/photos.get",
                            params={
                                "access_token": token,
                                "v": version,
                                "owner_id": owner_id,
                                "album_id": album_id
                            })

    data = response.json()["response"]
    for photo in data['items']:
        url = photo['sizes'][5]['url']
        photo_id = photo['id']
        photo_name = f"{photo_id}.jpg"

        folder_path = f"photos/{album_id}" # создастся папка photos в которой будут создаваться папки с названиями альбомов
        os.makedirs(folder_path, exist_ok=True)

        r = requests.get(url, stream=True)
        with open(f"{folder_path}/{photo_name}", 'wb') as file:
            for chunk in r.iter_content(chunk_size=128):
                file.write(chunk)
