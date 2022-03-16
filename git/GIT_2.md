# Git Branch

## start

```bash
$ git init
# 브랜치 목록 확인
$ git branch
# 새로운 브랜치 생성
$ git branch 브랜치 이름
```



## delete

```bash
# 병합된 브랜치 삭제
$ git branch -d 브랜치 이름
# 병합 상관 없이 리얼 삭제
$ git branch -D 브랜치 이름
```



## switch

```bash
# 해당 브랜치로 이동
$ git switch 브랜치 이름
# 브랜치 생성과 동시에 이동
$ git switch -c 브랜치 이름
# 혹시 예전 버전이라면 이럴 수도 있다
$ git checkout 브랜치 이름
$ git checkout -b 브랜치 이름
# 얘는 switch 또는 restore 해줌 지금은 해당 명령어들로 분리가 됨
```



## log(status)

```bash
# git 버전...? log 한 줄로
$ git log --oneline
# 그 뭐냐 내 앞에 있는 브랜치까지 전부 보여주는 log
$ git log --oneline --all
# 브랜치를 그래프(...작대기)으로 볼 수 있다
$ git log --oneline --all --graph
```



## merge

```bash
# 브랜치 병합(merge)
# 메인 브랜치에서 해야한다
$ git merge 병합할 브랜치 이름
```

1. fast-forward
   : 병합이라기보다는 그냥 마스터가 최신 버전으로 나아간다
2. 3-way merge (merge commit)
   : 이게 보통의 생각하는 머지... 브랜치 뻗은 거랑 내가 마스터에서 뻗은거 합치는 거...
   하고 나서 뻗은 브랜치는 합쳐졌으니까 브랜치의 역할은 끝났기 때문에 슥삭 지우는 게 보통
3. merge conflict
   : 두 브랜치에서같은 파일의 같은 부분을 동시에 수정하고 merge하면 git은 안 해준다 대신 겁나 친절하게 알려주고 vim이 뜬다 그러면 `:wq` 해주고 나오면 된대
   오 근데? 같은 파일이라도 다른 부분을 수정했다면 conflict 안 됨





