class idkwhatiwannado:
    def __init__(self) -> None:
        self.inp = None
    
    def driver(self):
        while(True):
            print("~"*50)
            print(f"{'Welcome to your random ass dashboard' : ^50}")
            print()
            print("*"*50)
            print()
            print(f"{'what would you like to do today?' : ^50}")
            print()
            print("1) Get weather updates for the day? :3")
            print("2) Get job listings from random python website? :3")
            self.inp = input()
            if self.inp == '1':
                print('yay!')
            if self.inp == '2':
                print("yay yo")
            break;

if __name__ == '__main__':
    ob = idkwhatiwannado()
    ob.driver()