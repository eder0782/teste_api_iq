import threading



t1 =None
def cont():
    global t1
    for i in range(5):        
        print(i)

t1 = threading.Thread(target=cont)
t1.start()
while t1.is_alive():
    print('rodando')


print('final: '+ str(t1.is_alive()))

  