class Banking:
    def __init__(self, name, balance):
        self.name = name #Public
        self.__balance = balance #Private

    def set_balance(self, new_balance):
        self.__balance = new_balance

    def get_balance(self):
        return self.__balance

acc1 = Banking("Rahul", 10000)

print(acc1.name, acc1.get_balance())