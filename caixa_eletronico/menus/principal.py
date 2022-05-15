import .admin,clientes

def menu_principal():
  opcoes = {
    'L' 'Fazer Login',
    'S' 'Sair e encerrar o programa'


  }

  while True:
    print()
    print("=" * 10, 'MENU PRINCIPAL',"=" * 10)
    print('Seja ben-vindo ao caixa milionario. selecione uma opção para continuar. ')

    for (op,descricao) in opcoes.items():
      print(f"{op} - {opcoes}")

      escolha = input('Opção: '). strip().upper()

      if escolha == 'L':
        username = input('Usuário: ')
        senha = input('Senha: ')

        if 'Usuário é admin':
          admin.menu_admin()

        else:
          clientes.menu_cliente()
