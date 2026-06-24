import socket

def main():
    # Define a porta onde o servidor vai "escutar" as conexões
    porta = 12345

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as servidor:
            servidor.bind(("0.0.0.0", porta))
            servidor.listen(1)

            print(f"Servidor iniciado. Aguardando conexão na porta {porta}...")

            # O servidor fica travado aqui até um cliente se conectar
            socket_cliente, endereco = servidor.accept()

            with socket_cliente:
                print("Cliente conectado com sucesso!")

                # Arquivos para ler e escrever dados no socket
                entrada = socket_cliente.makefile('r')
                saida = socket_cliente.makefile('w')

                mensagem_recebida = ""
                mensagem_enviada = ""

                print("Chat iniciado. Digite 'SAIR' para encerrar a conexão.")

                # Loop principal de comunicação: lê do cliente, escreve para o cliente
                while True:
                    # Aguarda a mensagem do cliente
                    mensagem_recebida = entrada.readline().strip()

                    if not mensagem_recebida or mensagem_recebida.upper() == "SAIR":
                        print("\nO cliente encerrou a conexão.")
                        break

                    # Exibe a mensagem recebida de forma mais organizada
                    print(f"\nCliente: {mensagem_recebida}")

                    # Lê o que o servidor quer responder e envia
                    mensagem_enviada = input("Sua resposta: ")
                    saida.write(mensagem_enviada + "\n")
                    saida.flush()

                    if mensagem_enviada.upper() == "SAIR":
                        break

                # Fecha a conexão do socket quando o chat terminar
                print("Servidor encerrado.")

    except Exception as e:
        print(f"Erro no servidor: {e}")

if __name__ == "__main__":
    main()