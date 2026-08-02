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
 
 ### 보너스 구현 기능
1. 문제 무작위 출제: `random.shuffle()` 모듈을 활용하여 퀴즈 게임 시작 시 매번 문제 순서를 무작위로 변경.
2. 힌트 보기 시스템: 퀴즈 풀이 중 `H` 키 입력 시 해당 문제에 등록된 힌트 출력.
3. 오답 노트 기능: 게임 완료 후 내가 틀린 문제와 제출했던 답, 정답을 한눈에 복습할 수 있도록 출력.
4. 퀴즈 카테고리 및 난이도 분류: 각 문제마다 카테고리(예: 브랜드, 상식)와 난이도(EASY/HARD) 속성을 추가하고 문제 출력 시 표시.
5. 정답률 계산 및 등급 부여: 최종 결과에서 단순 점수 외에 소수점 1자리 정답률과 판정 등급(A/B/F)을 실시간 산출.


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
            "question": "다음 중 이탈리아의 유명 슈퍼카 브랜드가 아닌 곳은?",
            "choices": [
                "페라리 (Ferrari)",
                "람보르기니 (Lamborghini)",
                "포르쉐 (Porsche)",
                "마세라티 (Maserati)"
            ],
            "answer": 3,
            "category": "브랜드",
            "difficulty": "EASY",
            "hint": "독일 슈투트가르트에 본사를 둔 브랜드입니다."
        },
        {
            "question": "세계 최초로 컨베이어 벨트 양산 시스템을 도입하여 대량생산을 시작한 자동차 회사는?",
            "choices": [
                "포드 (Ford)",
                "GM (General Motors)",
                "벤츠 (Mercedes-Benz)",
                "토요타 (Toyota)"
            ],
            "answer": 1,
            "category": "역사",
            "difficulty": "EASY",
            "hint": "모델 T를 제작한 미국 브랜드입니다."
        },
        {
            "question": "현대자동차 그룹의 독립 럭셔리 독자 브랜드 이름은 무엇인가요?",
            "choices": [
                "렉서스 (Lexus)",
                "제네시스 (Genesis)",
                "인피니티 (Infiniti)",
                "아큐라 (Acura)"
            ],
            "answer": 2,
            "category": "브랜드",
            "difficulty": "EASY",
            "hint": "G80, GV80 등을 생산하는 브랜드입니다."
        },
        {
            "question": "전기차 제조사 테슬라(Tesla)의 현 최고경영자(CEO)는 누구인가요?",
            "choices": [
                "빌 게이츠 (Bill Gates)",
                "스티브 잡스 (Steve Jobs)",
                "일론 마스크 (Elon Musk)",
                "제프 베조스 (Jeff Bezos)"
            ],
            "answer": 3,
            "category": "상식",
            "difficulty": "EASY",
            "hint": "스페이스X의 창업자이기도 합니다."
        },
        {
            "question": "독일의 대표 프리미엄 3사(독일 3사)에 속하지 않는 브랜드는?",
            "choices": [
                "메르세데스-벤츠",
                "BMW",
                "아우디",
                "볼보"
            ],
            "answer": 4,
            "category": "브랜드",
            "difficulty": "EASY",
            "hint": "스웨덴 태생의 안전으로 유명한 브랜드입니다."
        },
        {
            "question": "세계에서 가장 빠른 양산차 타이틀을 가졌던 부가티의 대표 모델은?",
            "choices": [
                "베이론 (Veyron)",
                "아벤타도르 (Aventador)",
                "911 GT3",
                "파가니 와이라"
            ],
            "answer": 1,
            "category": "상식",
            "difficulty": "HARD",
            "hint": "이름이 '베'로 시작합니다."
        },
        {
            "question": "아반떼의 제조사로 옳은 것은?",
            "choices": [
                "현대",
                "기아",
                "르노",
                "닛산"
            ],
            "answer": 1,
            "category": "브랜드",
            "difficulty": "EASY",
            "hint": "ㅎ으로 시작함"
        }
    ],
    "best_score": 6
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