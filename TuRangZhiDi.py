def TuRangZhiDi(clay,silt,sand):
    if clay <= 15:
        if silt < 15 and sand >= 85 and sand < 100:
            return "壤质砂土"
        if silt < 45 and sand >= 55 and sand < 85:
            return "砂质壤土"
        if silt >= 30 and silt < 45 and sand >= 40 and sand < 55:
            return "壤土"
        if silt >= 45 and silt < 100 and sand < 55:
            return "粉砂质壤土"
    elif clay > 15 and clay <= 25:
        if silt < 30 and sand >= 55 and sand < 85:
            return "砂质粘壤土"
        if silt >= 20 and silt < 45 and sand >= 30 and sand < 55:
            return "粘壤土"
        if silt >= 45 and silt < 85 and sand < 40:
            return "粉砂质粘壤土"
    elif clay > 25 and clay <= 45:
        if silt < 20 and sand >= 55 and sand < 75:
            return "砂质粘土"
        if silt < 45 and sand >= 10 and sand < 55:
            return "壤质粘土"
        if silt >= 45 and silt < 75 and sand < 30:
            return "粉砂质粘土"
    elif clay > 45 and clay < 65 and silt < 55 and sand < 55:
        return "粘土"
