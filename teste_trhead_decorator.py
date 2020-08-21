import threading,time

def threaded(fn):
    def wrapper(*args, **kwargs):
        thread = threading.Thread(target=fn, args=args, kwargs=kwargs)
        thread.start()
        return thread
    return wrapper
@threaded
def imprimir(msn):
    print(msn)


@threaded
def func_to_be_threaded():
    for i in range(10):
        imprimir(str(i) + 'func_to_be_threaded')
        time.sleep(1)


@threaded
def func_to_be_threaded_n2():
    for i in range(10):
        imprimir(str(i) + 'func_to_be_threaded_n2')
        time.sleep(1)

#func_to_be_threaded()

func_to_be_threaded_n2()
print(threading.activeCount())

for i in range(10):
    print(threading.enumerate())
    print(threading.activeCount())
    time.sleep(2)
    

print(threading.activeCount())



    


