def main():
    # Lendo os valores de N e K
    N, K = map(int, input().split())
    
    # Lendo a lista de nomes
    alunos = [input().strip() for _ in range(N)]
    
    # Ordenando os nomes em ordem alfabética
    alunos.sort()
    
    # Imprimindo o K-ésimo aluno (índice K-1)
    print(alunos[K - 1])

if __name__ == "__main__":
    main()
