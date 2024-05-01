# my_spartamarket_DRF
# 1. ERD
![스크린샷 2024-05-01 오후 10 03 38](https://github.com/JangSC9932/my_spartamarket_DRF/assets/60863619/06645e39-5b65-46a1-bd59-36094e94ea9d)
# 2. Accounts 기능구현
## 1) 회원가입
#### Endpoint: /api/accounts/
#### Method: POST
#### 요청필드
![스크린샷 2024-05-01 오후 10 04 28](https://github.com/JangSC9932/my_spartamarket_DRF/assets/60863619/d62f13bd-2556-4243-a6e6-0dc877ce846f)
#### 예시
![스크린샷 2024-05-01 오후 10 14 50](https://github.com/JangSC9932/my_spartamarket_DRF/assets/60863619/a7f28514-db0c-4acc-bb31-5481407c0303)
## 2) 로그인
#### Endpoint: /api/accounts/login/
#### Method: POST
#### 요청필드
![스크린샷 2024-05-01 오후 10 45 09](https://github.com/JangSC9932/my_spartamarket_DRF/assets/60863619/f6716ea7-e106-46b7-9a1c-1bbc950c1b9a)
#### 예시
![스크린샷 2024-05-01 오후 10 45 38](https://github.com/JangSC9932/my_spartamarket_DRF/assets/60863619/0c13ee45-bdc5-44cf-84b4-589526218ad9)
## 3) 프로필 조회
#### Endpoint: /api/accounts/<str:username>
#### Method: GET
#### 조건 : 로그인 필요
#### 예시
![스크린샷 2024-05-01 오후 10 47 19](https://github.com/JangSC9932/my_spartamarket_DRF/assets/60863619/7261dde6-a013-464b-9e4c-ba14f408cffe)
![스크린샷 2024-05-01 오후 10 47 29](https://github.com/JangSC9932/my_spartamarket_DRF/assets/60863619/853b60d0-e97b-4a41-bf05-43f208f4d450)
# 3. Products 기능구현
## 1) 상품 등록
#### Endpoint: /api/products/
#### Method: POST
#### 조건 : 로그인 필요
#### 요청필드
![스크린샷 2024-05-01 오후 10 49 46](https://github.com/JangSC9932/my_spartamarket_DRF/assets/60863619/0cb82806-0e02-4f83-886b-c6377ba5f043)
#### 예시
![스크린샷 2024-05-01 오후 10 50 02](https://github.com/JangSC9932/my_spartamarket_DRF/assets/60863619/d5fa6d85-f4ce-4e36-8e3b-d2aa8a965d48)
## 2) 상품 목록 조회
#### Endpoint: /api/products/
#### Method: GET
#### 예시
![스크린샷 2024-05-01 오후 10 51 45](https://github.com/JangSC9932/my_spartamarket_DRF/assets/60863619/a91a9f96-1339-4f25-8339-41eb8c8f6ccc)
## 3) 상품 수정
#### Endpoint: /api/products/<int:product_id>
#### Method: PUT
#### 조건: 로그인 필요, 작성자 정보와 로그인 정보 일치
#### 요청필드
![스크린샷 2024-05-01 오후 10 55 47](https://github.com/JangSC9932/my_spartamarket_DRF/assets/60863619/5eed4d11-ca72-4a26-b2dd-4e26d7e0f7c0)
#### 예시) 작성자 정보와 로그인 정보 불일치
![스크린샷 2024-05-01 오후 10 56 08](https://github.com/JangSC9932/my_spartamarket_DRF/assets/60863619/11c3c185-b86b-4c3e-adc0-4c8a4a5f312c)
#### 예시) 작성자 정보와 로그인 정보 일치
![스크린샷 2024-05-01 오후 10 57 24](https://github.com/JangSC9932/my_spartamarket_DRF/assets/60863619/9dd624aa-d460-4362-aeea-1e954ae96fa7)
## 4) 상품 삭제
#### Endpoint: /api/products/<int:product_id>
#### Method: DELETE
#### 조건: 로그인 필요, 작성자 정보와 로그인 정보 일치
#### 예시) 작성자 정보와 로그인 정보 불일치
![스크린샷 2024-05-01 오후 11 01 11](https://github.com/JangSC9932/my_spartamarket_DRF/assets/60863619/9bd8e37a-5c8b-4a2f-ac0e-94103fa41b4c)
#### 예시) 작성자 정보와 로그인 정보 일치
![스크린샷 2024-05-01 오후 11 01 33](https://github.com/JangSC9932/my_spartamarket_DRF/assets/60863619/775b8c38-26b4-45cd-b9e6-634e5a9c2853)

