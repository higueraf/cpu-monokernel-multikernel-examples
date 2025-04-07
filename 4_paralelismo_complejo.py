import platform
import time
import platform
import threading

if __name__ == "__main__":
    print("Procesador:", platform.processor())
    
    
    
    def fase(nombre, data): 
        print(f"{nombre} procesando: {data} en {platform.processor()}")
        time.sleep(0.5)
        print(f"{nombre} completada para: {data}")
    
    def procesar(data):
        fases = ["Búsqueda (Fetch)", "Decodificación (Decode)", "Ejecución (Execute)", "Almacenamiento (Store)"]
        hilos = [threading.Thread(target=fase, args=(f, data)) for f in fases]
        for h in hilos: h.start()
        for h in hilos: h.join()
    
    procesar("Tarea1")
    procesar("Tarea2")
    
    if __name__ == "__main__":
        procesar("Tarea1")
        procesar("Tarea2")
