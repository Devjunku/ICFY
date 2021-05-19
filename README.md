# Final-PJT

# Git 협업 방법

Pull Request를 통한 지속적인 병합으로 최신 셋팅

commit role 꼭 지켜야합니다!

push시 꼭 이야기 해줍시다!

## Github pr 방법

### 1. 부모 repository를 Fork 합니다.

Fork 버튼은 github respository로 들어가면
오른쪽 상단에 위치에 있습니다.
클릭만해도 자동으로 나의 repository로 Fork 됩니다.

이후 Fork 한 저장소를 그대로

`$ git clone 포크한URL`

를 입력합니다.

gitbash를 킨 다음

origin이 잘 저장되었는지 확인합니다.

`$ git remove -v`

### 2. upstream을 입력합니다.

origin이 잘 입력되었는지 확인되었다면,

upstream을 입력합니다.

`$ git remote add upstream 오리지널저장소URL`

이후 파일이 추가되면

### 3. branch로 push 합니다.(되도록 branch명은 영어로 작성합니다.)

`$ git switch -c branch_name`

`$ git status`

`$ git add . or filename_extension`

`$ git commit -m 'slack에 적힌 양식을 따릅니다.'`

`$ git push origin branch_name`


### 4. pr 양식은 다음과 같이 진행합니다.

제목: `초기 commit명과 같을겁니다. 이를 그대로 사용합니다.`

내용

**수정사항**

**해당 수정 이후 진행할 부분**


### 5. 해당 pr이 검증되면(회의에서 사용하기로 했으면), merge합니다.

pr merge는 github에서 진행합니다.

github merge 이후 로컬 저장소(본인 pc git folder)에서 branch를 삭제합니다.


`$ git branch -d branch_name` → 약한 삭제(본인 gitbash에서 git merge를 해야 명령어가 먹힐겁니다.)

or

`$ git branch -D branch_name` → 강한 삭제(따로 git merge를 하지 않아도 명령어가 먹힙니다.)


**END**