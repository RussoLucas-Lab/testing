# Pytest & GitHub Actions

[![Tests](https://github.com/RussoLucas-Lab/pytest-github-actions/actions/workflows/tests.yml/badge.svg)](https://github.com/RussoLucas-Lab/pytest-github-actions/actions/workflows/tests.yml)

Repo personal de práctica siguiendo el curso de Udemy de **Artem Istranin** sobre testing con
Pytest e integración continua con GitHub Actions. _(agregar acá el link al curso)_.

Cada carpeta es un capítulo independiente: un mini-proyecto autocontenido que demuestra un
concepto puntual de pytest (fixtures, parametrize, mocking, niveles de testing, CI/CD, etc.).

## Temario

| Capítulo | Qué demuestra |
|---|---|
| [document-editor](document-editor/) | Testing unitario básico: asserts, `pytest.raises`, `pytest.mark.xfail` para documentar un bug conocido. |
| [fixture-scope](fixture-scope/) | Fixtures con `scope="session"` sobre un `TestClient` de FastAPI compartido. |
| [hands-on](hands-on/) | Ejercicio práctico de testing de una función de negocio (procesamiento de órdenes e-commerce). |
| [pftracker](pftracker/) | Repaso integral: fixtures de distinto scope, `parametrize`, `pytest-mock`, `monkeypatch`, `caplog`, `pytest.ini`. |
| [user-analytics-api](user-analytics-api/) | API FastAPI con mockeo de dependencias lentas/externas, variables de entorno y upload de archivos. |
| [unit-converter](unit-converter/) | Librería de conversión de unidades (CLI con Typer) — versión base. |
| [testing-levels](testing-levels/) | La misma librería, organizada explícitamente en los tres niveles de testing: unit, integration, system. |
| [CICD Unit Converter](CICD%20Unit%20Converter/) | La misma librería con su propio pipeline de CI (GitHub Actions). Continúa como repo independiente en [RussoLucas-Lab/CI-CD-unit-converter](https://github.com/RussoLucas-Lab/CI-CD-unit-converter). |
| [more-itertools](more-itertools/README.student.md) | Librería open-source `more-itertools` vendorizada, usada como sandbox para testear código de terceros (`tests/test_custom.py`). |
| [rund-and-debug](rund-and-debug/) | Carpeta vacía — pendiente. |

## Instalación

```bash
git clone https://github.com/RussoLucas-Lab/pytest-github-actions.git
cd pytest-github-actions
python -m venv venv
source venv/bin/activate   # En Windows: venv\Scripts\activate
pip install -r requirements.txt
```

Ese `requirements.txt` cubre los capítulos sueltos (document-editor, fixture-scope, hands-on,
pftracker, user-analytics-api). Los capítulos empaquetados (unit-converter, testing-levels,
CICD Unit Converter, more-itertools) se instalan aparte con `pip install -e .` (o
`-e ".[dev]"`) desde su propia carpeta — ver el README de cada uno.

## Correr los tests

Cada capítulo se corre de forma independiente, parado en su propia carpeta:

```bash
cd fixture-scope
pytest
```

El workflow de GitHub Actions (`.github/workflows/tests.yml`) corre la suite de cada capítulo
por separado en cada push y pull request.
