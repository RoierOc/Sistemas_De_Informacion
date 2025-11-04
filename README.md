## Sistemas de Información

Nombre: Roger Fabian Bonilla Caro

## 1. Análisis sobre AWS Lambda

AWS Lambda es un servicio de AWS que permite ejecutar código sin manejar servidores. Esto significa que no es necesario administrar infraestructura para que una función se ejecute. Lambda corre el código cuando ocurre un evento y detiene el proceso cuando termina.
Está pensado para tareas pequeñas y específicas que se activan por eventos como cargas a un bucket S3 (almacenamiento), llamadas desde API Gateway u otros servicios dentro de AWS. Su uso facilita la creación de aplicaciones basadas en eventos de manera sencilla.
La ventaja más grande que tiene AWS lambda es la posiblidad de ejecutar script e interactuar con los servicios de AWS solo cuando se necesiten ejecutar, sin necesidad de preocuparse por infraestructura (serverless).

## 2. Beneficios

- No se requieren servidores dedicados.
- Escala automáticamente según la demanda.
- Se paga solo cuando la función se ejecuta.
- Se integra con muchos servicios de AWS.
- Requiere poco mantenimiento.

## 3. Limitaciones

- El tiempo máximo de ejecución es de 15 minutos.
- El espacio para almacenamiento temporal es limitado pero configurable.

## 4. Casos de uso comunes

- Ejecutar procesos cuando se cargan archivos a S3.
- Automatizar tareas programadas con EventBridge, servicio usado para programar la ejecución de algo (trigger).
- Ejecución de scripts para limpiar datos.

