if __name__ == '__main__':
    student = []
    note = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        student.append([name, score])
        student = sorted(student)
        note.append(score)
        note = sorted(list(set(note)))
    for i in student:
        if i[1] == note[1]:
            print(i[0])



    print(note)
    print(student)

# verificar as notas e pegar a segunda nota imprimindo o nome do aluno
# se houver mais de 1 aluno imprimir os nomes por ordem alfabetica


