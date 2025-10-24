# Hacktoberfest 2025 - Desafio de Padrão
# Criado por: Débora Martins
# Desenha uma pirâmide invertida de números e estrelas

def piramide_invertida(n):
    for i in range(n, 0, -1):
        linha = ''
        for j in range(1, i + 1):
            if j % 2 == 0:
                linha += '*'
            else:
                linha += str(j)
        print(linha)

# Exemplo com 6 linhas
piramide_invertida(6)
