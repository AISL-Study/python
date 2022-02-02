book_info = {
    "Harrypotter1" : [[1997], [6], [26]],
    "TheLordOfTheRings" : [[1954], [7], [29]],
    "engineering_mathematics1" : [[2018], [2], [28]],
}
while 1:
    title=input('''원하시는 책을 입력하세요.
>''')
    if title in book_info:
        mode =input("--------------------------\n"
                "원하시는 정보를 선택해주세요.\n"
                "1. 년\n"
                "2. 월\n"
                "3. 일\n"
                "4. 종료\n"
                "--------------------------\n")
        if mode =='1':
            print("{}년 입니다.".format(book_info[title][0]))
        elif mode =='2':
            print("{}월 입니다.".format(book_info[title][1]))
        elif mode =='3':
            print("{}일 입니다.".format(book_info[title][2]))
        elif mode =='4':
            print("프로그램이 종료되었습니다.")
            break
    else:
        print("제목을 다시 입력해주세요.")               
    

