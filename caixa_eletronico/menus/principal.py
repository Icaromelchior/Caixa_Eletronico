from getpass import getpass

from requests import get
from . import  admin,clientes

def menu_principal():
  opcoes = {
      'L': 'Fazer Login',
      'S': 'Sair e encerrar o programa'


  }

  while True:
    print()
    print("=" * 10, 'MENU PRINCIPAL',"=" * 10)
    print('Seja ben-vindo ao caixa milionario. selecione uma opção para continuar. ')

    for (op, descricao) in opcoes.items():
      print(f"{op} - {descricao}")

    escolha = input('Opção: ').strip().upper()

    if escolha == 'L':
        username = input('Usuário: ')
        senha = getpass('Senha: ')

        if 'Usuário é admin':
          admin.menu_admin()

        else:
          clientes.menu_cliente()
    
    elif escolha == 'S':
      print('Obrigado por usar o caixa milionario. ')
      break

    else:
      print('Digite uma opção valida. ')

    
