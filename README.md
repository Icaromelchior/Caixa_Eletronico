# Projeto Caixa Eletronico

# Objetivo

## Sistema de caixa eletrôni proposto no curso Python fundamentals da 4Linux

- Sistema foi proposto para o aluno aplicar oque foi passado no curso e praticar

## Sistema epenas é executado em terminal

Aplicação feita em python que simula um caixa eletrônico. A aplicação tem uma
área logada, que diferencie papéis de administrador e cliente do banco.

O administrador tem o papel de cadastrar novos clientes, desbloquear clientes e resetar senha:

- Um cliente estará bloqueado quando abrir a conta, ou errar a senha 3 vezes.
- O administrador apenas poderá desbloquear a conta
- A senha a ser definida é temporária, o cliente deverá trocá-la no primeiro login depois
  do desbloqueio.
- O cliente poderá realizar as seguintes tarefas:
- Consultar saldo
- Realizar depósito
- Realizar transferência para outra conta bancária
- Realizar saques

As operações são registradas no banco de dados sqlite3.

# Menu

menu interativo,via terminal, contyrola o fluxo da operações
e direciona para as funcionalidades da aplicação.

- O administrador enxerga apenas as ações de adminstrador
- Os clientes apenas enxerga as operações de clientes

Funções Administrativas Área dedicada ao administrador ao logar no sistema. O sistema
identifica o tipo de login realizado, e se este está habilitado a logar no sistema

- O administrador cria novos clientes
- O adminstrador desbloqueia clientes e reseta a senha

Funções do Cliente Área dedicada ao cliente do banco ao logar no sistema. O sistema
verifica se o cliente está desbloqueado para acesso.

- O cliente poderá consultar saldo
- O cliente poderá realizar saques (débito em conta)
- O cliente poderá realizar depósito (crédito em conta)
- O cliente poderá realizar transferência (débito em conta de origem, crédito em conta
  destino)
- O cliente poderá alterar a sua senha
- O cliente que errar a senha por 3 vezes consecutivas deverá ser bloqueado, logo ao
  acessar o sistema deverá aparecer a mensagem “Usuário Bloqueado. Entrar em contato
  com a Central de Atendimento”.

# Banco de Dados

A aplicação esta no Banco de dados Sqlite3 local, ja vem intslado por padrão no Python.

## para duvidas e informações entrar em contato:

- icaro_barbosa@outlook.com
