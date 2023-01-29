def create_set(s):
    set_returned=set()
    for obj in s.split(','):
        set_returned.add(obj.strip())
    return set_returned

set_mama=create_set(input("Lista mamei: "))
set_ana=create_set(input("Obiectele Anei: "))
set_maria=create_set(input("Obiectele Marieri: "))

#Ce s-a cumparat in total - Reuniune set_ana si set_maria
set_cumparaturi=set_ana | set_maria
print("") 
print("S-au cumparat: ",set_cumparaturi)
print("")

#Ce mai e de cumparat - Diferenta intre set_mama si set_cumparaturi
set_rest_cumparaturi=set_mama - set_cumparaturi #set_mama.difference(set_cumparaturi)
if set_rest_cumparaturi == set():
    print("Nu mai e nimic de cumparat")
    print("")
else:
    print("Mai avem de cumparat: ",set_rest_cumparaturi)
    print("")

#Ce s-a cumparat in plus - Diferenta intre set_cumparaturi si set_mama
set_cumparat_plus=set_cumparaturi - set_mama
if set_cumparat_plus==set():
    print("Nu s-a cumparat nimic in plus")
    print("")
else:
    print("S-au cumparat in plus: ",set_cumparat_plus)
    print("")

#Ce s-a cumparat dublu - Intersectia dintre set_ana si set_maria
set_dublu = set_ana & set_maria
if set_dublu == set():
    print("Nu s-au cumparat dubluri")
    print("")
else:
    print("Obiecte duplicate: ", set_dublu)
    print("")

#Ce a cumparat Ana din lista mamei - Intersectia dintre set_mama si set_ana
ana_set_cumparat_din_lista_mama = set_ana & set_mama
if ana_set_cumparat_din_lista_mama == set():
    print("Ana nu a cumparat nimic din lista mamei")
    print("")
else:
    print("Ana a cumparat din lista mamei: ",ana_set_cumparat_din_lista_mama)
    print("")

# Ce a cumparat Ana in plus fata de lista mamei - Diferenta intre set_ana si set_mama
ana_set_cumparat_plus = set_ana - set_mama
if ana_set_cumparat_plus == set():
    print("Ana nu a cumparat nimic in plus din lista mamei")
    print("")
else:
    print("Ana a cumparat in plus: ", ana_set_cumparat_plus)
    print("")

#Ce a cumparat Maria din lista mamei - Intersectia dintre set_mama si set_maria
maria_set_cumparat_din_lista_mama = set_maria & set_mama
if maria_set_cumparat_din_lista_mama == set():
    print("Maria nu a cumparat nimic din lista mamei")
    print("")
else:
    print("Maria a cumparat din lista mamei: ",maria_set_cumparat_din_lista_mama)
    print("")

## Ce a cumparat Maria in plus fata de lista mamei - Diferenta intre set_maria si set_mama
maria_set_cumparat_plus = set_maria - set_mama
if maria_set_cumparat_plus == set():
    print("Maria nu a cumparat nimic in plus din lista mamei")
    print("")
else:
    print("Maria a cumparat in plus: ", maria_set_cumparat_plus)
    print("")


