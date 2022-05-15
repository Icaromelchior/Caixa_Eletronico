


users = [
  {
    'username' : 'root',
    'senha' : 'root',
    'bloqueado' : False,
    'primeiro_acesso': False,
    'tentativas_erradas': 0,
    'admin' : True,
    'id' : 0
  },
  {
    'username' : 'Icaro',
    'senha' : 'icaro',
    'bloqueado' : False,
    'primeiro_acesso': False,
    'tentativas_erradas': 0,
    'admin' : False,
    'id' : 1
  },
  {
    'username' : 'Drika',
    'senha' : 'drika',
    'bloqueado' : True,
    'primeiro_acesso': True,
    'tentativas_erradas': 0,
    'admin' : False,
    'id' : 2
  }
]

def buscar(username):
  for u in users:
    if u['username'] == username:
      return u.values()

  return None    


def salvar(usuario):
  usuario = usuario.__dict__
  usuario['id'] = usuario.pop('id',None)

  id = usuario['id']

  if id is None:
    usuario['id'] = users[-1]['id'] + 1
    users.append(usuario)

  else:
    users[id] = usuario
