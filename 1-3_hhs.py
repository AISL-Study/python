new_id=input("ID를 입력하세요:")
#1단계 소문자로 변환
new_id_1=new_id.lower() 
disallow="~!#@$%^&*()=+[{]}:?,<>/"
#2 특수문자 제거
for i in new_id_1:
    if i in disallow:
        new_id_1 =new_id_1.replace(i,'')
#3 연속된 '.' 제거        
for j in reversed(range(len(new_id_1))):
    if new_id_1[j] == new_id_1[j-1]:
         new_id_1 = new_id_1.replace('.','',1) 
#4 처음과 끝의 '.' 제거
if new_id_1 != '':
    if  new_id_1[0] == '.':
        new_id_1 = new_id_1[1:]
    elif new_id_1[-1]=='.':
        new_id_1 = new_id_1[:-1] 
#5 공백이면 'a'        
elif new_id_1=='':
     new_id_1 = 'a'    
#6 15자 이하
if len(new_id_1) >= 16:
    new_id_1 = new_id_1[:15]
    if new_id_1[-1]=='.':
        new_id_1 = new_id_1[:-1] 
#7 
if len(new_id_1) <= 2:
    while 1:
       last_element = str(new_id_1[-1])
       new_id_1 = str(new_id_1) + last_element
       if len(new_id_1) == 3:
            break
print("recommended ID: {}".format(new_id_1))