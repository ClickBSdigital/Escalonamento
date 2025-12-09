def garantido(processos, ciclos):
    n = len(processos)
    for i in range(ciclos):
        nome = processos[i % n]
        print(f"Ciclo {i+1}: {nome} recebe tempo de CPU")


processos = ["P1", "P2", "P3"]
garantido(processos, ciclos=9)
