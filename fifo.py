def fifo(processos):
    tempo = 0
    for nome, duracao in processos:
        print(f"Executando {nome} por {duracao}s (início: {tempo}s)")
        tempo += duracao

fila = [("P1", 4), ("P2", 2), ("P3", 6)]
fifo(fila)
