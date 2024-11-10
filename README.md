# Lista de Chamada (Beecrowd - Problema 2137)

## Descrição
Tia Joana quer sortear um aluno para receber um bônus especial em sua nota final. Ela sorteou um número K, e o aluno premiado é o **K-ésimo** aluno da lista de chamada, que está organizada em **ordem alfabética**. Porém, Tia Joana esqueceu seu diário de classe, então ela não tem como saber quem é o aluno correspondente a esse número.

Os alunos estão ansiosos para saber o resultado, e sua tarefa é ajudar a professora a determinar o nome do aluno sorteado.

## Entrada
- A primeira linha contém dois inteiros **N** e **K** (1 ≤ K ≤ N ≤ 100), onde:
  - **N** é o número de alunos.
  - **K** é o número sorteado.
- As próximas **N linhas** contêm os nomes dos alunos (uma string de tamanho mínimo 1 e máximo 20), compostos apenas por letras minúsculas de 'a' a 'z'.

## Saída
- O programa deve imprimir uma única linha contendo o nome do aluno que deve receber o bônus.

## Exemplos de Entrada e Saída
### Exemplo 1
**Entrada:**
```
5 1
maria
joao
carlos
vanessa
jose
```
**Saída:**
```
carlos
```

### Exemplo 2
**Entrada:**
```
5 5
maria
joao
carlos
vanessa
jose
```
**Saída:**
```
vanessa
```

### Exemplo 3
**Entrada:**
```
5 3
maria
joao
carlos
vanessa
jose
```
**Saída:**
```
jose
```

## Lógica Utilizada
1. **Leitura dos dados de entrada**:
   - Lemos os valores de **N** e **K**.
   - Em seguida, lemos a lista de **N nomes**.

2. **Ordenação dos nomes em ordem alfabética**:
   - Utilizamos a função `sorted()` para classificar a lista de nomes.

3. **Seleção do K-ésimo aluno**:
   - Lembrando que o índice em Python começa em zero, o K-ésimo aluno será acessado com o índice `K-1`.

## Implementação em Python
```python
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
```

## Explicação do Código
1. **Leitura e entrada**:
   - Utilizamos `input().split()` para ler os inteiros **N** e **K**.
   - Usamos uma list comprehension para ler os **N nomes** e armazená-los em uma lista chamada `alunos`.

2. **Ordenação**:
   - A lista `alunos` é ordenada em ordem alfabética com o método `.sort()`.

3. **Saída**:
   - Como o índice em Python começa em zero, o K-ésimo aluno na lista ordenada é acessado com o índice `K-1`.

## Complexidade
- A complexidade para ordenar a lista é **O(N log N)**, o que é eficiente para os valores máximos de **N = 100**.
- A leitura e a seleção do K-ésimo aluno são **O(1)**.

## Como Executar
1. Salve o código em um arquivo, por exemplo, `lista_chamada.py`.
2. Abra o terminal e execute:
   ```bash
   python3 lista_chamada.py
   ```
3. Insira os valores conforme o exemplo fornecido.

## Notas Finais
Este problema é um bom exemplo de como utilizar **ordenação** para resolver problemas de classificação em listas. Além disso, reforça a importância de lidar com **índices** corretamente em linguagens como Python.
