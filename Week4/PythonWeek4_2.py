# 2. 행맨 게임(영어 단어 퀴즈) 프로그램 만들기
import random

# 리스트에 단어 추가 (4개 이상)
word_list = ["python", "programing", "line", "hangman"]
# 리스트에서 랜덤으로 단어 1개 선택
answer = random.choice(word_list)
# 단어의 길이에 맞추어 밑줄 생성
try_word = "_ " * len(answer)
# 남은 시도 횟수
count = 6

while True:
    # 문제 단어 출력
    print()
    print(try_word)
    # 하나의 글자 입력
    letter = input("Input letter > ")
    # 단어가 입력받은 글자를 포함하는지 확인
    find_letter = answer.find(letter)

    # 단어에 입력받은 글자가 존재하지 않는 경우
    if find_letter == -1:
        count -= 1
        # 남은 시도 횟수 출력
        print("Wrong 남은 시도 횟수: {}".format(count))
        # 시도 횟수가 0인 경우 - 프로그램 종료
        if count == 0:
            # 정답 공개
            print("word = {}".format(answer))
            break
    # 단어에 입력 받은 글자가 존재하는 경우
    else:
        for i in range(len(answer)):
            if answer[i] == letter:
                # 현재 맞은 글자를 저장
                try_word = try_word[0:i * 2] + answer[i] + try_word[i * 2 + 1:]
        print("Correct")

    # 정답을 맞힌 경우 - 프로그램 종료
    if answer == try_word.replace(" ", ""):
        print()
        print(try_word)
        print("SUCCESS")
        print("word = {}".format(answer))
        break