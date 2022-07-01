#Dans les version récente de python 3.6 + 

prenom = "Paul"
x = f"Bonjour {prenom} !"

print(x)

a = 5
b = 10

result = f"la multiplication de {a} par {b} est égal à {a*b}"
print(result)




#On peut faire la même chose dans les anciennes version de Python

y = 2
z = 15
res = "le resultat de {} + {} est {}".format(y,z,y+z)
print(res)

n = 4
p = "{} - {truc} est égal à 2".format(n,truc=2,)
print(p)

# On peut également choisir l'odre des variables, en indiquant l'indexe dans la chaine
y,z=4,15
res = "le resultat de {2} + {1} est {0}".format(y+z,z,y)
print(res)
