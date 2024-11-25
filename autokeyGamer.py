import random
import keyboard
import time
from ntfpy import NTFYServer, NTFYUser, NTFYClient, NTFYPushMessage, NTFYViewAction



chars = 'wasd'
tempo = 0
print('Pressione p para começar e o para parar')

running = False
def main(key):
	server = NTFYServer("https://ntfy.sh")
	user = NTFYUser("user", "pass")
	client = NTFYClient(server, "cougar")
	message = NTFYPushMessage("Essa tecla foi apertada: " + key + " em " + str(tempo) + " minutos", title = "Tecla pressionada")
	message.addTag("advanced")

	client.send_message(message)

while True:
    if keyboard.is_pressed('p') and not running:
        running = True
        print('Iniciando...')

    if running:
        key = random.choice(chars)
        keyboard.write(key)
        main(key)
        
        print('key: ' + key + ' tempo: ' + str(tempo) + ' minutos')
        tempo += 1
        time.sleep(60)

    if keyboard.is_pressed('o'):
        running = False
        key = 'Finalizado'
        main(key)
        print('Parando...')
        break

        
print('Finalizado')