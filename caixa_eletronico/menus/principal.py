from getpass import getpass

from requests import get
from . import  admin,clientes
from ..import exeptions, usuarios

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

        try:
            u = usuarios.login(username,senha)
        
        except exeptions.Usuariobloqueado:
          print('Usuário bloqueado - entrar em contato com a central')

        except exeptions.CredenciaisInvalidas as ci:
          tentativas = ci.args[0]
          print('Credenciais inválidas')

          if tentativas > 0:
            print(f"Tentativas restantes antes do bloqueio de usuário: {3 - tentativas}")

        else:

            if u.admin:
              admin.menu_admin(u)

            else:
              clientes.menu_cliente(u)
    
    elif escolha == 'S':
      print('Obrigado por usar o caixa milionario. ')
      break

    else:
      print('Digite uma opção valida. ')

    
