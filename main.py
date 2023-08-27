def verificaPrimo(numero):
    if numero > 1:
        for x in range(2, numero):  # Começando de 2, pois não precisamos verificar divisão por 1
            if numero % x == 0:
                print(f"{numero} não é primo.")
                break
            else:
                print(f"{numero} é primo.")
    else:
        print("Número inválido.")




if __name__ == '__main__':
    verificaPrimo(1)


