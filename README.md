# Simulación de Procesamiento Pipeline vs Paralelismo

Este proyecto en Python compara dos enfoques de procesamiento:

- ⛓️ **Pipeline (secuencial)**: Las tareas se procesan fase por fase, una tras otra.
- ⚡ **Paralelismo (concurrente)**: Las fases se ejecutan al mismo tiempo.

Incluye ejemplos básicos, avanzados, narrativos con emojis y una comparación visual con gráficos.

---

## 📁 Estructura del proyecto

```
procesamiento_simulado/
├── 1_pipeline_simple.py
├── 2_paralelismo_simple.py
├── 3_pipeline_complejo.py
├── 4_paralelismo_complejo.py
├── 5_comparacion_grafica.py
└── comparacion_pipeline_paralelismo.png  # Se genera automáticamente
```

---

## 🚀 Requisitos

- Python 3.8 o superior
- pip

---

## 🧪 Paso a paso

### 1. Crear y activar entorno virtual

```bash
python -m venv venv
# Activar entorno virtual
# En Windows:
venv\Scripts\activate
# En Mac/Linux:
source venv/bin/activate
```

---

### 2. Instalar dependencias

```bash7
pip install matplotlib
```

---

### 3. Ejecutar los archivos

```bash
python 1_pipeline_simple.py
python 2_paralelismo_simple.py
python 3_pipeline_complejo.py
python 4_paralelismo_complejo.py
python 5_comparacion_grafica.py
```

> El archivo `5_comparacion_grafica.py` genera una imagen llamada `comparacion_pipeline_paralelismo.png` que muestra visualmente la diferencia de rendimiento entre ambos enfoques.

---

## 📌 Nota

Cada script imprime el modelo del procesador detectado y simula las 4 fases de procesamiento: **Carga**, **Transformación**, **Análisis**, y **Finalización**.

---

## 🎓 Ideal para:

- Clases de arquitectura de computadores
- Introducción a concurrencia
- Demostraciones visuales de procesamiento
