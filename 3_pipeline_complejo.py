import platform
import time
import platform

if __name__ == "__main__":
    print("Procesador:", platform.processor())
    
    
    
    def fase(nombre, data): 
        print(f"{nombre} procesando: {data}")
        time.sleep(0.5)
        return data + f" -> {nombre}"
    
    def pipeline_complejo(data):
        print("Modelo de máquina:", platform.processor())
        fases = ["Búsqueda (Fetch)", "Decodificación (Decode)", "Ejecución (Execute)", "Almacenamiento (Store)"]
        for f in fases:
            data = fase(f, data)
        print("Resultado:", data)
    
    pipeline_complejo("Tarea1")
    pipeline_complejo("Tarea2")
    
    if __name__ == "__main__":
        pipeline_complejo("Tarea1")
        pipeline_complejo("Tarea2")
