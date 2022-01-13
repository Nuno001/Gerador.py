nome = input('qual o seu nome')
idade = input('qual sua idade')
idade = int (idade)

idade_limite = 18


if idade >= idade_limite:
    print(f'{nome} pode pegar o emprestimo')
else:
    print(f'{nome} Não pode pegar o emprestimo!')

