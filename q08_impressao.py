#08. Utilize um laço de repetição para gerar valores de 1 a 20, dando um tempo da impressão entre um valor e outro de 1segundo.
import time
i= 1
while i < 21:
    time.sleep(1)
    print(i)
    i+=1