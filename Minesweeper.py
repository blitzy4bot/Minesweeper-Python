import random


class Minesweeper:

    def __init__(self, x, y, tries):
        self.x = x
        self.y = y
        self.mines = 0
        self.hits = 0
        self.misses = 0
        self.triesNeeded = 0
        self.tries = tries
        self.list0 = []
        self.list1 = []
        self.list2 = []
        self.listFinal = []
        self.listFinalViewable = []
        self.active = True

    def create_field(self):
        for i in range(self.x):
            self.list0.append(0)
        for i in range(self.y):
            self.list1 = self.list0[:]
            self.listFinal.append(self.list1)
            self.list2 = self.list1[:]
            self.listFinalViewable.append(self.list2)

    def insert_random(self):
        chars = ["+", "-"]
        list_ran = self.listFinal[:]
        for i in range(self.y):
            for ii in range(self.x):
                ran = random.choice(chars)
                list_ran[i][ii] = ran
        for i in range(0, self.y):
            for ii in range(0, self.x):
                self.listFinal[i][ii] = str(list_ran[i][ii])

    def initViewableBoard(self):
        _list = self.listFinalViewable[:]
        for i in range(self.y):
            for ii in range(self.x):
                _list[i][ii] = "*"
        for i in range(0, self.y):
            for ii in range(0, self.x):
                self.listFinalViewable[i][ii] = str(_list[i][ii])
    
    def set_ammount_mines(self):
        for i in range(0, self.y):
            for ii in range(0, self.x):
                if self.listFinal[i][ii] == "+":
                    self.mines += 1

    def get_ammount_mines(self):
        print(f"Ammount of mines: {self.mines}")

    def checkBoard(self):
        var0 = 0
        num_list = []
        for i in range(self.x + 1):
            num_list.append(var0)
            var0 += 1
        print(" | ".join(map(str, num_list)))
        num_list1 = ["---"]
        for i in range(self.x + 1):
            num_list1.append("-" * 4)
        print(''.join(map(str, num_list1)))
        var1 = 1
        for i in self.listFinal:
            print(f"{var1} | {' | '.join(map(str, i))}")
            var1 += 1
        print("\n")

    def checkViewableBoard(self):
        var0 = 0
        num_list = []
        for i in range(self.x + 1):
            num_list.append(var0)
            var0 += 1
        print(" | ".join(map(str, num_list)))
        num_list1 = ["---"]
        for i in range(self.x + 1):
            num_list1.append("-" * 4)
        print(''.join(map(str, num_list1)))
        var1 = 1
        for i in self.listFinalViewable:
            print(f"{var1} | {' | '.join(map(str, i))}")
            var1 += 1
        print("\n")  
    
    def seek(self, x, y):
        if self.allowed():
            if not self.x < x or not self.y < y:
                if self.listFinalViewable[x-1][y-1] == "*":
                    self.triesNeeded += 1
                    if self.listFinal[x-1][y-1] ==  "+":
                        print("HIT!!!")
                        self.hit(x, y)
                        self.getTriesLeft()
                    else:
                        self.miss(x, y)
                        self.getTriesLeft()
                else:
                    print("You cant seek twice on the same field!")
            else:
                print("\n")
                print("Out of bounds!")
        else:
            print("No tries left! game ended")
            self.result()
            self.gameOver()
        self.checkViewableBoard()
    
    def hit(self, x, y):
        self.listFinal[x-1][y-1] = "+"
        self.listFinalViewable[x-1][y-1] = "+"
        self.mines -= 1
        self.hits += 1
        print(f"Hit at x: {x} y: {y}!")

    def miss(self, x, y):
        self.listFinal[x-1][y-1] = "-"
        self.listFinalViewable[x-1][y-1] = "-"
        self.misses += 1
        self.deductTries()
        print("You missed")

    def allowed(self):
        return self.tries > 0 and self.triesNeeded < self.x*self.y

    def getTriesLeft(self):
        print(f"Tries left {self.tries}")

    def deductTries(self):
        self.tries -= 1

    def addTries(self, x):
        self.tries += x
    
    def gameOver(self):
        del mineSweeper1
    
    def reset(self):
        del self.x
        del self.y
        del self.mines
        del self.hits
        del self.misses
        del self.triesNeeded
        del self.tries
        del self.list0
        del self.list1
        del self.list2
        del self.listFinal
        del self.listFinalViewable
    
    def result(self):
        print(f"Tries: {self.triesNeeded} | Hits: {self.hits} | Misses: {self.misses}")

def starter():
    while True:
        initialized = True
        run_user_prompt = True
        while initialized:
            try:
                size_x = int(input("Size of X [1-10]: "))
                size_y = int(input("Size of y [1-10]: "))
                tries = int(input("How many tries do you want to have? >> "))
            except ValueError:
                print("Invalid input!")
            if size_x <= 10 and size_y <= 10 and tries <= 100 and size_x >= 1 and size_y >= 1 and tries >= 1:
                print("\n")
                mineSweeper1 = Minesweeper(size_x, size_y, tries)
                mineSweeper1.create_field()
                mineSweeper1.insert_random()
                mineSweeper1.initViewableBoard()
                mineSweeper1.set_ammount_mines()
                while run_user_prompt:
                    input1 = input("[0]Seek - [1]Show board - [2]Get tries left - [3]Get status - [4]Give yourself more tries - [5]Get ammount of mines left - [6]Restart\n")
                    print("\n")
                    if input1 == "0":
                        try:
                            input2 = int(input("X: "))
                            input3 = int(input("Y: "))
                        except ValueError:
                            print("Invalid Input!")
                        if input2 <= 10 and input3 <= 10 and input2 >= 1 and input3 >= 1:
                            mineSweeper1.seek(input2, input3)
                            print("\n")
                    if input1 == "1":
                        mineSweeper1.checkViewableBoard()
                        print("\n")
                    if input1 == "2":
                        mineSweeper1.getTriesLeft()
                        print("\n")
                    if input1 == "3":
                        mineSweeper1.result()
                        print("\n")
                    if input1 == "4":
                        try:
                            input2 = int(input("Ammount of tries to add [1-1000]: "))
                        except ValueError:
                            print("Invalid input!")
                        if input2 <= 100:                
                            mineSweeper1.addTries(input2)
                        else:
                            print("Invalid ammount [1-100]!")
                    if input1 == "5":
                        mineSweeper1.get_ammount_mines()
                    if input1 == "6":
                        print("Resetting...")
                        mineSweeper1.reset()
                        run_user_prompt = False
                        initialized = False
            else:
                print("Invalid sizes!")

if __name__ == '__main__':
    starter()
