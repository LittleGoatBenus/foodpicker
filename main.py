import random


opt = []

run = True

while run:
    print("type stop when you have listed everything")
    inp = input(("whats in house "))
    opt.append(inp)

    if inp == "stop":
        opt.pop(-1)
        run = False
        print("in house", opt)
        print("you will be eating",random.choice(opt))
