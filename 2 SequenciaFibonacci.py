def pertence_fibonacci(n):
    if n < 0:
        return False
        
    a = 0;b = 1; aux=0 
   
    if n == a or n == b:  # Verifica se o número é 0 ou 1, que são os primeiros da sequência
        return True

    while b < n:
        aux = a
        a = b
        b = aux+b

        if b == n:
            return True
        print(b)

    return False

num = int(input("Digite um número: "))

if pertence_fibonacci(num):
    print("Pertence a sequência")
else:
    print("Não pertence a sequência")