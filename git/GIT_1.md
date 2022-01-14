# GIT 101

## 0. 명령어 이모저모

```bash
# ..는 상위 폴더 상징, .는 현재 위치를 상징
# * 는 전체, 모든

# mkdir make directory
$ mkdir new_project

# cd change directory
$ cd new_project
$ cd ..

# pwd present working dir 지금 주소가 어딘지
$ pwd

# touch 파일 생성
$ touch memo.txt
$ touch a.txt b.docx c.md d.md

# ls 폴더 내 파일 리스트
$ ls # except 숨김 파일
$ ls -a # 전체 파일 including 숨김 파일
$ ls -t # 생성 시간대로 정렬
$ ls -at # a & t

# rm 파일 삭제
$ rm memo.txt
$ rm *.md

# rm -r 폴더 삭제 (하위 파일들 포함)
$ rm -r folder1

# 모니터링 명령어
$ git status # 현재 상황
$ git log # commit log

# 파일 이름 바꾸기
$ mv namebefore nameafter

# 파일 위치 바꾸기
$ mv filename foldername/

# 사본 만들기
$ cp originfilename copiedfilename
```



## 1. START

### 1) local computer 에서 repo 만들기

```bash
# 처음 bash에 들어가면 `~`, 즉 home 폴더로 지정되어있다

# home에 pjt 폴더 생성
$ mkdir pjt

# 해당 폴더로 이동
$ cd pjt

# 현재 위치한 이 폴더를 리포(repo(sitory))로 지정
$ git init
# 그러면 해당 폴더 뒤에 (master)가 뜬다

# 지금 폴더의 리포 해제
$ rm -rf .git/

# 기본적인 거 만들어보자
$ touch README.md .gitignore

# git 쓸 때 내 계정 서명 등록
$ git config --global user.name
$ git config --global user.email
$ cat ~/.gitconfig # 서명 확인

# 파일을 스테이지에 올리기 (-> 스테이징된 변경사항에 들어감)
$ git add README.md
$ git add . # 현재 위치 내 모든 파일 스테이징

# commit (스테이징된 파일들 스샷)
$ git commit -m 'commit 올릴 때 이름'
# cf) 스테이징된 것들이 전의 commit과 변경된 게 없으면 새로 commit되지 않는다
```

### 2) github와 연결하기

```bash
# github에 원격 리포를 생성한 후
$ git remote add name <URL>
# name에는 보통 origin을 적는다 (이하 origin은 name이 바뀜에 따라 바꿔 써야 함)
# URL은 해당 원격 리포의 https (.git으로 끝난다)
$ git remote add origin https://github.com/hanna-debussy/TIL.git

# 원격 리포 확인
$ git remote -v

# 지금까지의 commit들 PUSH(=upload)
$ git push origin master

# 원격 리포를 최초 1회 다운받을 때
$ git clone <URL>

# 그 이후 원격 리포들 내용 이어 받아올 때
$ git pull origin master
```

### cf) 체크해야 할 것들

- `~`에서 `$ git init` 진행 XXXXX

- 리포 안에 리포 만들기 XXXXX

- 그러므로 `$ git init` 입력 전 확인해야 할 것들

  1. `~`에서 하고 있는 건 아닌지

     : 리포로 만들 폴더 안에서 해야 함

  2. `(master)`에서 하고 있는 건 아닌지

     : 이미 리포입니다

  3. 리포 폴더 안에서 하고 있는 건 아닌지

     : 현재 위치 꼭 확인하기