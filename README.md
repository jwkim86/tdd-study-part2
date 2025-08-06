# TDD Study Part 2

## Windows Python 환경 설정
### 준비물
- https://scoop.sh/ 설치
   

### 환경 설정
1. **Python 설치**
   - Chocolatey로 설치:  
     `$ choco install python`
   - 설치 후, 명령 프롬프트에서 `python --version`으로 정상 설치 확인
2. pipx 설치
- scoop install pipx
     pipx ensurepath
3. poetry 설치
- pipx install poetry

2. 가상환경인 venv 대신 설정이 쉬운 poetry 설치
  - pip install poetry
  - 

2. **pip, venv 등 기본 도구 확인**
   - pip: `python -m pip --version`
   - venv: `python -m venv --help`

3. **가상환경 생성 및 활성화**
   - 가상환경 생성:  
     `$ python -m venv venv`
   - 가상환경 활성화:  
     `$ .\venv\Scripts\activate`
   - 비활성화:  
     `$ deactivate`

4. **필수 패키지 설치**
   - 예시:  
     `$ pip install pytest`

7. **(선택) .gitignore 파일에 venv 추가**
   - `.gitignore` 파일에 아래 내용 추가:  
     `venv/`

---

### [문제 해결] python --version 실행 시 버전이 보이지 않을 때
- `python --version` 명령어 실행 시 "Python"만 출력되고 버전 숫자가 보이지 않는 경우, 
  뭘로 설치하던 앱스토어로 이동해서 설치해야 되는듯 합니다.

---

## Poetry 사용법

### 1. Poetry 설치
- pipx로 설치: `pipx install poetry`
- pip로 설치: `pip install poetry`

### 2. 프로젝트 생성
- `poetry new 프로젝트명`  # 새 프로젝트 생성
- `po`            # 기존 폴더에 pyproject.toml 생성

### 3. 의존성(패키지) 추가/삭제
- 패키지 추가: `poetry add 패키지명`
- 개발용 패키지 추가: `poetry add --dev 패키지명`
- 패키지 삭제: `poetry remove 패키지명`

### 4. 가상환경 및 실행
- 가상환경 생성/활성화: `poetry shell`
- 명령 실행: `poetry run python main.py` (예시)

### 5. 의존성 설치
- `poetry install`  # pyproject.toml 기반 전체 패키지 설치

### 6. 패키지 업데이트
- `poetry update`   # 모든 패키지 최신화

### 7. 패키지 배포
- `poetry build`    # 패키지 빌드
- `poetry publish`  # PyPI 업로드

### 8. 기타
- 현재 환경 정보: `poetry show`
- lock 파일 재생성: `poetry lock`

---

자세한 내용은 공식 문서(https://python-poetry.org/docs/) 참고

#### 참고
- Chocolatey 설치 방법: https://chocolatey.org/install
- Python 공식 사이트: https://www.python.org/
- VS Code 공식 사이트: https://code.visualstudio.com/
