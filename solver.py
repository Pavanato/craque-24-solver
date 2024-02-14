import itertools

def avaliar_expressao(expressao):
    try:
        return eval(expressao)
    except ZeroDivisionError:
        return None

def verificar_24(numeros):
    operadores = ['+', '-', '*', '/']
    permutacoes = itertools.permutations(numeros)

    for perm in permutacoes:
        for ops in itertools.product(operadores, repeat=3):
            expressao = f"(({perm[0]} {ops[0]} {perm[1]}) {ops[1]} {perm[2]}) {ops[2]} {perm[3]}"
            resultado = avaliar_expressao(expressao)
            if resultado == 24:
                return (True , expressao)

    return (False, None)

if __name__ == "__main__":
    while True:
        numeros = input("Digite 4 números separados por espaços: ").split()
        numeros = [int(num) for num in numeros]
        resultado = verificar_24(numeros)
        print("Solução encontrada") if resultado[0] else print("Nenhuma solução encontrada")
        if resultado[0] and input("Deseja ver a expressão? (s/n): ") == 's':
            print(resultado[1],)