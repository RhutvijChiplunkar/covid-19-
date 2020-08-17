from covid import Covid
covid=Covid()
x=input("Enter name of the country:")
cases=covid.get_status_by_country_name(x)
for x in cases:
    print(x,":",cases[x])


