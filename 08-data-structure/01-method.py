print(type('1'))
print(type([1,2]))
# print(help(str))


def add(a,b):
    return a + b

# 클래스 파트에서 이어서 진행할 예정
class Calculator:
    def add(self, a, b):
        return a + b

# 함수 호출
add(1, 2)

# 메서드 호출
a = Calculator()
a.add(1, 2)