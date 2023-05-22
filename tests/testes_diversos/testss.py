


for num in range(1,151,1):
    multiplo_de_3 = num / 3
    multiplo_de_5 = num / 5
 
    if int(multiplo_de_3) == multiplo_de_3:
        print(multiplo_de_3, num, " Harpia")
    if int(multiplo_de_5) == multiplo_de_5:
        print(multiplo_de_5, num, " Tech")
    if int(multiplo_de_3) == multiplo_de_3 and int(multiplo_de_5) == multiplo_de_5:
        print("Harpia Tech")