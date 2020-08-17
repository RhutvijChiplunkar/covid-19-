from covid import Covid
covid=Covid()
print(covid.list_countries())
for i in covid.list_countries():
    L=[]
    for x,y in i.items():
        L.append(y)
    print("id:",L[0])
    print("country:",L[1])
