global apa
apa = "apa"

def la():
    global apa
    stri = " papa is a good man "
    stri = stri.replace(apa," ")
    print(stri)
    apa = "good"

la()
la()
    
