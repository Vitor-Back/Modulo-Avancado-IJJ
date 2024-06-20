valor= int(input("Informe de qual numero quer a Tabuada de 1 a 10: "))

for i in range(10):
    total = valor * i
    print(f"[{valor}x{i}={total}]")