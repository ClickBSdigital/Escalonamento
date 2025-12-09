

#  **README — Algoritmos de Escalonamento de CPU**

##  **Identificação**

**Alunos:**

* *Eliandro Aparecido Elias da Silva*
* *Jowilson Ribas Nunes*

**Docente:**

* *Professor Edeson Costa*

**Instituição:**

* Faculdade SENAC – MS
* Curso: *Sistemas Operacionais / Desenvolvimento de Sistemas*
* Unidade: *SENAC Hub Academy – Campo Grande - MS*

---

##  **Data**

**Data de Entrega / Registro:**
 *09 de dezembro de 2025*

---

## 🛠 **Autorização para Ajustes e Novas Demandas**

Este trabalho está **autorizado pelo docente** para receber:

✔ Atualizações
✔ Ajustes técnicos
✔ Melhorias
✔ Inserção de novas funcionalidades
✔ Complementação de conteúdo

As próximas versões devem manter o padrão acadêmico e seguir as orientações da disciplina.

---

##  **Resumo Geral do Trabalho**

Este documento apresenta os principais **algoritmos de escalonamento de CPU**, responsáveis pela ordem em que processos são executados dentro de um Sistema Operacional.

Cada algoritmo inclui:

* ✔ Explicação simples (estilo slide)
* ✔ Vantagens e desvantagens
* ✔ Código Python para simulação
* ✔ Conceitos essenciais

---

#  FIFO — *First In, First Out*

###  Resumo (slide)

* Ordem de chegada = ordem de execução
* Simples e não preemptivo
* Pode gerar atrasos se o primeiro processo for muito longo

###  Como funciona

É como uma fila de mercado: o primeiro que chega é o primeiro a ser atendido.

---

###  Código Python — FIFO

```python
def fifo(processos):
    tempo = 0
    for nome, duracao in processos:
        print(f"Executando {nome} por {duracao}s (início: {tempo}s)")
        tempo += duracao

fila = [("P1", 4), ("P2", 2), ("P3", 6)]
fifo(fila)
```

---

#  SJF — *Shortest Job First*

### Resumo (slide)

* Executa primeiro o processo mais rápido
* Reduz tempo médio de espera
* Não preemptivo
* Pode causar *starvation* (processos longos ficam esquecidos)

###  Como funciona

Os processos são ordenados pelo menor tempo estimado de execução.

---

###  Código Python — SJF

```python
def sjf(processos):
    processos_ordenados = sorted(processos, key=lambda x: x[1])
    tempo = 0
    for nome, duracao in processos_ordenados:
        print(f"Executando {nome} ({duracao}s) – início: {tempo}s")
        tempo += duracao

tarefas = [("P1", 6), ("P2", 2), ("P3", 1)]
sjf(tarefas)
```

---

#  Round Robin — *RR*

###  Resumo (slide)

* Cada processo recebe um "quantum" de tempo
* Preemptivo
* Muito justo para sistemas interativos
* Quantum pequeno demais = perda de desempenho

###  Como funciona

Cada processo roda por um pequeno intervalo e volta para o fim da fila, repetidamente.

---

###  Código Python — Round Robin

```python
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
```

---

#  Escalonamento por Prioridade

###  Resumo (slide)

* Cada processo recebe uma prioridade
* Pode ser preemptivo ou não
* Processo de maior prioridade executa primeiro
* Risco de *starvation*

###  Como funciona

A CPU escolhe sempre o processo com maior prioridade (ou menor número, dependendo da regra).

---

###  Código Python — Prioridade

```python
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
```

---

#  Escalonamento Garantido

###  Resumo (slide)

* CPU é dividida igualmente entre os processos
* Evita *starvation*
* Justo para sistemas multiusuário

###  Como funciona

Cada processo recebe uma parte igual do tempo total de execução.

---

###  Código Python — Garantido

```python
def garantido(processos, ciclos):
    n = len(processos)
    for i in range(ciclos):
        nome = processos[i % n]
        print(f"Ciclo {i+1}: {nome} recebe tempo de CPU")

processos = ["P1", "P2", "P3"]
garantido(processos, ciclos=9)
```

---

#  Escalonamento por Tempo Compartilhado (*Time Sharing*)

###  Resumo (slide)

* Versão evoluída do Round Robin
* Focado em usuários simultâneos
* Ideal para sistemas multitarefa modernos
* Tempo de CPU dividido em pequenos blocos

###  Como funciona

Cada usuário/processo recebe uma fatia repetida de CPU, garantindo fluidez multitarefa.

---

###  Código Python — Time Sharing

```python
def time_sharing(processos, quantum):
    print("Simulação de Time Sharing:")
    round_robin(processos, quantum)

processos = [("User1", 4), ("User2", 6), ("User3", 5)]
time_sharing(processos, quantum=1)
```

---

#  **Conclusão**

Este trabalho apresenta:

* Explicações claras dos principais algoritmos
* Resumos no estilo slide
* Simulações utilizando Python
* Estrutura ideal para relatório, GitHub ou apresentação

Os algoritmos demonstram como um Sistema Operacional organiza e distribui o uso da CPU, influenciando diretamente o desempenho e a experiência do usuário.


