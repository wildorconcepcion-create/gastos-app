# Sistema de Control de Gastos

## Descripción

Aplicación web desarrollada con Python, Flask y SQLite que permite registrar gastos personales y generar reportes.

El sistema incluye autenticación, almacenamiento en base de datos SQLite, edición de gastos y auditoría de acciones realizadas por los usuarios.

---

## Tecnologías Utilizadas

- Python 3
- Flask
- SQLite
- SQLAlchemy
- Bootstrap 5
- HTML5

---

## Credenciales de Acceso

Usuario:

```text
admin
```

Contraseña:

```text
123
```

---

## Funcionalidades

### Inicio de Sesión

Permite acceder al sistema mediante autenticación de usuario.

imagenes/login.png

---

### Dashboard

Visualiza:

- Total de gastos registrados.
- Monto total acumulado.
- Accesos directos a las funcionalidades.

imagenes/dashboard.png

---

### Registro de Gastos

Permite registrar:

- Fecha
- Descripción
- Monto

imagenes/nuevo_gasto.png

---

### Reporte de Gastos

Permite consultar todos los gastos registrados y visualizar el total acumulado.

imagenes/reporte.png

---

### Edición de Gastos

Permite actualizar la información de gastos previamente registrados.

---

### Auditoría

Registra todas las acciones realizadas por el usuario:

- Registro de gastos.
- Edición de gastos.

Cada acción almacena:

- Fecha y hora.
- Usuario.
- Acción ejecutada.
- Detalle.

imagenes/auditoria.png

---

## Estructura del Proyecto

```text
gastos_app/
│
├── app.py
├── models.py
├── requirements.txt
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── dashboard.html
│   ├── nuevo_gasto.html
│   ├── editar_gasto.html
│   ├── reporte.html
│   └── auditoria.html
│
├── imagenes/
│
└── instance/
```

---

## Instalación

Clonar repositorio:

```bash
git clone https://github.com/wildorconcepcion-create/gastos-app.git
```

Ingresar al proyecto:

```bash
cd gastos_app
```

Crear entorno virtual:

```bash
python -m venv .venv
```

Activar entorno virtual:

```bash
.venv\Scripts\activate
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar aplicación:

```bash
python app.py
```

---

## Funcionamiento

1. Iniciar sesión con las credenciales proporcionadas.
2. Acceder al Dashboard principal.
3. Registrar gastos indicando fecha, descripción y monto.
4. Consultar el reporte de gastos.
5. Editar gastos registrados.
6. Revisar la auditoría para visualizar las acciones realizadas dentro del sistema.

---

## Autor

Wildor Alfredo Concepción Raico
