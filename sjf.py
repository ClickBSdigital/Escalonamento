def sjf(processos):
    processos_ordenados = sorted(processos, key=lambda x: x[1])
    tempo = 0
    for nome, duracao in processos_ordenados:
        print(f"Executando {nome} ({duracao}s) – início: {tempo}s")
        tempo += duracao


tarefas = [("P1", 6), ("P2", 2), ("P3", 1)]
sjf(tarefas)
