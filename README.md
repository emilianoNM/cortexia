# Proyecto de Scraping de Farmacia San Pablo

Este repositorio contiene un ejemplo de código para obtener información de productos del sitio web de [Farmacia San Pablo](https://www.farmaciasanpablo.com.mx) mediante Python. El script `scraper.py` muestra cómo descargar la página de resultados de búsqueda y extraer datos básicos, como nombre y precio del producto.

**Nota:** el código se ha escrito de forma genérica porque la estructura del sitio puede cambiar. Es posible que necesites ajustar los selectores CSS para que coincidan con el HTML actual del sitio.

## Requisitos

- Python 3.8 o superior.
- Paquetes `requests` y `beautifulsoup4`.

Puedes instalarlos con:

```bash
pip install requests beautifulsoup4
```

## Uso

1. Edita el valor de `PRODUCTS_URL` en `scraper.py` para apuntar al listado de productos que quieras extraer.
2. Ejecuta el script:

```bash
python scraper.py
```

Esto generará un archivo `products.csv` con los datos obtenidos.

Recuerda respetar los términos de uso del sitio web y realizar peticiones de forma responsable.
