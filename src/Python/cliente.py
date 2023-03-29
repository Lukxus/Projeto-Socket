import Front.pygamevisual
import Objetos.figuras
import Jogo.main
import socket #importa modulo socket

#luiz:  192.168.15.14
#leonardo: 192.168.100.14

TCP_IP = '192.168.15.14' # endereço IP do servidor 
TCP_PORTA = 24000      # porta disponibilizada pelo servidor
TAMANHO_BUFFER = 1024
caras = Objetos.figuras.gerando_caras()
escolhido = Front.pygamevisual.escolhaCaras(caras)

def main():

    cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    cliente.connect((TCP_IP, TCP_PORTA))
    print(f"A sua cara é {escolhido.getNome()}")
    
    while 1:
        data, addr = cliente.recvfrom(1024)
        #print(data.decode())
        data = data.decode()
        cliente.send(str(Jogo.main.answer(eval(data), escolhido)).encode())
        pergunta = Jogo.main.ask()
        cliente.send(str(pergunta).encode())
        resposta = cliente.recv(1024).decode()
        print(f"\n A resposta para a sua pergunta foi:{resposta}")
    cliente.close()
        

main()
