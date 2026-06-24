# Sistema de Chat Cliente-Servidor em Python utilizando Sockets TCP

## 1. Introdução

Este projeto implementa um sistema simples de comunicação em rede utilizando a arquitetura Cliente-Servidor através da linguagem Python.

O objetivo é permitir a troca de mensagens entre dois programas executados em máquinas ou processos diferentes utilizando o protocolo TCP/IP.

O projeto é composto por dois arquivos:

* `Servidor.py`
* `Cliente.py`

O servidor aguarda conexões de clientes e responde às mensagens recebidas. O cliente estabelece conexão com o servidor e inicia a comunicação.

---

# 2. Objetivos do Projeto

Este projeto tem como finalidade demonstrar conceitos fundamentais de:

* Redes de computadores
* Programação de sockets
* Comunicação Cliente-Servidor
* Protocolo TCP
* Troca de mensagens em tempo real
* Manipulação de fluxos de entrada e saída
* Tratamento de exceções

Além disso, o projeto serve como base para aplicações mais complexas como:

* Chats online
* Sistemas distribuídos
* Jogos multiplayer
* Sistemas de monitoramento
* Aplicações web

---

# 3. Conceitos Teóricos

## 3.1 Arquitetura Cliente-Servidor

A arquitetura Cliente-Servidor é um modelo de comunicação onde existem dois participantes:

### Servidor

É o programa responsável por:

* Ficar aguardando conexões
* Receber solicitações
* Processar informações
* Enviar respostas

### Cliente

É o programa responsável por:

* Iniciar a conexão
* Enviar solicitações
* Receber respostas

Fluxo:

```
Cliente ---------> Servidor
        Solicitação

Cliente <--------- Servidor
          Resposta
```

---

## 3.2 O que é um Socket?

Socket é uma interface utilizada para comunicação entre processos através de uma rede.

Pode ser entendido como um "canal de comunicação".

Cada socket é identificado por:

* Endereço IP
* Porta

Exemplo:

```
IP: 127.0.0.1
Porta: 12345
```

---

## 3.3 Endereço IP

O endereço IP identifica um dispositivo na rede.

Neste projeto utilizamos:

```
127.0.0.1
```

Também conhecido como:

* localhost
* loopback

Representa a própria máquina.

Ou seja:

Cliente e servidor executam no mesmo computador.

---

## 3.4 Porta

A porta identifica um serviço dentro do computador.

Exemplo:

| Serviço    | Porta |
| ---------- | ----- |
| HTTP       | 80    |
| HTTPS      | 443   |
| FTP        | 21    |
| Nosso Chat | 12345 |

Neste projeto utilizamos:

```python
porta = 12345
```

---

## 3.5 TCP

TCP significa:

Transmission Control Protocol

É um protocolo orientado à conexão.

Características:

* Entrega garantida
* Dados chegam na ordem correta
* Controle de erros
* Comunicação confiável

Por isso é ideal para chats.

---

# 4. Estrutura do Projeto

```
ProjetoChat/

│
├── Servidor.py
│
├── Cliente.py
│
└── README.md
```

---

# 5. Funcionamento Geral

## Etapa 1

Servidor inicia.

```
Servidor iniciado...
```

---

## Etapa 2

Servidor fica aguardando conexão.

```
Aguardando conexão...
```

---

## Etapa 3

Cliente é executado.

---

## Etapa 4

Cliente conecta ao servidor.

```
Conectado ao servidor
```

---

## Etapa 5

Cliente envia mensagem.

```
Você: Olá
```

---

## Etapa 6

Servidor recebe.

```
Cliente: Olá
```

---

## Etapa 7

Servidor responde.

```
Sua resposta: Tudo bem?
```

---

## Etapa 8

Cliente recebe.

```
Servidor: Tudo bem?
```

---

## Etapa 9

O processo se repete até alguém digitar:

```
SAIR
```

---

# 6. Explicação Detalhada do Servidor

## Importação da biblioteca

```python
import socket
```

Importa o módulo responsável pela comunicação em rede.

---

## Criação do socket

```python
socket.socket(
    socket.AF_INET,
    socket.SOCK_STREAM
)
```

### AF_INET

Define uso de IPv4.

### SOCK_STREAM

Define uso do protocolo TCP.

---

## Associação da porta

```python
servidor.bind(("0.0.0.0", porta))
```

Permite que o servidor escute conexões.

### 0.0.0.0

Significa:

Aceitar conexões vindas de qualquer endereço IP.

---

## Iniciando escuta

```python
servidor.listen(1)
```

