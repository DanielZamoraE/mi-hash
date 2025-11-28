#  Manual de instalación, uso y desinstalación – `mi-hash`

Este documento describe cómo instalar, ejecutar y desinstalar el programa **mi-hash**, desarrollado como proyecto académico. Incluye instrucciones tanto para instalación interactiva (GUI) como instalación silenciosa, pruebas posteriores y resolución de problemas.

---

##  1. Requisitos previos

| Requisito | Detalle |
|-----------|---------|
| Sistema Operativo | Windows 10 o 11 (x64) |
| Permisos | Se requiere ejecutar como administrador |
| Terminal recomendada | PowerShell o CMD |
| Archivo de instalación | `mi-hash-installer.exe` |

---

##  2. Instalación estándar (GUI)

1. Descargar el archivo `mi-hash-installer.exe`
2. Hacer doble clic para ejecutar
3. Seguir los pasos:  
   **Next → Install → Finish**
4. Finalizada la instalación, cerrar y abrir nuevamente la terminal.
5. Verificar la instalación ejecutando:

```powershell
mi-hash --version

Ejecutar el siguiente comando desde PowerShell:
& "C:\ruta\mi-hash-installer.exe" /silent
Luego abrir una nueva terminal y verificar:
mi-hash --version
Generar hash SHA-256 desde archivo
y deberia dar como resultado: 586a8f983caddee01bebdba31ca3499fc487f98a14c6e273df6fcbc23f22b96f

Desintalación:
(GUI) Panel de Control → Programas → mi-hash → Desinstalar
Forma silenciosa: en Powershell escriba "C:\Program Files\mi-hash\unins000.exe" /silent

Resolución de problemas

| Problema                 | Posible solución                                       |
| ------------------------ | ------------------------------------------------------ |
| `mi-hash` no se reconoce | Cerrar y volver a abrir PowerShell después de instalar |
| Error al instalar        | Ejecutar instalador como administrador                 |
| No genera hash           | Verificar que el archivo existe                        |
| No corre `--version`     | Reinstalar y reabrir terminal                          |
| No se puede desinstalar  | Usar método silencioso desde Program Files             |

Informacion tectnica

| Elemento                  | Detalle                                                           |
| ------------------------- | ----------------------------------------------------------------- |
| Lenguaje                  | Python                                                            |
| Algoritmo                 | SHA-256 (librería `hashlib`)                                      |
| CLI                       | Implementada con `argparse`                                       |
| Instalador                | Inno Setup                                                        |
| Instalación silenciosa    | Soportada mediante `/silent`                                      |
| Desinstalación silenciosa | También soportada                                                 |
| Firma digital             | GPG                                                               |
| Tests automatizados       | Pytest (incluye ejecución en CI)                                  |
| Pipeline CI/CD            | GitHub Actions, pruebas en cada commit y generación de artefactos |

Manual creado por Daniel Zamora 
Proyecto: Generación de hash SHA-256 con instalador multiplataforma.

