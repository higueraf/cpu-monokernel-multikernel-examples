import platform
import time
import threading
import matplotlib.pyplot as plt

if __name__ == "__main__":
    print("Procesador:", platform.processor())
    
    
    
    resultados = {}
    
    def pipeline(data):
        start = time.time()
        for d in data:
            print(f"Procesando {d} en pipeline...")
            for fase in range(4):
                time.sleep(0.5)
        resultados["Pipeline"] = time.time() - start

    def paralelismo(data):
        def tarea(d):
            print(f"Procesando {d} en paralelo...")
            for fase in range(4):
                time.sleep(0.5)
        start = time.time()
        hilos = [threading.Thread(target=tarea, args=(d,)) for d in data]
        for h in hilos: h.start()
        for h in hilos: h.join()
        resultados["Paralelismo"] = time.time() - start

    
    datos = ["Tarea1", "Tarea2", "Tarea3", "Tarea4"]
    
    pipeline(datos)
    paralelismo(datos)
    
    # Mostrar resultados
    for k, v in resultados.items():
        print(f"{k}: {v:.2f} segundos")
    
    # Gráfica
    plt.bar(resultados.keys(), resultados.values())
    plt.ylabel("Tiempo (segundos)")
    plt.title("Comparación: Pipeline vs Paralelismo")
    plt.savefig("comparacion_pipeline_paralelismo.png")
    plt.show()
    
    if __name__ == "__main__":
        pipeline("Tarea1")
        pipeline("Tarea2")
        paralelismo("Tarea1")
        paralelismo("Tarea2")
