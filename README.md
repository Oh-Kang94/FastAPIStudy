# 🚀 FASTAPI STUDY

## 📚 목적

기존에는 FastAPI를 그때그때 필요할 때마다 주먹구구식으로 익힘.  
이번 스터디는 **[책](https://product.kyobobook.co.kr/detail/S000201188332)이나 강의 등 검증된 학습 자료를 기반으로**,  
**FastAPI를 보다 체계적으로 학습**하고,  
지속 가능한 실력을 쌓는 것을 목표.

## 🎯 목표

- FastAPI의 핵심 개념과 작동 원리 이해 [ ]
- 실제 서비스에 적용 가능한 코드 작성 능력 향상 [ ]
- 학습 내용을 문서화하고 정리하여 지식의 자산화 [ ]
- TestCode 작성 및 체계화 [ ]

## 환경 (Environment)

- 프로젝트 환경은 [`uv`](https://github.com/astral-sh/uv)를 사용하여 구성합니다.
- Python 버전: **3.11**

---

## 실행 방법 (Execution)

### 초기 세팅 (Initial Settings)

```sh
    uv venv                     # 가상환경 생성
    source .venv/bin/activate   # 가상환경 활성화
    uv sync                     # pyproject.toml 기준으로 패키지 설치
```

### 개발 서버 실행 (Dev Run)

#### 명령어 (Scripts)

```sh
    (venv) $ uvicorn api:app --port 8000 --reload
    # 형식: uvicorn [파일명]:[FastAPI 인스턴스 변수명]
    # 예: api.py 파일 내의 app 인스턴스를 실행
```

#### VS Code용 .launch.json 설정

```json
{
  "version": "0.2.0",
  "configurations": [
    {
      "name": "FastAPI Study Dev",
      "type": "debugpy",
      "request": "launch",
      "module": "uvicorn",
      "args": ["api:app", "--reload"],
      "console": "internalConsole",
      "jinja": true
    }
  ]
}
```
