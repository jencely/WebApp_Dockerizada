# WebApp para analizar imágenes
Aplicación web que analiza imágenes utilizando el servicio de inteligencia artificial de Imagga.

## Prerrequisitos

* Docker instalado

## Configuración y funcionamiento

Clonar el repositorio
* Run:
docker run -p 5000:5000 image-analyzer

## Acceso

* URL: http://localhost:5000

### Pasos de verificación

Abra http://localhost:5000 en su navegador
* Verás tres imágenes mostradas
* Haga clic en el botón "Analizar"
* Cada imagen mostrará sus dos etiquetas más relevantes con porcentajes de confianza.
