def prioridade(processos):
    fila = sorted(processos, key=lambda x: x[2])
    for nome, duracao, prioridade in fila:
        print(f"Executando {nome} (prioridade {prioridade}) por {duracao}s")


processos = [
    ("P1", 4, 3),
    ("P2", 2, 1),
    ("P3", 5, 2),
]
prioridade(processos)
