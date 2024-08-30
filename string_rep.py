def a_string_rep(text):
    """Conta a quantidade de vezes que a letra 'a' (maiúscula ou minúscula) aparece na string."""

    # Converte o texto para minúsculas para contar ambas as letras 'a' e 'A'
    lower_text = text.lower()

    # Conta quantas vezes 'a' aparece no texto
    quantity = lower_text.count('a')
    
    # Verifica se a letra 'a' aparece ou não
    if quantity > 0:
        print(f"A letra 'a' aparece {quantity} vez(es) na string.")
    else:
        print("A letra 'a' não aparece na string.")

# Solicita a string ao usuário
string = input("Digite uma string para verificar a quantidade de letras 'a': ")

# Conta e exibe a quantidade de vezes que a letra 'a' aparece na string
a_string_rep(string)