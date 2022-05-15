from .. import exeptions, usuarios

def menu_admin(admin):
  opcoes = {
    'C': 'Cadastrar novo cliente',
    'D': 'Desbloquear cliente',
    'L': 'Fazer Logout'  
    }



  while True:
    print()
    print("="* 10,'MENU ADMINISTRATIVO',"=" * 10)

    for (op, descricao) in opcoes.items():
      print(f"{op} - {descricao} " )

    escolha = input('Opção: ').strip().upper()

    if escolha == 'L':
      break

    elif escolha == 'C':
      username = input('Digite o username da nova conta: ')
      cadastrar_conta(admin, username)

    elif escolha == 'D':
      username = input('Digite o username da conta bloqueada: ')
      desbloquear_conta(admin, username)

    else:
      print('Digite uma opção valida.')

def cadastrar_conta(admin,username):
  if username == '':
    print('username vazio.')
    return

  try:
      u = admin.criar(username)

  except exeptions.UsernameRepitido:
    print('Username ja esta em uso')

  else:
      u.salvar()
      print(f"Usuaário `{username}` criado com sucesso.")
      print('A senha é o próprio username')


def desbloquear_conta(admin, username):
  try:
      admin.desbloquear(username)

  except exeptions.UsuarioInexistente:
    print('Username não consta no sistema')

  else:
    print('Usuario desbloqueado com sucesso.')
    print('Senha igual username')




