from collections import deque


def round_robin(processos, quantum):
    fila = deque(processos)
    while fila:
        nome, tempo = fila.popleft()

        # Executa até o limite do quantum
        exec_time = min(quantum, tempo)
        print(f"{nome} executou {exec_time}s")

        # Se ainda houver tempo, volta para o fim da fila
        if tempo - quantum > 0:
            fila.append((nome, tempo - quantum))


def time_sharing(processos, quantum):
    print("Simulação de Time Sharing:")
    round_robin(processos, quantum)


# Lista de processos (usuário, tempo total)
processos = [("User1", 4), ("User2", 6), ("User3", 5)]

# Inicia o algoritmo
time_sharing(processos, quantum=1)
