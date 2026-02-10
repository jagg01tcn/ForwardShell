# ForwardShell

Shell remota interactiva sobre HTTP mediante inyección de comandos, usando FIFO para mantener un canal persistente en sistemas Linux vulnerables.  
Diseñada para validación de impacto tras detectar ejecución remota de comandos en aplicaciones web.

---

## Propósito del repositorio

Este repositorio documenta una herramienta de post-explotación orientada a escenarios donde existe **ejecución remota de comandos vía parámetros HTTP** en servidores Linux.

El objetivo es demostrar impacto técnico real transformando una inyección puntual en una **shell interactiva estable**, útil para evaluación de riesgo, CTFs o laboratorios de seguridad ofensiva.

---



### Funcionalidad técnica

Establece una shell remota interactiva contra un endpoint web vulnerable que ejecuta comandos recibidos por un parámetro HTTP (`cmd`).

El script crea un canal de comunicación persistente usando:
- Archivos temporales en `/dev/shm`
- Un pipe FIFO (`mkfifo`)
- Redirecciones estándar hacia `/bin/sh`

Esto permite enviar comandos y recibir su salida de forma continua, simulando una terminal remota básica.

---

#### Problema de seguridad que aborda

- Ejecución remota de comandos (RCE) en aplicaciones web
- Validación de impacto tras detectar inyección de comandos
- Demostración práctica de riesgo operativo

---

#### Escenarios de uso técnico

- Pentesting web
- Red team en entornos controlados
- Laboratorios de entrenamiento y CTFs
- Pruebas de concepto para informes técnicos

No está orientado a:
- Persistencia avanzada
- Operaciones encubiertas
- Uso defensivo

---

#### Suposiciones y requisitos del entorno objetivo

- Sistema Linux
- Ejecución directa de comandos desde un parámetro HTTP
- Disponibilidad de:
  - `/bin/sh`
  - `mkfifo`
  - `tail`
  - `/dev/shm`
- Permisos de escritura en memoria compartida
- Sin controles de autenticación o filtrado efectivo

---

## Ejecución y uso

### Requisitos técnicos

**Sistema local**
- Python 3
- Librerías:
  - `requests`
  - `termcolor`

**Sistema remoto**
- Linux
- Utilidades estándar de shell
- Endpoint vulnerable a inyección de comandos vía HTTP GET

## Requisito crítico: 
  ### payload PHP en el servidor

Para que la forward shell funcione, el servidor objetivo **debe exponer un script PHP vulnerable** que ejecute directamente comandos recibidos por GET.

Ejemplo mínimo funcional:

```php
<?php
system($_GET['cmd']);
?>
```
---
### URL en la que se expone el script
Modificar la url en la que se expone el  payload PHP en el servidor en el sistema
<img width="900" height="628" alt="image" src="https://github.com/user-attachments/assets/b6aa89cf-b9fb-4cf3-9b08-81ed6cf38c13" />


### Ejecución básica

```bash
python3 remote_fifo_shell.py
