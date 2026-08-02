# 나만의 자동차 상식 콘솔 퀴즈 게임

터미널 환경에서 즐기는 파이썬 기반의 콘솔 퀴즈 게임 프로그램입니다.  
객체지향 프로그래밍(OOP) 개념을 적용하여 `Quiz`와 `QuizGame` 클래스로 구조화하였으며, JSON 파일 저장 방식으로 데이터 영속성을 구현했습니다.

---

## 퀴즈 주제 및 선정 이유
* **주제**: 자동차 상식 및 브랜드/모델 관련 퀴즈
* **선정 이유**: 평소 관심 주제인 자동차를 활용하여 퀴즈를 만드는게 좋을 것 같아서 선정했습니다.

---

## 실행 방법

### 1. 개발 환경
* Python 3.10 이상

### 2. 실행 명령어
터미널에서 작업 디렉토리로 이동 후 아래 명령어를 입력합니다.

```bash
python3 main.py
```


## 기능 목록
 1. 퀴즈 풀기: 저장된 퀴즈를 순서대로 풀고 정답 여부를 판별하여 최종 점수를 계산합니다.
 2. 퀴즈 추가: 사용자가 새로운 문제, 4개 선택지, 정답 번호를 직접 등록할 수 있습니다.
 3. 퀴즈 목록: 등록된 전체 퀴즈 문제 목록을 한눈에 조회합니다.
 4. 점수 확인: 게임 종료 후 최고 점수를 기록하고 확인할 수 있습니다.
 5. 데이터 영속성: 퀴즈 및 최고 점수는 state.json 파일로 자동 저장/불러오기됩니다.
 6. 예외 처리: 공통 입력 검증(공백, 문자 입력, 범위 밖 숫자) 및 Ctrl+C 비정상 종료 방지를 지원합니다.
 
 ## 파일 구조
 ```bash
python-quiz-game/
├── main.py              # 퀴즈 게임 메인 프로그램
├── state.json           # 퀴즈 및 최고 점수 저장 데이터 파일
├── README.md            # 프로젝트 설명서
├── .gitignore           # Git 추적 제외 설정 파일
└── docs/
    └── screenshots/     # 증빙 및 실행 화면 스크린샷 폴더
        ├── add_quiz.png # 퀴즈 추가 스크린샷
        ├── env.png      # 개발 환경 스크린샷
        ├── git_log.png  # Git Log 스크린샷
        ├── menu.png     # 메인 메뉴 스크린샷
        ├── play.png     # 퀴즈 풀기 스크린샷
        └── score.png    # 점수 확인 스크린샷
```

## 데이터 파일 설명 (state.json)
프로젝트 루트 경로에 UTF-8 인코딩으로 저장되며, 프로그램 실행 시 자동으로 로드됩니다.

### JSON 스키마 예시
 ```bash
{
    "quizzes": [
        {
            "question": "다음 중 이탈리아의 유명슈퍼카 브랜드가 아닌곳은?",
            "choices": [
                "페라리 (Ferrari)",
                "람보르기니 (Lamborghini))",
                "포르쉐 (Porsche)",
                "마세라티 (Maserati)"
            ],
            "answer": 3
        }
    ],
    "best_score": 5
}
```

## 제출 증빙 스크린샷

### 1. 개발 환경 설정
![개발 환경](docs/screenshots/env.png)

### 2. 프로그램 실행 결과
| 메인 메뉴 | 퀴즈 풀기 |
| :---: | :---: |
| ![메인 메뉴](docs/screenshots/menu.png) | ![퀴즈 풀기](docs/screenshots/play.png) |

| 퀴즈 추가 | 점수 확인 |
| :---: | :---: |
| ![퀴즈 추가](docs/screenshots/add_quiz.png) | ![점수 확인](docs/screenshots/score.png) |

### 3. Git Log 그래프 (`git log --oneline --graph`)
![Git Log](docs/screenshots/git_log.png)