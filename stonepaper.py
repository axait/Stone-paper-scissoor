# stone/paper=paper
# stone/scissor=stone
# paper/scissor=scissor
import random,os,time
def welcome():
    print("""
    █┼┼┼█ ███ █┼┼ ███ ███ █▄┼▄█ ███ ┼┼ █┼█ ███ ███ ███
    █┼█┼█ █▄┼ █┼┼ █┼┼ █┼█ █┼█┼█ █▄┼ ┼┼ █▄█ █▄┼ █▄┼ █▄┼
    █▄█▄█ █▄▄ █▄█ ███ █▄█ █┼┼┼█ █▄▄ ┼┼ █┼█ █▄▄ █┼█ █▄▄

    Loading ...""")

def banner():
    print("""
██ ███ ███ █╬╬█ ██ ╬╬ ███ ███ ███ ██ ███/ ██ ██ █ ██ ██ ███ ███
█▄ ╬█╬ █╬█ ██▄█ █▄ ╬╬ █▄█ █▄█ █▄█ █▄ █▄╬/ █▄ █╬ █ █▄ █▄ █╬█ █▄╬
▄█ ╬█╬ █▄█ █╬██ █▄ ╬╬ █╬╬ █╬█ █╬╬ █▄ █╬█/ ▄█ ██ █ ▄█ ▄█ █▄█ █╬█
    """)


def menu():
    print("""
Options in this game are :
    1.stone
    2.paper
    3.scissor
    """)
    
def compchoice():
    options=['paper','scissor','stone']
    choice1=random.choice(options)
    choice2=random.choice(options)
    choice3=random.choice(options)
    choicestring=choice1+" "+choice2+" "+choice3
    choiceslist=choicestring.split()
    # print(choicestring)
    finalchoice=random.choice(choiceslist)
    return finalchoice


def ucinput():
    option=['paper','scissor','stone']
    print("Enter your choice :")
    user=input()
    user=user.lower()
    print("")
    computer=compchoice()
    print("Computer choice is :")
    print(computer)
    return user,computer

def defeat():
    print("""
          
     /‾‾\\
    (#`_´)
    <,><╦╤─ ҉ - -
    /‾‾\\
    """)

    
def win():
    print("""
    █┼┼┼█ ███ █┼┼█
    █┼█┼█ ┼█┼ ██▄█
    █▄█▄█ ▄█▄ █┼██
    """)


def check(user,comp):
    print("")
    if (user=='paper' and comp=='stone')or(user=='stone' and comp=='scissor')or(user=='scissor' and comp=='paper'):
        print(f'----------YOU WIN with {user}-----------');win()
    # if (user=='stone' and comp=='scissor'):
    #     print(f'----------YOU WIN with {user}-----------')
    # if (user=='scissor' and comp=='paper'):
    #     print(f'----------YOU WIN with {user}-----------')
    if (comp=='paper' and user=='stone')or(comp=='stone' and user=='scissor')or(comp=='scissor' and user=='paper'):
        print(f'----------COMPUTER WIN with {comp}-----------');defeat()
    # if (comp=='stone' and user=='scissor'):
    #     print(f'----------COMPUTER WIN with {comp}-----------')
    # if (comp=='scissor' and user=='paper'):
    #     print(f'----------COMPUTER WIN with {comp}-----------')
    if user==comp:
        print("Match has draw")
    if user!='paper' or user!='paper' or user!='paper':
        print("")
        print("NOTE:")
        print("Enter option from menu")
    print("")
    print("")

def main():
    welcome()
    time.sleep(2)
    os.system('cls')
    banner()
    while True:
        menu()
        u,c=ucinput()
        check(u,c)
if __name__=='__main__':
    main()
    