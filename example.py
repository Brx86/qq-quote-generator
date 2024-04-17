import requests

json_data = [
    {
        "user_id": 5435486,
        "user_nickname": "竹林里有冰",
        "message": "你好啊，我是你的小可爱",
    },
    {
        "user_id": 5435486,
        "user_nickname": "竹林里有冰",
        "image": ["https://api.vercel.zhullyb.top/api/randomtoppic.php"],
    },
    {
        "user_id": 5435486,
        "user_nickname": "竹林里有冰",
        "message": "你好啊，我是你的小可爱",
        "image": [
            "https://api.vercel.zhullyb.top/api/randomtoppic.php",
            "https://api.vercel.zhullyb.top/api/randomtoppic.php",
        ],
    },
    {
        "user_id": 5435486,
        "user_nickname": "竹林里有冰",
        "message": "你好啊，我是你的小可爱啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊啊",
        "image": [
            "https://api.vercel.zhullyb.top/api/randomtoppic.php",
            "https://api.vercel.zhullyb.top/api/randomtoppic.php",
            "https://api.vercel.zhullyb.top/api/randomtoppic.php",
        ],
        "reply": {
            "user_nickname": "竹林里没冰",
            "message": "你好啊，我不是你的小可爱",
            "image": "https://api.vercel.zhullyb.top/api/randomtoppic.php",
        },
    },
]

r = requests.post("https://api.aya1.de:22001/jpeg", json=json_data)
with open("test.jpg", "wb") as f:
    f.write(r.content)