Coloca o servidor em modo de espera.

O número 1 representa:

Quantidade máxima de conexões pendentes.

---

## Aceitando conexão

```python
socket_cliente, endereco = servidor.accept()
```

O servidor fica bloqueado até algum cliente conectar.

Quando isso ocorre:

* socket_cliente → canal de comunicação
* endereco → IP do cliente

---

## Leitura da mensagem

```python
mensagem_recebida = entrada.readline().strip()
```

Recebe mensagem enviada pelo cliente.

---

## Exibição da mensagem

```python
print(f"\nCliente: {mensagem_recebida}")
```

Mostra a mensagem recebida.

---

## Envio da resposta

```python
saida.write(mensagem_enviada + "\n")
saida.flush()
```

Envia resposta ao cliente.

### flush()

Força o envio imediato dos dados.

Sem ele os dados podem permanecer em buffer.

---

# 7. Explicação Detalhada do Cliente

## Criação da conexão

```python
cliente.connect(
    (endereco_servidor, porta)
)
```

Solicita conexão com o servidor.

---

## Envio de mensagens

```python
saida.write(mensagem_enviada + "\n")
saida.flush()
```

Envia a mensagem digitada pelo usuário.

---

## Recebimento de mensagens

```python
mensagem_recebida = entrada.readline().strip()
```

Recebe resposta enviada pelo servidor.

---

## Encerramento

Quando usuário digita:

```text
SAIR
```

A conexão é encerrada.

---

# 8. Tratamento de Exceções

Utilizamos:

```python
try:
    ...
except Exception as e:
```

Objetivo:

Evitar que o programa seja encerrado abruptamente.

Exemplos de erros tratados:

* Servidor desligado
* Porta ocupada
* Falha de conexão
* Problemas de rede

---

# 9. Fluxograma Simplificado

## Servidor

```
Início
   |
Criar Socket
   |
Bind
   |
Listen
   |
Accept
   |
Receber Mensagem
   |
Responder
   |
Mensagem = SAIR?
   |
 Sim ---------> Encerrar
   |
 Não
   |
Volta ao início do loop
```

---

## Cliente

```
Início
   |
Conectar
   |
Enviar Mensagem
   |
Receber Resposta
   |
Mensagem = SAIR?
   |
 Sim ---------> Encerrar
   |
 Não
   |
Volta ao início do loop
```

---

# 10. Como Executar o Projeto

## Requisitos

* Python 3.8 ou superior

Verificar instalação:

```bash
python --version
```

ou

```bash
python3 --version
```

---

## Passo 1

Criar os arquivos:

```text
Servidor.py
Cliente.py
```

---

## Passo 2

Copiar os códigos para seus respectivos arquivos.

---

## Passo 3

Abrir dois terminais.

---

## Passo 4

No primeiro terminal executar:

```bash
python Servidor.py
```

Saída esperada:

```text
Servidor iniciado. Aguardando conexão na porta 12345...
```

---

## Passo 5

No segundo terminal executar:

```bash
python Cliente.py
```

Saída esperada:

```text
Conectado ao servidor no endereço 127.0.0.1
```

---

## Passo 6

Começar a conversar.

Exemplo:

### Cliente

```text
Você: Olá
```

### Servidor

```text
Cliente: Olá
Sua resposta: Tudo bem?
```

### Cliente

```text
Servidor: Tudo bem?
```

---

## Passo 7

Para encerrar:

Digite:

```text
SAIR
```

em qualquer um dos lados.

---

# 11. Possíveis Melhorias

Este projeto pode evoluir para:

### Múltiplos clientes

Utilizando:

```python
threading
```

ou

```python
asyncio
```

---

### Interface gráfica

Utilizando:

* Tkinter
* PyQt
* Kivy

---

### Comunicação em rede real

Substituindo:

```python
127.0.0.1
```

pelo IP da máquina servidora.

---

### Criptografia

Utilizando:

* SSL/TLS
* OpenSSL

---

### Histórico de mensagens

Salvando conversas em:

* TXT
* CSV
* Banco de Dados

---

# 12. Conclusão

Este projeto demonstra de forma prática como funciona a comunicação Cliente-Servidor utilizando sockets TCP em Python.

Durante o desenvolvimento são aplicados conceitos fundamentais de redes de computadores, incluindo IP, portas, protocolos de transporte, conexões TCP e troca de mensagens entre processos.

Apesar de simples, este projeto representa a base de sistemas muito utilizados atualmente, como chats online, aplicações web, serviços distribuídos e sistemas de comunicação em tempo real.
