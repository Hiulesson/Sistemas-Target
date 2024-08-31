frase = "Meu primeiro estagio, assim espero, amem"
aux = ""

# Loop que percorrer de trás pra frente
for i in range(len(frase) - 1, -1, -1):
    aux += frase[i]

print(aux)