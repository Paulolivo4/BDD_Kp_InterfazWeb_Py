# BDD_Kp_InterfazWeb_Py

Web interface with an **MVC** structure to create, list, edit and delete the catechized users ("catequizados") of a parish, backed by a **SQL Server** database.

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![SQL Server](https://img.shields.io/badge/SQL%20Server-CC2927?style=flat-square&logo=microsoftsqlserver&logoColor=white)

> The next phase of this project, using MongoDB, is [catequesis_parroquial_MongoDB](https://github.com/Paulolivo4/catequesis_parroquial_MongoDB).

## Features

- Register a catequizado (name, surname, birth date, ID number, address, phone, email, parish, group).
- List, edit and delete records.
- Flash messages for success and error feedback.

## Tech stack

Python · Flask · Jinja2 · pyodbc (ODBC Driver 17 for SQL Server).

## Structure

```
app.py                                # Routes
conexion.py                           # SQL Server connection
controllers/catequizado_controller.py
templates/                            # registro, listar, editar
```

## Routes

| Route | Purpose |
| --- | --- |
| `/` | Redirects to the list |
| `/catequizados` | List records |
| `/registro` | Register |
| `/catequizado/editar/<id>` | Edit |
| `/catequizado/eliminar/<id>` | Delete |

## Status

The controller imports `models.catequizado`, and that module is **not included in this repository yet**, so the app will not start until it is added.

## Configuration

Database settings and the Flask secret are read from environment variables (see `.env.example`): `DB_SERVER`, `DB_NAME`, `DB_USER`, `DB_PASSWORD` and `SECRET_KEY`.
