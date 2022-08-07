
#sonia@health, ShivShakti
#aniket@health, Maa Kali
#anirban@health, JaiShreeRam
print('Welcome to Health Management')
input("Enter anything to begin")
print("Please enter your username")
a = input()
def func1():
    if a =="aniket@health":
        print("Welcome aniket\n"
              "Please eneter your password")
        var1 = input()
        if var1 =="Maa Kaali":
            print("Please press 1 for retrieving your health data\n "
                  "Press 2 for adding more data")
            var2 = int(input())
            if var2 ==2:
                print('What would you like to add?\n'
                      'Press 1 for Food\n'
                      'Press 2 for Exercise')
                ab = int(input())
                if ab == 1:
                    ab1 = open("aniket_health_food", "a+")
                    print("What did you eat?")
                    aab1 = input()
                    print("At what time did you eat", aab1)
                    var3 = input()
                    ab1.write(var3)
                    ab1.write(" ")
                    ab1.write(aab1)
                    ab1.write("\n")
                    ab1.close()
                elif ab ==2:
                    with open("aniket_health_exercise") as ab2:
                        print("Which exercise did you do today?")
                        aab2 = input()
                        print("At what time did you do", aab2)
                        var4 = input()
                        ab2.write(var4)
                        ab2.write(" ")
                        ab2.write(aab2)
                        ab2.write("\n")
            elif var2 ==1:
                print("What would you like to retrieve?"
                      "Press 1 for Excercise"
                      "Press 2 for Food")
                aaa = int(input())
                if aaa ==1:
                    aaab = open("aniket_health_excercise")
                    print(aaab.read())
                if aaa ==2:
                    aaac = open("aniket_health_food")
                    print(aaac.read())


        else:
            exit("Incorrect Password\n"
                 "Exiting the programme")
    elif a =="sonia@health":
        print("Welcome back sonia\n"
              "Please enter your password")
        b = input()
        if b =="ShivShakti":
            print("Please press 1 for retrieving your health data\n "
                  "Press 2 for adding more data")
            c = int(input())
            if c ==2:
                print("What would you like to add?\n"
                      "Press 1 for food\n"
                      "Press 2 for excercise")
                d = int(input())
                if d == 1:
                    print("What did you eat today?")
                    f = input()
                    print("At what time did you eat", f)
                    var6 = input()
                    with open("sonia_health_food", "a+") as e:
                        e.write(var6)
                        e.write(" ")
                        e.write(f)
                        e.write("\n")
                elif d ==2:
                    print("What excercise did you do today?")
                    g = input()
                    print("At what time did you do", g)
                    var7 = input()
                    with open("sonia_health_excercise", "a+") as h:
                        h.write(var7)
                        h.write(" ")
                        h.write(g)
                        h.write("\n")
            elif c ==1:
                print("What would you like to retrieve?\n"
                      "Press 1 for food\n"
                      "Press 2 for excercise")
                i = int(input())
                if i ==1:
                    with open("sonia_health_food") as j:
                        print(j.read())
                elif i ==2:
                    with open("sonia_health_excercise") as k:
                        print(k.read())
        else:
            exit("Incorrect Password\n"
                 "Exiting the programme")
    elif a =="anirban@health":
        print("Welcome anirban\n"
              "Please enter your password")
        w = input()
        if w =="JaiShreeRam":
            print("Please press 1 for retrieving your health data\n "
                  "Press 2 for adding more data")
            u = int(input())
            if u ==2:
                print("What would you like to add\n"
                      "Press 1 for food\n"
                      "Press 2 for exercise")
                v = int(input())
                if v ==1:
                    with open("anirban_health_food", "a+") as n:
                        print("What did you eat today?")
                        n1 = input()
                        print("At what time did you eat", n1)
                        n2 = input()
                        n.write(n2)
                        n.write(" ")
                        n.write(n1)
                        n.write("\n")
                elif v ==2:
                    with open("anirban_health_exercise", "a+") as m:
                        print('Which excercise did you do today?')
                        m1 = input()
                        print("At what time did you do", m1)
                        m2 = input()
                        m.write(m2)
                        m.write(" ")
                        m.write(m1)
                        m.write("\n")
            elif u ==1:
                print("What would you like to retrieve?\n"
                      "Press 1 for food\n"
                      "Press 2 for excercise")
                x = int(input())
                if x ==1:
                    with open("anirban_health_food") as z:
                        print(z.read())
                elif x ==2:
                    with open("anirban_health_exercise") as l:
                        print(l.read())
        else:
            exit("Incorrect Password"
                 "Exiting the code")
    else:
        exit("Invalid username\n"
             "Exiting the programe")

func1()