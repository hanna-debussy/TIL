if request.method == 'GET':
    base_URL = "https://api.themoviedb.org/3"
params = {
    "api_key": "17d70c389617d161e982197e5f7b8bd9",
    "region": "KR",
    "language": "ko",
}

# 입력한 영화의 정보 가져오기
path = "/search/movie"
params["query"] = request
response = urllib.request.Request(base_URL + path, params=params)
data = response.json()
results = data.get("results")

for n in range(0, len(results)):
    # 영화의 id 가져오기
    movie_id = results[n]["id"]
    if not (movie_id):
        return None

    # recommendation 요청
    path = f"/movie/{movie_id}/recommendations"
    response2 = urllib.request.Request(base_URL + path, params=params)
    data2 = response2.json()
    results2 = data2.get("results")

    # 추천영화 title 가져오기
    recom_title = []
    for m in range(0, len(results2)):
        recom_title.append(results2[m]["title"])

sth_title = random.choice(recom_title)
context = {
    "title": sth_title,
}