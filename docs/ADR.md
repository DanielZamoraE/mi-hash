# 📝 ADR – Registro de decisiones técnicas
Proyecto: `mi-hash`  
Autor: Daniel Zamora  

Este documento registra las decisiones técnicas importantes tomadas durante el desarrollo del proyecto

---

## 1. Elección del algoritmo – SHA-256

- Se escogió **SHA-256** porque es un estándar ampliamente utilizado.
- Es seguro, eficiente y forma parte de la familia *SHA-2* aprobada por NIST.
- La librería `hashlib` de Python permite su implementación sin dependencias externas.
- Es fácil de validar mediante herramientas externas (online o terminal).



## 2. Lenguaje de programación – Python

| Ventaja 
| Fácil de desarrollar | Tiempo reducido de implementación |
| Librería estándar | `hashlib` sin dependencias |
| Compatible con CI/CD | Excelente integración con GitHub Actions |
| Soporta empaquetado y ejecución CLI | Uso de `argparse` y `pyproject.toml` |
| Portabilidad | Puede generar ejecutables multiplataforma |

Alternativas como C++ o Rust hubieran requerido más tiempo.


## 3. Interfaz CLI con `argparse`

- Simplicidad de uso para pruebas automatizadas.
- Permite ejecutar comandos como `mi-hash archivo.txt` o `mi-hash --version`.
- Ideal para validaciones en CI/CD.


## 4. Instalador – Inno Setup

- Se eligió **Inno Setup** para crear un instalador profesional para Windows.
- Permite:
  - Instalación estándar y silenciosa (`/silent`)
  - Añadir el ejecutable al PATH
  - Ejecutar automáticamente comandos post-instalación
  - Generar acceso directo al escritorio

Alternativa descartada: MSI (mas complejo y requiere herramientas adicionales).


## 5. Firma digital – GPG

- Se utilizó para garantizar integridad y autenticidad.
- Permite verificar que el instalador no fue modificado.

 Aporta a **seguridad e integridad (hashes, firmas)** 


## 6. Automatización CI/CD – GitHub Actions

- Se implementó pipeline que ejecuta:
  - Instalación de dependencias
  - Pruebas unitarias (`pytest`)
  - Construcción del paquete (`python -m build`)
- Se ejecuta en cada commit para garantizar reproducibilidad.


## 7. Pruebas – Pytest

- Se utilizó para validar la lógica del hash.
- Incluidas en pipeline automático.
- Se comprobaron pruebas funcionales manuales (matriz de instalación).


## 8. Empaquetado del software – `pyproject.toml`

- Estructura recomendada por PEP 518.
- Permite construir fácilmente (`python -m build`).
- Facilita distribución y mantenibilidad.


## 9. Gestión de entorno – `virtualenv` + `requirements.txt`

- Permite reproducibilidad en nuevos ambientes.
- Facilita pruebas en CI/CD.

## Conclusión

Las decisiones técnicas fueron tomadas considerando:

 Requerimientos académicos  
 Simplicidad y eficiencia  
 Compatibilidad con automatización (CI/CD)  
 Seguridad e integridad del software  

El stack utilizado permite entregar una solución **funcional, automatizada y correctamente instalada**


