def fibonacci(number):
    """Verifica se o número está na sequência de Fibonacci."""
    if number < 0:
        return False

    # Começa com os dois primeiros números da sequência
    a, b = 0, 1

    # Gera a sequência até encontrar o número ou ultrapassá-lo
    while a <= number:
        if a == number:
            return True
        a, b = b, a + b

    return False

# Pede ao usuário um número
number = int(input("Digite um numero para verificar se pertence a sequência de Fibonacci: "))

# Verifica se o número pertence à sequência e imprime o resultado
if fibonacci(number):
    print(f"O número {number} pertence a sequência de Fibonacci.")
else:
    print(f"O número {number} não percente a sequência de Fibonacci.")