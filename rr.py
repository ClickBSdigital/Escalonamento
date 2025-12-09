from collections import deque


def round_robin(processos, quantum):
    fila = deque(processos)
    while fila:
        nome, tempo = fila.popleft()
        if tempo > quantum:
            print(f"{nome} executa {quantum}s (resta {tempo - quantum}s)")
            fila.append((nome, tempo - quantum))
        else:
            print(f"{nome} finaliza executando {tempo}s")


processos = [("P1", 5), ("P2", 3), ("P3", 7)]
round_robin(processos, quantum=2)
