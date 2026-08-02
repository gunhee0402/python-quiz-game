import json
import os

# ==========================================
# 1. Quiz 클래스 (개별 문제 틀)
# ==========================================
class Quiz:
    def __init__(self, question, choices, answer):
        self.question = question   # 질문 내용
        self.choices = choices     # 보기 4개 (리스트)
        self.answer = answer       # 정답 번호 (1~4)

    def display(self, number):
        """문제를 화면에 출력"""
        print(f"\n[문제 {number}] {self.question}")
        for i, choice in enumerate(self.choices, 1):
            print(f"  {i}. {choice}")

    def is_correct(self, user_answer):
        """정답 제출 확인"""
        return self.answer == user_answer

    def to_dict(self):
        """JSON 저장을 위해 딕셔너리로 변환"""
        return {
            "question": self.question,
            "choices": self.choices,
            "answer": self.answer
        }


# ==========================================
# 2. 공통 예외 처리 함수 (안전한 숫자 입력)
# ==========================================
def get_valid_input(prompt, min_val, max_val):
    while True:
        try:
            raw_input = input(prompt).strip()
            if not raw_input:
                print("⚠️ 빈 입력입니다. 다시 입력해주세요.")
                continue
            
            value = int(raw_input)
            if min_val <= value <= max_val:
                return value
            else:
                print(f"⚠️ {min_val}~{max_val} 사이의 숫자를 입력하세요.")
        except ValueError:
            print("⚠️ 숫자로만 입력해주세요.")
        except (KeyboardInterrupt, EOFError):
            print("\n\n⚠️ 프로그램이 안전하게 종료되었습니다.")
            exit(0)


# ==========================================
# 3. QuizGame 클래스 (전체 게임 관리)
# ==========================================
class QuizGame:
    def __init__(self, filename="state.json"):
        self.filename = filename
        self.quizzes = []
        self.best_score = 0
        self.load_data()

    def get_default_quizzes(self):
        """기본 퀴즈 데이터 5개 (파이썬 기초 주제)"""
        return [
            Quiz("파이썬의 창시자는 누구일까요?", ["Guido van Rossum", "Elon Musk", "Steve Jobs", "Bill Gates"], 1),
            Quiz("다음 중 파이썬의 기본 자료형이 아닌 것은?", ["int", "str", "bool", "array"], 4),
            Quiz("리스트의 맨 뒤에 요소를 추가하는 메서드는?", ["add()", "append()", "push()", "insert()"], 2),
            Quiz("파이썬의 조건문 키워드가 아닌 것은?", ["if", "elif", "else", "then"], 4),
            Quiz("JSON 데이터 저장 시 권장하는 인코딩은?", ["UTF-8", "ASCII", "EUC-KR", "UTF-16"], 1)
        ]

    def load_data(self):
        """state.json 파일 읽기 및 예외 처리"""
        if not os.path.exists(self.filename):
            self.quizzes = self.get_default_quizzes()
            self.save_data()
            return

        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                data = json.load(f)
                self.best_score = data.get("best_score", 0)
                self.quizzes = [
                    Quiz(q["question"], q["choices"], q["answer"]) 
                    for q in data.get("quizzes", [])
                ]
            print(f"📂 저장된 데이터를 불러왔습니다. (퀴즈 {len(self.quizzes)}개, 최고점수 {self.best_score}점)")
        except Exception:
            print("⚠️ 데이터 파일이 손상되었습니다. 기본 데이터로 초기화합니다.")
            self.quizzes = self.get_default_quizzes()
            self.best_score = 0
            self.save_data()

    def save_data(self):
        """state.json 파일에 저장"""
        data = {
            "quizzes": [q.to_dict() for q in self.quizzes],
            "best_score": self.best_score
        }
        with open(self.filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=4)

    def play_quiz(self):
        """1. 퀴즈 풀기"""
        if not self.quizzes:
            print("\n⚠️ 등록된 퀴즈가 없습니다.")
            return

        print(f"\n📝 퀴즈를 시작합니다! (총 {len(self.quizzes)}문제)")
        score = 0

        for idx, quiz in enumerate(self.quizzes, 1):
            quiz.display(idx)
            user_ans = get_valid_input("정답 입력 (1-4): ", 1, 4)
            if quiz.is_correct(user_ans):
                print("✅ 정답입니다!")
                score += 1
            else:
                print(f"❌ 오답입니다! (정답: {quiz.answer}번)")

        print(f"\n========================================")
        print(f"🏆 결과: {len(self.quizzes)}문제 중 {score}문제 정답!")
        if score > self.best_score:
            print("🎉 축하합니다! 새로운 최고 점수입니다!")
            self.best_score = score
            self.save_data()
        print(f"========================================")

    def add_quiz(self):
        """2. 퀴즈 추가"""
        print("\n📌 새로운 퀴즈를 추가합니다.")
        question = input("문제를 입력하세요: ").strip()
        while not question:
            print("⚠️ 문제는 빈 값일 수 없습니다.")
            question = input("문제를 입력하세요: ").strip()

        choices = []
        for i in range(1, 5):
            choice = input(f"선택지 {i}: ").strip()
            while not choice:
                print("⚠️ 선택지는 빈 값일 수 없습니다.")
                choice = input(f"선택지 {i}: ").strip()
            choices.append(choice)

        answer = get_valid_input("정답 번호 (1-4): ", 1, 4)
        
        new_quiz = Quiz(question, choices, answer)
        self.quizzes.append(new_quiz)
        self.save_data()
        print("\n✅ 퀴즈가 성공적으로 추가되었습니다!")

    def show_quiz_list(self):
        """3. 퀴즈 목록 보기"""
        print(f"\n📋 등록된 퀴즈 목록 (총 {len(self.quizzes)}개)")
        print("-" * 40)
        for idx, quiz in enumerate(self.quizzes, 1):
            print(f"[{idx}] {quiz.question}")
        print("-" * 40)

    def show_score(self):
        """4. 최고 점수 확인"""
        print(f"\n🏆 현재 최고 점수: {self.best_score}점")

    def run(self):
        """게임 메인 메뉴 실행"""
        while True:
            print("\n========================================")
            print("        🎯 나만의 퀴즈 게임 🎯")
            print("========================================")
            print("1. 퀴즈 풀기")
            print("2. 퀴즈 추가")
            print("3. 퀴즈 목록")
            print("4. 점수 확인")
            print("5. 종료")
            print("========================================")
            
            choice = get_valid_input("선택: ", 1, 5)
            
            if choice == 1:
                self.play_quiz()
            elif choice == 2:
                self.add_quiz()
            elif choice == 3:
                self.show_quiz_list()
            elif choice == 4:
                self.show_score()
            elif choice == 5:
                print("\n게임을 종료합니다. 이용해 주셔서 감사합니다!")
                break

if __name__ == "__main__":
    game = QuizGame()
    game.run()