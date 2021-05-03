# Gerenciador de contatos
 Se trata de um gerenciador de contatos feito em **Python** utilizando **banco de dados MySQL**.
 Era inicialmente um projeto que fiz na disciplina de Pensamento Computacional na universidade que depois que aprendi sobre Banco de dados resolvi implementá-lo no projeto.

![image](https://user-images.githubusercontent.com/50207805/116932275-6ce49d80-ac38-11eb-85a7-ec4bc4031847.png)


## Como usar 
***
Você deve:
1. Clonar este repositório ou baixar os arquivos dele
2. Importar o banco de dados `Dump20210503.sql` no seu servidor MySQL ([Como?](https://ajuda.hostnet.com.br/importacao-do-banco-via-mysql-workbench/))
3. Alterar as informações do servidor MySQL

### Como alterar informações do servidor MySQL?
No arquivo `Gerenciador de contatos com Banco de dados em Python.py`, na função `def iniciaConexao():` você deve alterar as informações do servidor (`host`, `user` e `password`) MySQL que você esta usando.

```
def iniciaConexao(): #Pronta
    global con
    global cursor
    
    #Altere as informações do seu servidor MySQL aqui
    con = mysql.connector.connect(host='localhost', database='contatos', user='root', password='suaSenha')
    cursor = con.cursor()
```

## Requisitos
***
São os presentes no arquivo `requirements.txt` que são:
```
appdirs==1.4.4
asgiref==3.3.4
distlib==0.3.1
Django==3.2
filelock==3.0.12
mysql-connector-python==8.0.24
protobuf==3.15.8
pytz==2021.1
six==1.15.0
sqlparse==0.4.1
virtualenv==20.4.4
```
