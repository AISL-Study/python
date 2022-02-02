import mod4
class Calculator:
    def __init__(self, first, second):
        self.first = first
        self.second = second
    def addition(self):
        value = self.first + self.second
        return value
    def subtraction(self):
        value = self.first - self.second
        return value
    def multiple(self):
        value = self.first * self.second
        return value 
    def div(self):
        if self.second == 0:  
           return "0으로 나눌 수 없습니다."
        else:
             return self.first / self.second

class ImprovedCalculator(Calculator):
    def square(self):
        return mod4.square(self.first,self.second)
    def gcd(self):
        return mod4.gcd(self.first,self.second)

def main():   
    while 1:
        print(
            "아래에 사용을 원하시는 사칙연산을 선택해 주세요!\n"
            "1.더하기\n"
            "2.빼기\n"
            "3.곱하기\n"
            "4.나누기\n"
            "5.제곱\n"
            "6.최대공약수\n"
            "7.종료\n>>"
            )
       
        mode=input()
        if mode =='7':
            print("계산기 프로그램을 종료합니다.")
            break

        number=list(map(int,input("두 수를 입력해 주세요:").split()))
        output=ImprovedCalculator(number[0],number[1])

        if mode == '1':
            print(output.addition())
        if mode == '2':
            print(output.subtraction())
        if mode == '3':
            print(output.multiple())
        if mode == '4':
            print(output.div())
        if mode == '5':
            print(output.square())
        if mode == '6':
            print(output.gcd())
        
main()