estudantes={}
n_estudantes=int(input("Introduza o número de estudantes:"))
for i in range(1, n_estudantes+1):
    print(f"------- Estudante {i} -------")
    nome=input(f"Nome do estudante: ")
    lista_notas=[]
    n_disciplina=int(input("Digite a quantidade de disciplinas: "))
    for j in range(1, n_disciplina+1):
        nota=float(input(f"Nota {j}: "))
        lista_notas.append(nota)
    estudantes[f"Estudante {i} {nome} "]=lista_notas
print(f"------- RESGISTRO FINAL -------")
print(estudantes)