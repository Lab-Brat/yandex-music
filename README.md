## yandex-music
A simple tool to get the list of liked tracks from Yandex Music account. It uses ```yandex-music``` unofficial Python wrapper, since Yandex never bothered to make their API public.  

### How-To
To run the tool, first install dependencies and set up virtual environment:
```
python -m venv venv
source venv/bin/activate
python -m pip install yandex-music
```
Then obtain an authentication token by following Yandex Musics's OAuth [link](https://oauth.yandex.ru/authorize?response_type=token&client_id=23cabbbdc6cd418abb4b39c32c41195d) and authenticating there using a Yandex account, detailed steps are [here](https://github.com/MarshalX/yandex-music-api/discussions/513). After it's done, create a file named ```token``` and paste the token there without any whitespace characters.  

Finally, to run the app:
```
python main.py
```

### Useful Links
Official Documentation: https://yandex-music.readthedocs.io/en/main/index.html  
Official Github Repo: https://github.com/MarshalX/yandex-music-api  
More on OAuth Tokens: https://yandex.ru/dev/direct/doc/start/token.html  
Yandex Account Authentication Settings: https://passport.yandex.ru/profile
