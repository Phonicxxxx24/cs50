def checks(s):
    result = ''
    for i in s:
        if (i.isupper()):
            result += "_" + i.lower()
        elif(not i.isupper()):
            result += i
    return(result)
            

# checks("jainHarshit")
