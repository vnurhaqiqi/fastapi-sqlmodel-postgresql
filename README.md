# FastAPI with SQLModel and PostgresSQL

## Introduction
Example FastAPI with [SQLModel by fouder itself, tiangolo](https://sqlmodel.tiangolo.com/), connected to PostgreSQL. As reference, this tutorial by Michael Herman about [fastapi-sqlmodel](https://testdriven.io/blog/fastapi-sqlmodel/) and I made some tweaks from there.

## Installment
#### clone the project

```bash
git clone https://github.com/vnurhaqiqi/fastapi-sqlmodel-postgresql.git
```

#### run virtual env

```bash
source /your-env/bin/activate -> Linux

your-env\Scripts\activate.bat -> Windows
```

#### migrate models using alembic

```bash
alembic upgrade head
```

#### run project using uvicorn

```bash
uvicorn main:app --reload
```

---
Copyright © 2021 by Viqi Nurhaqiqi