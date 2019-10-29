# :dog: Django : rest

[사전_준비](https://github.com/wally-wally/TIL/blob/master/04_django/%5BSSAFY%5Ddjango_%234.md#15-10%EC%9B%9428%EC%9D%BC15%EC%9D%BC%EC%B0%A8---rest-api)



#### :grey_exclamation: 역참조

###### models.py

```python
class Music(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    title = models.TextField()
```

- 첫번째 방법 : CASCADE 뒤, ` related_name='musics'` 추가

###### serializers.py

```python
class ArtistDetailSerializer(ArtistSerializer):
    # 자식모델_set 으로 역참조 가능 => 단일객체x
    musics = MusicSerializer(source='music_set', many=True)
    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ('musics',)
```

- 두번째 방법 : `musics = MusicSerializer(source='music_set', many=True)` 구문 추가

- 두번째 방법을 사용하여 역참조를 해보자.





- [POSTMAN 다운로드](https://www.getpostman.com/downloads/)

![image](https://user-images.githubusercontent.com/52684457/67653874-b773c280-f98e-11e9-8755-c99fcbe25464.png)

- http type(POST) 설정 후, 주소 입력
- Body **=>** form-data 에서 값을 입력후 send 하면 값이 입력된다.

![image](https://user-images.githubusercontent.com/52684457/67653908-e12ce980-f98e-11e9-84d4-66bbbd536558.png)

- Params에서 value 값을 지정해놓고 사용할 수도 있다.

- 주소를 더 만들 필요없이 http 속성만 바꿔줌으로서 수정, 삭제 등을 실행하는 것이 rest



###### `comments_update_and_delete`

![image](https://user-images.githubusercontent.com/52684457/67654217-269de680-f990-11e9-880f-acd43197c5f5.png)

- ###### DELETE



![image](https://user-images.githubusercontent.com/52684457/67654338-8eecc800-f990-11e9-93ca-fc6d994e8340.png)![image](https://user-images.githubusercontent.com/52684457/67654356-a330c500-f990-11e9-9114-2e0ec89aedca.png)

- ###### UPDATE



#### :raised_hand_with_fingers_splayed: count 값

```python
class ArtistDetailSerializer(ArtistSerializer):
    musics = MusicSerializer(source='music_set', many=True)
    musics_count = serializers.IntegerField(source='music_set.count')
    class Meta(ArtistSerializer.Meta):
        fields = ArtistSerializer.Meta.fields + ('musics', 'musics_count')
```

-  `musics_count = serializers.IntegerField(source='music_set.count')` 구문 추가

![image](https://user-images.githubusercontent.com/52684457/67654574-526d9c00-f991-11e9-9166-047457f27d76.png)























