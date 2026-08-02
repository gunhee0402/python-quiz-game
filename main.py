import json
import os
import random


class Quiz:
    """단일 퀴즈 문제를 관리하는 클래스"""
    def __init__(self, question, choices, answer, category="일반", difficulty="EASY", hint=""):
        self.question = question
        self.choices = choices
        self.answer = answer
        self.category = category      # 카테고리
        self.difficulty = difficulty  # 난이도
        self.hint = hint              # 힌트

    def to_dict(self):
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer,
            "category": self.category,
            "difficulty": self.difficulty,
            "hint": self.hint
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            question=data["question"],
            choices=data["choices"],
            answer=data["answer"],
            category=data.get("category", "일반"),
            difficulty=data.get("difficulty", "EASY"),
            hint=data.get("hint", "등록된 힌트가 없습니다.")
        )


class QuizGame:
    """퀴즈 게임의 로직과 데이터를 관리하는 클래스"""
    def __init__(self, filepath="state.json"):
        self.filepath = filepath
        self.quizzes = []
        self.best_score = 0
        self.load_state()

    def load_state(self):
        """state.json 파일에서 데이터 불러오기"""
        if not os.path.exists(self.filepath):
            self.init_default_quizzes()
            self.save_state()
            return

        try:
            with open(self.filepath, "r", encoding="utf-8") as f:
                data = json.load(f)
                self.quizzes = [Quiz.from_dict(q) for q in data.get("quizzes", [])]
                self.best_score = data.get("best_score", 0)
        except Exception as e:
            print(f"\n[!] 데이터 파일 로드 중 오류 발생: {e}")
            self.init_default_quizzes()

    def save_state(self):
        """state.json 파일에 데이터 저장하기"""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score
        }
        with open(self.filepath, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def init_default_quizzes(self):
        """기본 퀴즈 데이터 초기화 (6개 문항)"""
        default_data = [
            {
                "question": "다음 중 이탈리아의 유명 슈퍼카 브랜드가 아닌 곳은?",
                "choices": ["페라리 (Ferrari)", "람보르기니 (Lamborghini)", "포르쉐 (Porsche)", "마세라티 (Maserati)"],
                "answer": 3,
                "category": "브랜드",
                "difficulty": "EASY",
                "hint": "독일 슈투트가르트에 본사를 둔 브랜드입니다."
            },
            {
                "question": "세계 최초로 컨베이어 벨트 양산 시스템을 도입하여 대량생산을 시작한 자동차 회사는?",
                "choices": ["포드 (Ford)", "GM (General Motors)", "벤츠 (Mercedes-Benz)", "토요타 (Toyota)"],
                "answer": 1,
                "category": "역사",
                "difficulty": "EASY",
                "hint": "모델 T를 제작한 미국 브랜드입니다."
            },
            {
                "question": "현대자동차 그룹의 독립 럭셔리 독자 브랜드 이름은 무엇인가요?",
                "choices": ["렉서스 (Lexus)", "제네시스 (Genesis)", "인피니티 (Infiniti)", "아큐라 (Acura)"],
                "answer": 2,
                "category": "브랜드",
                "difficulty": "EASY",
                "hint": "G80, GV80 등을 생산하는 브랜드입니다."
            },
            {
                "question": "전기차 제조사 테슬라(Tesla)의 현 최고경영자(CEO)는 누구인가요?",
                "choices": ["빌 게이츠 (Bill Gates)", "스티브 잡스 (Steve Jobs)", "일론 마스크 (Elon Musk)", "제프 베조스 (Jeff Bezos)"],
                "answer": 3,
                "category": "상식",
                "difficulty": "EASY",
                "hint": "스페이스X의 창업자이기도 합니다."
            },
            {
                "question": "독일의 대표 프리미엄 3사(독일 3사)에 속하지 않는 브랜드는?",
                "choices": ["메르세데스-벤츠", "BMW", "아우디", "볼보"],
                "answer": 4,
                "category": "브랜드",
                "difficulty": "EASY",
                "hint": "스웨덴 태생의 안전으로 유명한 브랜드입니다."
            },
            {
                "question": "세계에서 가장 빠른 양산차 타이틀을 가졌던 부가티의 대표 모델은?",
                "choices": ["베이론 (Veyron)", "아벤타도르 (Aventador)", "911 GT3", "파가니 와이라"],
                "answer": 1,
                "category": "상식",
                "difficulty": "HARD",
                "hint": "이름이 '베'로 시작합니다."
            }
        ]
        self.quizzes = [Quiz.from_dict(q) for q in default_data]

    def play(self):
        """퀴즈 풀기 진행"""
        if not self.quizzes:
            print("\n등록된 퀴즈가 없습니다. 퀴즈를 먼저 추가해주세요!")
            return

        print("\n=== 퀴즈 게임을 시작합니다! ===")
        score = 0
        wrong_quizzes = []

        # [보너스 1] 문제 순서 무작위 섞기 (Random Shuffle)
        play_quizzes = self.quizzes.copy()
        random.shuffle(play_quizzes)

        for idx, quiz in enumerate(play_quizzes, 1):
            # [보너스 4] 카테고리 및 난이도 출력
            print(f"\n[문제 {idx}/{len(play_quizzes)}] [{quiz.category} | 난이도: {quiz.difficulty}] {quiz.question}")
            for c_idx, choice in enumerate(quiz.choices, 1):
                print(f"  {c_idx}. {choice}")
            print("  H. 힌트 보기")

            while True:
                user_input = input("정답 번호 선택 (1-4 / H:힌트): ").strip()
                
                if user_input.upper() == 'H':
                    print(f"💡 힌트: {quiz.hint}")
                    continue

                if not user_input.isdigit():
                    print("숫자 1~4 또는 'H'를 입력해 주세요.")
                    continue

                choice_num = int(user_input)
                if 1 <= choice_num <= 4:
                    if choice_num == quiz.answer:
                        print("⭕ 정답입니다!")
                        score += 1
                    else:
                        print(f"❌ 오답입니다. (정답: {quiz.answer}번)")
                        wrong_quizzes.append((quiz, choice_num))
                    break
                else:
                    print("1부터 4 사이의 숫자를 입력해 주세요.")

        # [보너스 5] 정답률 및 등급 계산
        total = len(play_quizzes)
        rate = (score / total) * 100
        grade = "A" if rate >= 80 else ("B" if rate >= 60 else "F")

        print("\n=========================")
        print(f"🎉 최종 점수: {score} / {total} 점")
        print(f"📊 정답률: {rate:.1f}% (등급: {grade})")
        print("=========================")

        # [보너스 3] 오답 노트 출력
        if wrong_quizzes:
            print("\n📝 [오답 노트] 틀린 문제를 확인하세요:")
            for q, my_ans in wrong_quizzes:
                print(f"- {q.question}")
                print(f"  제출한 답: {my_ans}번 / 정답: {q.answer}번")

        if score > self.best_score:
            print(f"\n🎊 축하합니다! 최고 점수를 갱신하셨습니다! ({self.best_score}점 ➡️ {score}점)")
            self.best_score = score
            self.save_state()

    def add_quiz(self):
        """새로운 퀴즈 추가하기"""
        print("\n=== 새 퀴즈 추가 ===")
        question = input("문제 내용 입력: ").strip()
        while not question:
            print("문제 내용을 입력해야 합니다.")
            question = input("문제 내용 입력: ").strip()

        choices = []
        for i in range(1, 5):
            choice = input(f"선택지 {i} 입력: ").strip()
            while not choice:
                print("선택지를 입력해야 합니다.")
                choice = input(f"선택지 {i} 입력: ").strip()
            choices.append(choice)

        while True:
            ans_input = input("정답 번호 입력 (1-4): ").strip()
            if ans_input.isdigit() and 1 <= int(ans_input) <= 4:
                answer = int(ans_input)
                break
            print("1에서 4 사이의 올바른 숫자를 입력해 주세요.")

        category = input("카테고리 입력 (예: 브랜드, 상식 / Enter 시 '일반'): ").strip() or "일반"
        difficulty = input("난이도 입력 (EASY / HARD / Enter 시 'EASY'): ").strip().upper() or "EASY"
        hint = input("힌트 입력 (없을 경우 Enter): ").strip() or "등록된 힌트가 없습니다."

        new_quiz = Quiz(question, choices, answer, category, difficulty, hint)
        self.quizzes.append(new_quiz)
        self.save_state()
        print("\n✅ 새로운 퀴즈가 성공적으로 등록되었습니다!")

    def show_list(self):
        """등록된 퀴즈 목록 보기"""
        print("\n=== 등록된 퀴즈 목록 ===")
        if not self.quizzes:
            print("등록된 퀴즈가 없습니다.")
            return

        for idx, q in enumerate(self.quizzes, 1):
            print(f"\n{idx}. [{q.category} | {q.difficulty}] {q.question} (정답: {q.answer}번)")
            for c_idx, choice in enumerate(q.choices, 1):
                print(f"   {c_idx}) {choice}")
            print(f"   💡 힌트: {q.hint}")

    def show_best_score(self):
        """최고 점수 보기"""
        print(f"\n🏆 현재 최고 점수: {self.best_score}점")


def main():
    game = QuizGame()

    while True:
        try:
            print("\n=========================")
            print("  자동차 상식 퀴즈 게임  ")
            print("=========================")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록 보기")
            print("4. 최고 점수 확인")
            print("5. 종료")
            print("=========================")
            
            choice = input("원하는 메뉴 번호를 입력하세요: ").strip()

            if choice == "1":
                game.play()
            elif choice == "2":
                game.add_quiz()
            elif choice == "3":
                game.show_list()
            elif choice == "4":
                game.show_best_score()
            elif choice == "5":
                print("\n게임을 종료합니다. 이용해 주셔서 감사합니다!")
                break
            else:
                print("\n[!] 올바른 메뉴 번호(1~5)를 입력해 주세요.")

        except KeyboardInterrupt:
            print("\n\n[!] 강제 종료 신호(Ctrl+C)가 감지되었습니다. 게임을 안전하게 종료합니다.")
            break


if __name__ == "__main__":
    main()