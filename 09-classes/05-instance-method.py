class Counter:
    def __init__(self):
        self.count = 0

    def increasement(self):
        self.count += 1



c = Counter()
# Counter.__init__(인스턴스)
print(c.count)  # 0
c.increasement()
print(c.count)  # 1

c2 = Counter()
c.increasement()
print(c2.count)  # 0
print(c.count)  # 2