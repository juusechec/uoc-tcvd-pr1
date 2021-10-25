# uoc-tcvd-pr1
Práctica 1 de la asignatura Tipología y Ciclo de Vida de los Datos de la UOC

# Objetivo
Cálculo de costo de vida tecnológico en algunos países de la región iberoamericana, simplificando el modelo a información de mercadolibre y todos sus subportales con ciertos productos que se encuentran en la mayoría de ellos.

# Dependencias
- python 3.8

# Pasos para instalar
```sh
virtualenv venv
source venv/bin/activate
pip install -r requirements.txt
```

# Ejecutar
```sh
source venv/bin/activate
python ScrapperSelenium.py
```

# Guardar nuevas dependencias
```sh
pip freeze > requirements.txt
```

# Integrantes
- Jorge Ulises Useche Cuellar (@juusechec)
- Cristian Alejandro Zamora Flores (@chrisitan)

# Descripción de los ficheros
- ScrapperSelenium.py: Script standalone para la ejecución del webscrapping.
- MercadoLibreData.csv: Archivo destino del webscrapping.
- .gitignore: Archivo que nos ayuda a decirle al sistema git qué queremos trackear en la gestión del versionamiento del código.
- LICENSE: Licencia del código generado, no de la información resultante o de las herramientas usadas.
- README.md: Documentación del proyecto.
- requirements.txt: Lista de las dependencias del proyecto python.

# Estructura de los datos
| Columna      | Descripción                                       |
| ------------ | -----------                                       |
| product      | Nombre del producto buscado                       |
| country      | País del subsitio de Mercado libre buscado        |
| url          | URL del item encontrado                           |
| precio       | Precio junto con su moneda                        |
| item         | Nombre completo del item encontrado               |

# [DOI](https://en.wikipedia.org/wiki/Digital_object_identifier) (digital object identifier) para referencias
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.5580016.svg)](https://doi.org/10.5281/zenodo.5580016)

# Enlace Zenodo
https://zenodo.org/record/5580016#.YXXxkHtOldA
