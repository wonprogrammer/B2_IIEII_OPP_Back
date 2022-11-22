## IIEII - 유화 제작 프로젝트

# **프로젝트 개요**
- 업로드한 사진을 다양한 스타일의 유화로 변환해주는 웹 서비스  

## 목표
- 장고 drf , 유화 제작 인공지능 기술을 이용하여 사용자가 이미지를 넣으면 유화 스타일이 적용된 이미지로 변환되어 출력되는 서비스 제작
- 프로젝트 기한(2022.11.22 ~ 2022.11.28)내에 프로젝트 완성을 목표

## Wireframe
- https://enormous-ragdoll-497.notion.site/221122-a90ad7eaa1194801a9631a411a081d2c
## 트러블 슈팅

## API 명세서
- 유화 변환
|기능|Method|URL|request|response|
|----|----|----|----|----|
|공통 headers|||Headers:{Authorization: Bearer access_token }||
|1. 메인화면 전체 게시글 조회|GET|/||[{’article’:article}]|
|2. 유화로 바꾸기 - 1.이미지 업로드|GET|/articles/imgtoop/||{’user’:id’img’:img_id}|
|2. 유화로 바꾸기 - 1. 이미지 업로드|POST|/articles/imgtoop/|Body:
{’user’:user,
’input_img’:input_img,
’output_img’:output_img}| {
’user’:id,
’img’:img_id,
}|
|3. 유화로 바꾸기 - 2. 게시물 등록|GET|/articles/imgtoop/{img_id}/||{”img”:output_img}|
|3. 유화로 바꾸기 - 2. 게시물 등록|POST|/articles/imgtoop/{img_id}/|Body:
{’user’:user, ‘img’:output_img,’title’:title, ‘content’:content}|{
’img’:output_img,
’img_content’:content,
}|
|4. 이미지 게시글 디테일|GET|/articles/{post_id}/detail/||{’user’:id,’img’:img_id}|
|4. 이미지 게시글 디테일|PUT|/articles/{post_id}/detail/|Body:
{’title’:title, ‘content’:content}|{
’title’:title,
’content:content
}|
|4. 이미지 게시글 디테일|DELETE|/articles/{post_id}/detail/||“Delete”|
|5. 이미지 게시글 댓글|POST|/articles/{post_id}/detail/|Body:
{’comment’:comment}|{
’user’:id,
’comment’:comment
}|
|5. 이미지 게시글 댓글|PUT|/articles/{post_id}/comment/{comment_id}|Body:
{’comment’:comment}|{
’user’:id,
’comment’:comment
}|
|5. 이미지 게시글 댓글|DELETE|/articles/{post_id}/comment/{comment_id}||“Delete”|
|6. 이미지 게시글 좋아요|POST|/articles/{post_id}/likes||{
’user’:id,
’likes”:like
}|

- User

|기능|Method|URL|request|response|
|----|----|----|----|----|
|회원가입|POST|/users/signup|Body :{”username”:”username”,”password”:”password”}|{”message”:”가입완료!”}|
|로그인 jwt토큰생성|POST|/users/api/token|Body :{”username”:”username”,”password”:”password”}|{”message”:”가입완료!”}|
|로그아웃|POST|/users/logout|||
|마이 프로필|GET|/users/{user_id}/profile|Headers:{
Authorization: Bearer access_token }|{ "profile_img": profile_img_url}|
|마이 프로필 이미지 수정|PUT|/users/{user_id}/profile|Body:
{"profile_img": profile_img_url}|{”message”:”수정완료!”}|


## ERD
![IIEII_erd](https://user-images.githubusercontent.com/55372753/203258279-6988333d-0b62-4bda-a5f2-974c5cb54d3a.png)
