## IIEII - 유화 제작 프로젝트

# **프로젝트 개요**
- 업로드한 사진을 다양한 스타일의 유화로 변환해주는 웹 서비스  


## 목표
- 장고 drf , 유화 제작 인공지능 기술을 이용하여 사용자가 이미지를 넣으면 유화 스타일이 적용된 이미지로 변환되어 출력되는 서비스 제작
- 프로젝트 기한(2022.11.22 ~ 2022.11.28)내에 프로젝트 완성을 목표


## 개발기간
2022년 11월 22일 ~ 2022년 11월 28일


## 팀구성
팀장 [김병문](https://github.com/kbm1933)
팀원 [김동익](https://github.com/DongIkkk), [오형석](https://github.com/auberr), [이혜원](https://github.com/wonprogrammer), [최정윤](https://github.com/uniqquej)


## 주요 구현 기능
- 장고
    - 회원 기능
    - 회원 가입 (SimpleJWT를 이용)
    - 로그인 기능 (SimpleJWT를 이용)
    - 유저 프로필 기능
        - 프로필 별 게시글 보여주기
        - 프로필 이미지 수정
        - 팔로우 기능
    - 게시판 기능
        - 게시물 CRUD
        - 게시물의 댓글 CRUD
        - 게시물의 좋아요 기능
    - 딥러닝_유화 변환 기능
        - NST를 이용해 사용자가 업로드한 이미지를 유화로 변경해 저장


## Front-end repo
- [깃헙으로 이동](https://github.com/kbm1933/B2_IIEII_OPP_Front)

## Project Intro Notion
- [노션으로 이동](https://www.notion.so/221122-a90ad7eaa1194801a9631a411a081d2c)

## Wireframe
- [피그마로 이동](https://enormous-ragdoll-497.notion.site/221122-a90ad7eaa1194801a9631a411a081d2c)
![figma](https://user-images.githubusercontent.com/6766202/204168797-bed8aaee-3ab4-4e99-9bda-a86542992703.png)


## API Doc
- 유화 변환
![api1](https://user-images.githubusercontent.com/6766202/204169348-2ef4fad3-3cd3-421b-a799-8b131c88f841.png)
![api2](https://user-images.githubusercontent.com/6766202/204169351-a061f901-3635-49e0-a81b-cd309aeff7a8.png)

- 유저
![api3](https://user-images.githubusercontent.com/6766202/204169357-ff2910b2-74c4-43cb-ab46-12ce45c2bee1.png)


## DB
- ERD
![ERD](https://user-images.githubusercontent.com/6766202/204168979-8ec2ee8b-ab9b-4e5e-8a81-afc113c5ebc3.jpg)


## 트러블 슈팅
