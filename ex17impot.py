sexe=input("entrer le sexe de l'habitant ")
age=int(input("entrer l'age de l'habitant"))
a1= (age>=20 and sexe == "homme")
a2= (age>=18 and age <=35 and sexe=="femme")  
if a1 or a2 :
    print("l'habitat est imposable")
else :
    print("l'habitat n'est pas imposable")
