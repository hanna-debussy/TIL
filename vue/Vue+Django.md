# Vue+Django

## 교차 출처

https://developer.mozilla.org/ko/docs/Web/HTTP/CORS

```bash
$ pip install django-cors-headers
```

settings.py

```python
INSTALLED_APPS = [
    "corsheaders",
]
MIDDLEWARE = [
    # CommonMiddleware보다 반드시 위에 위치해야 한다
    # 보통은 가장 위에 둠
    "corsheaders.middleware.CorsMiddleware",
]

# 추가
CORS_ALLOWED_ORIGINS = [
    "http://localhost:8080",
]

# 만약 모든 origin에 대해 교차 출처를 허용한다면
CORS_ALLOW_ALL_ORIGINS = True
```



## DRF Authentication

### Basic Token

로그인 한 사람에게 token을 부여하여 서버는 token table에, 클라이언트는 브라우저에 token을 저장해서 요청을 할 때마다 요청 header에 토큰을 함께 보내면 table에서 확인하고 응답을 해주는 형식



### JWT

JSON Web Token. JWT가 검증에 필요한 정보를 모두 갖고 있기 때문에 table이 따로 필요 없고 JWT 자체로 검증이 가능하다. 

```bash
$ pip install django-allauth
$ pip install dj-rest-auth
```

```python
# settings.py

INSTALLED_APPS = [
    'rest_framework',
    
     # token 기반 auth
    'rest_framework.authtoken',
    
    # DRF auth 담당
    'dj_rest_auth',  # signup 제외 auth 관련 담당
    'dj_rest_auth.registration',  # signup 담당

	# 기본적으로 깔린 것 중에 allauth 사용을 위해 필요한 게
    'django.contrib.sites',
]


# 그리고 밑에 추가할 것

# DRF 인증 관련 설정
REST_FRAMEWORK = {
    # 기본 인증방식 설정
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework.authentication.TokenAuthentication',
    ],
    
    # 기본 권한 설정
    'DEFAULT_PERMISSION_CLASSES': [
        # 모두에게 허용
        # 'rest_framework.permissions.AllowAny', 

        # 인증된 사용자만 모든일이 가능 / 비인증 사용자는 모두 401 Unauthorized
        'rest_framework.permissions.IsAuthenticated'
    ]
}

```

```python
# urls.py

urlpatterns = [
    ...
    # 포워딩을 dj_rest_auth로 보내줘야 한다
    path('accounts/', include('dj_rest_auth.urls')),
    path('accounts/signup/', include('dj_rest_auth.registration.urls')),
]
```



### Oauth

