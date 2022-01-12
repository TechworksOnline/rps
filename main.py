# RSP
import random


def main():
    modec = None
    while not modec:
        modec = clean("m", input("Choose from modes: (e)asy, (h)ard or (n)ormal: \n"))
    print(modec, "mode chosen")
    print("use d to select a different difficulty at any time")
    mchoice(modec)


def mchoice(modec):
    uchoice = None
    while not uchoice:
        uchoice = clean("c", input("Choose from: (r)ock, (p)aper or (s)cissors: \n"))
    cpuchoice = cpupick(modec, uchoice)
    print("You have chosen", uchoice)
    print("CPU has chosen", cpuchoice)
    compres = compare(cpuchoice, uchoice)
    print("You", compres)
    score(compres)
    print("NEXT GAME! ")
    mchoice(modec)
    main()


def clean(s, c):
    w = rps if s == "c" else mode
    if c == "d":
        main()
    if c not in w:
        print("Not a valid choice, please ")
        return
    if w.index(c) > 2:
        c = w[w.index(c) - 3]
    return c


def cpupick(modec, uchoice):
    r = None
    cs = None
    #comment for git
    if modec == "easy":
        while r != "Win":
            cs = random.choice(rps[:3])
            r = compare(cs, uchoice)
        return cs
    if modec == "hard":
        while r != "lose" and r != "tie":
            cs = random.choice(rps[:3])
            r = compare(cs, uchoice)
        return cs
    if modec == "normal":
        return random.choice(rps[:3])


def compare(c, h):
    if c == h:
        return "tie"
    if rps.index(c) == (rps.index(h)-1) or ((rps.index(c) == 2) and (rps.index(h) == 0)):
        return "Win"
    else:
        return "lose"


def score(sc):
    global user
    global computer
    if sc == "Win":
        user += 1
    elif sc != "tie":
        computer += 1
    print(f'Score is\nyou {user} to the computer: {computer}')


user = 0
computer = 0
rps = "rock", "paper", "scissors", "r", "p", "s"
mode = "easy", "hard", "normal", "e", "h", "n"

if __name__ == '__main__':
    main()
