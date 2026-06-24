# Chat Cliente-Servidor com Sockets TCP em Python

## Descrição

Este projeto implementa um sistema simples de comunicação Cliente-Servidor utilizando a linguagem Python e o protocolo TCP/IP através de sockets.

O servidor aguarda conexões de clientes e responde às mensagens recebidas, enquanto o cliente estabelece a conexão e inicia a troca de mensagens.

## Conceitos Utilizados

* Redes de Computadores
* Arquitetura Cliente-Servidor
* Sockets
* Protocolo TCP
* Endereço IP e Portas
* Comunicação em tempo real
* Tratamento de exceções

## Estrutura do Projeto

```text
Projeto_Redes_Sockets/
│
├── Servidor.py
├── Cliente.py
└── README.md
```

## Funcionamento

1. O servidor é iniciado e fica aguardando conexões na porta 12345.
2. O cliente se conecta ao servidor utilizando o endereço IP configurado.
3. O cliente envia uma mensagem.
4. O servidor recebe e responde.
5. A comunicação continua até que um dos lados digite `SAIR`.

## Tecnologias Utilizadas

* Python 3
* Biblioteca Socket

## Como Executar

### 1. Iniciar o servidor

```bash
python Servidor.py
```

### 2. Iniciar o cliente

Em outro terminal:

```bash
python Cliente.py
```

## Exemplo de Usos

Cliente:

```text
Você: Olá
```

Servidor:

```text
Cliente: Olá
Sua resposta: Tudo bem?
```

Cliente:

```text
Servidor: Tudo bem?
```

## Possíveis Melhorias

* Suporte a múltiplos clientes
* Interface gráfica
* Comunicação entre computadores diferentes
* Criptografia das mensagens
* Histórico de conversas

## Conclusão

Este projeto demonstra de forma prática a comunicação Cliente-Servidor utilizando sockets TCP em Python, aplicando conceitos fundamentais de Redes de Computadores e servindo como base para sistemas de comunicação mais avançados.


## Vídeo de Apresentação

https://youtu.be/DUPvBbXdurY