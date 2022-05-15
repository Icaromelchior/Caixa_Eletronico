
from .bd import usuarios
from .import exeptions


from webbrowser import get


class Usuarios:
  def __init__(self, username,senha,bloqueado=True,
              tentativas_erradas=0,primeiro_acesso=True,admin=False,id=None):
      self.id = id
      self.username = username
      self.senha = senha
      self.bloqueado = bloqueado
      self.primeiro_acesso = primeiro_acesso
      self.tentativas_erradas = tentativas_erradas
      self.admin = admin

  def salvar(self):
    usuarios.salvar(self)



class Administrador(Usuarios):
  def __init__(self,username,senha,id=None):
    super() .__init__(username, senha,False,False,admin=True,id=id)


  def criar(self,username):

      if usuarios.buscar(username) is not None:
       raise exeptions.UsernameRepitido

      return Cliente(username, username)



  def desbloquear(self,username):

      user_data = usuarios.buscar(username)

      if user_data is None:
        raise exeptions.UsuarioInexistente

      u = Usuarios(*user_data)
      u.senha = u.username
      u.bloqueado = False
      u.primeiro_acesso = True
      u.tentativas_erradas = 0
      u.salvar()



class Cliente(Usuarios):
  def get_saldo(self):
    pass

  def sacar(self,quantia):
    pass

  def depositar(self,quantia):
    pass

  def transferiar(self,quantia,destinatario):
    pass

def login(username,senha):
  user_data = usuarios.buscar(username)

  if user_data is None:
    raise exeptions.CredenciaisInvalidas(-1)

  u = Usuarios(*user_data)

  if u.bloqueado:
    raise exeptions.Usuariobloqueado

  if senha != u.senha:
    u.tentativas_erradas += 1

    if u.tentativas_erradas == 3:
      u.bloqueado = True

      u.salvar()  
      raise exeptions.CredenciaisInvalidas(u.tentativas_erradas)

  if u.admin:
    u = Administrador (u.username,u.senha,u.id)

  else:
    u = Cliente(*user_data)


  u.tentativas_erradas = 0 
  u.salvar()
  return u

