# git

- 분산 버전 관리 시스템
- 프로젝트 버전을 관리
  - 개발 되어온 과정을 파악할 수 있음
  - 이전 버전과 비교할 수 있음
- 코드의 변경 이력을 기록하고 협업을 원활하게 하는 도구

### 중앙집중식
- 버전은 중앙 서버에 저장, 중앙 서버에서 파일을 가져와 중앙에 업로도(ex.위키피디아)

### 분산식
- 버전을 여러개의 복제된 저장소에 저장 및 관리

- 분산 구조의 장점
  - 중앙 서버에 의존X
  - 장애나 손실에 대비, 백업과 복구에 용이
  - 인터넷 연결이 되지 않아도 작업 가능
---
## git의 영역
- Working Directory : 그냥 파일, 아직 프로젝트의 일부X(물리적으로만 존재)
- Staging Area 
  - 추가될 파일, 실제로 프로젝트 버전에 일부분에 들어갈 파일
  - Working Directory에서 변경된 파일 중, 다음 버전에포함시킬 파일들을 추가하거나 제외할 수 있는 중간 영역
- Repositary(저장소) 
  - 버전에 추가 된 파일, 변경사항이 있는 파일을 다시 Working Directory, 변경사항이라는 파일이 생김
  - 버전 이력과 파일들이 영구적으로 저장된느 영역, 모든 버전과 변경 이력이 기록

  ### commit(기여하다, 저장, 버전)
  - 변경된 파일들을 저장하는 행위이며, 마치 사진을 찍듯이 기록한다 하여 'snap shot'이라고도 함
  - local repository에 저장

  ## git 명령어
  - git init : 저장소를 초기화
  - git status 
    - 어떤 파일이 tracked 되고 있지 않은지 나옴.
    - Working Directory(버전으로 인식하지 않음)
  - git add  파일명 : Staging Area로 넘어감, 다음버전에 추가가 될 파일
- git commit -m (”~”): ~ 메세지를 남기겠다>한 번에 되지 않음(프로젝트 내용같은거)
- git config --global user.email(name) : 이메일, 이름 설정
(이름, 이메일 설정 후 git commit -m 하기)

- git log : 여태 한 걸 기록으로 확인
- git log --oneline : git log를 압축해서

- 로컬 저장소 내 모든 파일의 ‘변경사항’을 감시

- git remote add (이름(origin)) 주소 추가
  - git remote seturl

- git geturl>확인

 - -u > user

- git push (-u) origin master : 원격저장소에 commit을 업로드
- push : 내가 가진 걸 줌/ -u, - - set-up stream
- pull : 내가 받음(clone)
- git clone > 복제/ 서로 다른 두 개발자가 참여할 수 있음

- git revert 페이지 번호(git log  - -oneline하면 나오는)vim이 나옴
- git revert에서도 conflict > 과거의 영향을 받음
  - git commit -m “merge conflict”으로 해소

- git reset[옵션] <commit id>

- —soft, —hard, —mixed

**[git init 주의 사항]**

- git 로컬 저장소 내에 또다른 git 로컬 저장소를 만들지 말 것
  - 이미 git 로컬 저장소인 디렉토리 내부 하단에서 git init 명령어를 다시 입력하지 말것
  - git 저장소 안에 git 저장소가 있을 경우 가장 바깥 쪽의 git 저장소가 안쪽의 git 변경사항을 추적할 수 없기 때문


*ammend > commit 메세지 수정, 전체 수정

## Remote Repositary

- 코드와 버전 관리 이력을 **온라인 상의 특정 위치에 저장**하여 여러 개발자가 협업하고 코드를 공유할 수 있는 공간 >> git hub, git lab, bitbucket

git push (-u) origin master : 원격저장소에 commit을 업로드

### local과 github

- push : 내가 가진 걸 줌/ -u, - - set-up stream
- pull : 내가 받음(clone)

- git은 commit  단위로 기억
  - commit 이력이 없다면 push 할 수 없다

- pull/clone

- git clone > 복제/ 서로 다른 두 개발자가 참여할 수 있음
- git clone 후 파일 생성된 거 확인하기

### gitignore 주의 사항
- 이미 git의 관리를 받은 이력이 있는 파일이나 디렉토리는 나중에 gitignore에 작성해도 적용되지 않음

- git rm -- cached 명령어를 통해 git 캐시 삭제 필요

### commit
local repository 에 저장

### push
- local > remote repository로 보내기

### clone

- 원격 저장소 전체를 복제(다운로드) 

***conflict- 2가지가 공존할 수 없는 상황**

수정해서 저장하고
git add 하고 git commit -m “merge conflict, keep ~~~~”으로 해소
git push
후 다른 vscode에서 git pull