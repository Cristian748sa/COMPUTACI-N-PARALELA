import time #pip install time
#from threading import Thread

def holamundo():
    time_ini = time.time()
    print("Inicio_")
    time.sleep(1)
    print("Computación Paralela")
    print ("Fin_")
    time_end = time.time()
    total = time_end - time_ini
    print(total)

for i in range(1):
    holamundo()

def generaPares(m):
  time_ini = time.time()
  n=2
  lista=[]
  while n<=m:
    lista.append(n*1)
    n+=2
  return lista
  time_end = time.time()
  total = time_end - time_ini
  print(total)
print(generaPares(10))



