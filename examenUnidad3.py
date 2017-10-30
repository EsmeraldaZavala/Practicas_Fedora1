#!/usr/bin/python

import threading
import time

NTHREADS=2

def hilo(i):
    """
 :param i: numero de procesador a efectos ilustrativos
 :return: nada
 """
    print ("[+] se ha procesado  %d" % i)
    time.sleep(3)
    print ("[-] procesador %d finalizado" % i)


simplethread=[]
for i in range(NTHREADS):
    # arranque y comienzo de procesador num i+1
    simplethread.append(threading.Thread(target=hilo, args=[i+1]))
    simplethread[-1].start()

for i in range(NTHREADS):
    # esperamos que acabe el procesador num i
    simplethread[i].join()

print ("[*] all threads finished")
