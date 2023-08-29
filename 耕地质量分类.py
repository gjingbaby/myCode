#坡度
def PD(PDJB):
    if PDJB == "1":
        return "≤2°"
    elif PDJB == "2":
        return "2°～6°"
    elif PDJB == "3":
        return "6°～15°"
    elif PDJB == "4":
        return "15°～25°"
    elif PDJB == "5":
        return "＞25°"

#耕地级别
def GDJB(GDEJL):
    if GDEJL == "水田":
        return "1"
    elif GDEJL == "水浇地":
        return "2"
    elif GDEJL == "旱地":
        return "3"

#土层厚度级别
def TCHDJB(TCHD):
    if float(TCHD) >= 100:
        return "1"
    elif float(TCHD) >= 60 and float(TCHD) < 100:
        return "2"
    elif float(TCHD) < 60:
        return "3"

#土壤质地级别
#!/usr/bin/python
# coding=UTF-8

def TRZDJB(TRZD):
    YIJI = [u"壤土",u"砂壤",u"轻壤",u"中壤",u"粉黏壤",u"黏壤",u"砂黏壤",u"粉壤",u"粉土",u"砂黏壤"]
    ERJI = [u"黏土",u"重壤",u"粉黏土",u"砂黏土",u"壤黏土",u"砂黏土"]
    SANJI= [u"砂土",u"紧砂土",u"松砂土",u"砂壤",u"壤砂土"]
    if TRZD in YIJI:
        return "1"
    elif TRZD in ERJI:
        return "2"
    elif TRZD in SANJI:
        return "3"
    
#土壤有机质含量
def TRYJZHLJB(TRYJZHL):
    if float(TRYJZHL) >= 20:
        return "1"
    elif float(TRYJZHL) >= 10 and float(TRYJZHL) < 20:
        return "2"
    elif float(TRYJZHL) < 10:
        return "3"
    


#土壤PH
def TRPHZJB(TRPHZ):
    if float(TRPHZ) >= 8.5:
        return "3b"
    elif float(TRPHZ) >= 7.5 and float(TRPHZ) < 8.5:
        return "2b"
    elif float(TRPHZ) >= 6.5 and float(TRPHZ) < 7.5:
        return "10"
    elif float(TRPHZ) >= 5.5 and float(TRPHZ) < 6.5:
        return "2a"
    elif float(TRPHZ) < 5.5:
        return "3a"