import random
def cal(YDFDDYFZ):
    if YDFDDYFZ >=92:
        return "1"
    elif YDFDDYFZ>=84:
        return "2"
    elif YDFDDYFZ >=76:
        return "3"
    elif YDFDDYFZ >=68:
        return "4"
    elif YDFDDYFZ>=60:
        return "5"
    elif YDFDDYFZ >=52:
        return "6"
    elif YDFDDYFZ >=44:
        return "7"
    elif YDFDDYFZ >=36:
        return "8"
    elif YDFDDYFZ >=28:
        return "9"
    else:
        return "10"

if __name__ == "__main__":
   
   cbb = random.randint(1,100)
   b = cal(cbb)
   print("分值",cbb,"    级别",b)