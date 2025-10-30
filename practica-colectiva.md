
---

# 🧭  **Guía para los alumnos**

## 💻 Ejercicio colectivo: *Gestor de alumnos (proyecto modular con Git y GitHub)*

### 🎯 Objetivo general

Realizar un **proyecto grupal** en Python que combine todo lo aprendido hasta ahora (estructuras de control, funciones, listas, diccionarios y modularización) y aplicar un  **flujo de trabajo colaborativo con Git y GitHub** .

---

## 🧩 PARTE 1 – Programa técnico

### 📝 Descripción

Vais a desarrollar un programa en Python llamado  **Gestor de alumnos** , que permitirá registrar, consultar y analizar datos básicos de un grupo de alumnos.

El programa mostrará un menú con las siguientes opciones:

1. Ver lista de alumnos
2. Añadir un nuevo alumno
3. Buscar un alumno por nombre
4. Mostrar estadísticas del grupo
5. Salir

Los datos se guardarán **en memoria** (no en archivos).

Cada alumno se representará como un diccionario con las claves `nombre`, `edad` y `nota`.

```python
alumnos = [
    {"nombre": "Ana", "edad": 20, "nota": 8.5},
    {"nombre": "Luis", "edad": 22, "nota": 6.9}
]
```

El programa se dividirá en tres módulos:

* `main.py` → menú principal
* `funciones_alumnos.py` → altas, búsquedas y listado
* `estadisticas.py` → cálculos de media, máximo y mínimo

---

## 🤝 PARTE 2 – Flujo de trabajo con Git y GitHub

### 🧭 Paso a paso

#### 1️⃣ Crear el repositorio inicial

* Una persona del grupo será el  **líder del proyecto** .
* El líder creará el repositorio en GitHub con el nombre `gestor-alumnos`.
* Los demás serán añadidos como  **colaboradores** .

#### 2️⃣ Clonar el proyecto

Cada alumno clona el repositorio en su ordenador:

```bash
git clone <url_del_repositorio>
```

#### 3️⃣ Crear una rama propia

Cada miembro trabajará en una  **rama separada** :

```bash
git checkout -b feature/<tu_nombre>
```

Ejemplo: `feature/ana`, `feature/luis`, `feature/funciones`, etc.

#### 4️⃣ Reparto de tareas sugerido

| Alumno | Módulo / tarea                                    |
| ------ | -------------------------------------------------- |
| A      | `main.py`(menú principal)                       |
| B      | `funciones_alumnos.py`(añadir, listar, buscar)  |
| C      | `estadisticas.py`(nota media, máxima y mínima) |
| D      | Documentación y README                            |

#### 5️⃣ Hacer commits claros y frecuentes

```bash
git add .
git commit -m "Añadida función para buscar alumno por nombre"
```

#### 6️⃣ Subir la rama al repositorio remoto

```bash
git push origin feature/<tu_nombre>
```

#### 7️⃣ Crear un Pull Request

* En GitHub, cada alumno abrirá un **Pull Request (PR)** para que el líder revise el código.
* El líder o el grupo aprueban y **hacen merge** a `main`.

#### 8️⃣ Sincronizar los cambios finales

Después del merge, todos actualizan su copia:

```bash
git pull origin main
```

#### 9️⃣ Verificar el resultado

El programa debe funcionar completo, con las tres partes integradas.

---

## 📘 Entrega final

Cada grupo entregará:

1. Enlace al repositorio GitHub.
2. Archivo `README.md` con:
   * Descripción del proyecto
   * Participantes y tareas
   * Imagen o texto del flujo de commits:
     ```bash
     git log --graph --all --decorate
     ```
3. Programa funcional con los tres módulos.

---
