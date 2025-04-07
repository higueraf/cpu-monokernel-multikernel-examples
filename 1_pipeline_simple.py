import platform
import time

if __name__ == "__main__":
    print("Procesador:", platform.processor())
    
    
    
    def fase1(data): print(f"Búsqueda (Fetch) procesando: {data}"); time.sleep(0.5); return data + " -> F1"
    def fase2(data): print(f"Decodificación (Decode) procesando: {data}"); time.sleep(0.5); return data + " -> F2"
    def fase3(data): print(f"Ejecución (Execute) procesando: {data}"); time.sleep(0.5); return data + " -> F3"
    def fase4(data): print(f"Almacenamiento (Store) procesando: {data}"); time.sleep(0.5); return data + " -> F4"
    
    def pipeline(data):
        result = fase1(data)
        result = fase2(result)
        result = fase3(result)
        result = fase4(result)
        print("Resultado final:", result)
    
    pipeline("Tarea1")
    pipeline("Tarea2")
    
    if __name__ == "__main__":
        pipeline("Tarea1")
        pipeline("Tarea2")
