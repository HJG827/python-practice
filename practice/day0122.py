# 스코프 연습하기 

a = 10
b = 20
c = 30
def outer_fun():
    global a
    a = 40
    b = 50
    c = 60
    def inner_fun():
        global b
        print(f"inner fun's b: {b}")
        print(f"inner fun's c: {c}")
    inner_fun()

outer_fun()
print(f"global a: {a}")

# inner fun's b: 20
# inner fun's c: 60
# global a: 40