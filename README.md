# 🚀 CRUD Básico con FastAPI

Este es un CRUD básico desarrollado con **FastAPI**, donde se utiliza una **lista en memoria** como base de datos temporal. En futuras versiones, se implementará una conexión con una base de datos SQL.

---

## 📌 **Requisitos**
Antes de comenzar, asegúrate de tener instalado:
- Python 3.8+
- Virtualenv (opcional pero recomendado)

---

## ⚙️ **Instalación y Configuración**

### 1️⃣ **Clonar el Repositorio**
```bash
git clone https://github.com/tu_usuario/tu_repositorio.git
cd tu_repositorio

2️⃣ Crear un Entorno Virtual (Opcional pero Recomendado)
python -m venv venv
source venv/bin/activate  # En macOS/Linux
venv\Scripts\activate      # En Windows

3️⃣ Instalar Dependencias
pip install fastapi uvicorn pydantic

🚀 Ejecutar el Proyecto
fastapi dev main.py

📖 Rutas Disponibles
GET	/	Página de inicio
POST	/newitem/	Crear un nuevo ítem
GET	/allitems/	Obtener todos los ítems
PUT	/itemsupd/{item_id}	Actualizar un ítem por ID
DELETE	/itemdelete/{item_id}	Eliminar un ítem por ID

Puedes probar la API con Swagger UI en:
🔗 http://127.0.0.1:8000/docs
