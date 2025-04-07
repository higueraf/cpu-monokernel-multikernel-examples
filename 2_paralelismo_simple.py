import platform
import time
import threading

if __name__ == "__main__":
    print("Procesador:", platform.processor())
    
    
    
    def fase(nombre, data): 
        print(f"{nombre} procesando: {data}")
        time.sleep(0.5)
        print(f"{nombre} completada para: {data}")
    
    def procesar_en_paralelo(data):
        fases = ["Búsqueda (Fetch)", "Decodificación (Decode)", "Ejecución (Execute)", "Almacenamiento (Store)"]
        hilos = [threading.Thread(target=fase, args=(f, data)) for f in fases]
        for h in hilos: h.start()
        for h in hilos: h.join()
    
    procesar_en_paralelo("Tarea1")
    procesar_en_paralelo("Tarea2")
    
    if __name__ == "__main__":
        procesar_en_paralelo("Tarea1")
        procesar_en_paralelo("Tarea2")
