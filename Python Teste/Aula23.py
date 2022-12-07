try:
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a/b
except (ValueError, TypeError):
    print('Tivemos um problema com os tipos de dados que você digitou')
except ZeroDivisionError:
    print('Não possivel dividir um numero por Zero')
except KeyboardInterrupt:
    print('O usuário preferiu não informar os dados')
else:
    print(f'O resultado é {r}')
finally:
    print('Volte sempre! Muito obrigado!')