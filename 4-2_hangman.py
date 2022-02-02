import random

def correct_word():
    alphabet_index = answer.find(alphabet)
    # 일치하는 알파벳을 최초로 찾은 경우
    if word[alphabet_index] == '_' :
        print("correct")
        word[alphabet_index] = alphabet
        correct_word()
    # 일치하는 알파벳이 여러개인 경우
    else:
        alphabet_index +=1
        alphabet_index = int(answer[alphabet_index:].find(alphabet)) + alphabet_index
        word[alphabet_index] = alphabet
        return 

def display_word():
    for i in word:
        print(i,end=' ')
    print()

def wrong_answer():
    global chance
    chance -=1
    print("wrong  남은 시도 횟수: {}".format(chance))
    
        

#리스트에 4개 이상의 단어 추가
list=['python', 'programing','line','hangman']
#위 리스트에서 랜덤으로 1개의 단어 선택 
answer =list[random.randint(0,3)]
#단어의 길이에 맞게 밑줄 생성
word=['_'] * len(answer)

chance = 6
while 1:
    display_word()
    alphabet = input("Input letter >")
    # 입력된 알파벳이 정답에 존재하는 경우
    if alphabet in answer: 
        correct_word()
    # 모든 알파벳을 맞춘 경우
        if '_' not in word:
            display_word()
            print("SUCCESS")
            break           
    # 입력된 알파벳이 정답에 존재하지 않는 경우
    else:
        wrong_answer()
    # 6번의 기회를 모두 사용한 경우
        if chance == 0:
            print("word ={}".format(answer))
            break

