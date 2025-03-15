import geometria as g

def menu():
    print("calculadora geometrica")
    print("1 - area do Circulo")
    print("2 - perimetro do Circulo")
    print("3 - area do Retangulo")
    print("4 - perimetro do Retangulo")
    print("5 - area do Triangulo")
    print("6 - perimetro do Triangulo")
    print("0 - sair")
    
while True:
    menu()
    opcao = int(input("escolha uma opcao: "))

    if opcao == 1:
        raio = float(input("raio: "))
        print(f"area: {g.areaCirculo(raio)}")

    elif opcao == 2:
        raio = float(input("raio: "))
        print(f"perimetro: {g.perimetroCirculo (raio)}")

    elif opcao == 3:  
        base = float(input("base: "))
        altura = float(input("altura "))
        print(f"area: {g.areaRentangulo (base, altura)}")

    elif opcao == 4:  
        base = float(input("base: "))
        altura = float(input("altura "))
        print(f"perimetro: {g.perimetroRetangulo (base, altura)}")    
 
    elif opcao == 5:  
        base = float(input("base: "))
        altura = float(input("altura "))
        print(f"area: {g.areaTriangulo (base, altura)}")

    elif opcao == 6:  
        lado1 = float(input("lado1 "))
        lado2 = float(input("lado2 "))
        lado3 = float(input("lado3 "))
        print(f"area: {g.perimetroTriangulo (lado1,lado2,lado3)}")

    elif opcao == 0:
        print("saindo")
        break