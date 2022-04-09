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
            self.inp = input()
            if self.inp == '1':
                print('yay!')
            break;

if __name__ == '__main__':
    ob = idkwhatiwannado()
    ob.driver()
