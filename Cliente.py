import socket

def main():
    # Endereço e porta do servidor (localhost significa a própria máquina)
    endereco_servidor = "127.0.0.1"
    porta = 12345

    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as cliente:
            cliente.connect((endereco_servidor, porta))

            print(f"Conectado ao servidor no endereço {endereco_servidor}")

            # Arquivos para enviar e receber dados do servidor
            entrada = cliente.makefile('r')
            saida = cliente.makefile('w')

            mensagem_enviada = ""
            mensagem_recebida = ""

            print("Chat iniciado. Digite sua mensagem (ou 'SAIR' para encerrar):")

            # Loop de comunicação: Cliente escreve primeiro, depois aguarda a resposta
            while True:
                mensagem_enviada = input("Você: ")
                saida.write(mensagem_enviada + "\n")
                saida.flush()

                if mensagem_enviada.upper() == "SAIR":
                    print("Você encerrou a conexão.")
                    break

                # Aguarda a resposta do servidor
                mensagem_recebida = entrada.readline().strip()

                if not mensagem_recebida or mensagem_recebida.upper() == "SAIR":
                    print("\nO servidor encerrou a conexão.")
                    break

                # Exibe a resposta do servidor de forma mais organizada
                print(f"\nServidor: {mensagem_recebida}")

    except Exception as e:
        print(f"Erro no cliente: Não foi possível conectar ao servidor. {e}")

if __name__ == "__main__":
    main()