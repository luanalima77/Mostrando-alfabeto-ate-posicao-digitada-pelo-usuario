# Função para retornar um array com todas as letras do alfabeto até a posição que foi digitada.
# Exemplo: se o usuário digitou o número 8, será mostrado um array com todas as letras do alfabeto até essa posição.
def retornar_array_alfabeto(numero):
    alfabeto = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

    # O número digitado deve ir de 1 a 26 (índices das letras do alfabeto).
    # Coloquei ele fora do for e do if dentro do for porque, se ele for True, ele já retorna a mensagem e sai da função, economizando tempo de execução. 
    if numero < 1 or numero > 26:
        return "Número inválido!"
    
    # Se o número digitado for válido, a lista é percorrida e o array com as letras é criado.
    for indice, letra in enumerate(alfabeto):
        if indice + 1 == numero and numero > 0 and numero < 27:
            lista = alfabeto[0:numero]
            return lista

# Inserção do número pelo usuário.
numero_digitado = int(input("Digite um número de 1 a 26: "))

# Mostrando o resultado na tela, com base no que o usuário digitou.
print(retornar_array_alfabeto(numero_digitado))