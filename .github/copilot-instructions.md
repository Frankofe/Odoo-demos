# 🧑‍💻 Copilot Instructions for Odoo-demos & Construnort Acopio

## Arquitectura General
- Este repositorio extiende Odoo v15, principalmente mediante módulos en `extra-addons/Odoo-demos/`.
- Los módulos siguen la estructura estándar de Odoo: `models/`, `wizards/`, `views/`, `security/`.
- El módulo `construnort_acopio` agrega funcionalidad sobre `sale.order` (ventas), añadiendo un estado custom y un wizard controlado por permisos.

## Flujos de Desarrollo
- **Instalación de módulos:** Copia el módulo en el directorio de addons, actualiza la lista de aplicaciones y realiza la instalación desde la interfaz de Odoo.
- **Permisos:** Los grupos y reglas de acceso se definen en `security/construct_acopio_security.xml` y `security/ir.model.access.csv`. El orden de carga es importante: primero grupos, luego permisos.
- **Testing:** Pruebas manuales recomendadas para flujos de UI y permisos. No hay tests automatizados por defecto.

## Convenciones y Patrones
- **Herencia de modelos:** Se usa `_inherit` para extender modelos nativos de Odoo.
- **Vistas:** Las vistas se heredan usando `xpath` para modificar headers y botones sin duplicar elementos.
- **Wizards:** Los wizards usan `TransientModel` y se vinculan a la orden mediante `Many2one`.
- **Permisos de botón:** El botón "Acopio" solo es visible para usuarios con el grupo `Construct Acopio` y en estados específicos.
- **Persistencia de valores:** Si se requiere persistencia de campos custom, agregar el campo en el modelo principal y sincronizar desde el wizard.

## Integraciones y Dependencias
- Depende del módulo base `sale` de Odoo.
- No hay dependencias externas ni integraciones con APIs fuera de Odoo.

## Ejemplo de Estructura de Módulo
```
construnort_acopio/
├── __manifest__.py
├── models/
│   └── sale_order.py
├── wizards/
│   └── acopio_wizard.py
├── views/
│   ├── sale_order_views.xml
│   └── acopio_wizard_views.xml
├── security/
│   ├── construct_acopio_security.xml
│   └── ir.model.access.csv
└── README.md
```

## Comandos Útiles
- Reiniciar Odoo: `sudo docker restart <nombre_contenedor_odoo>`
- Ver logs: `sudo docker compose logs -f odoo`

## Notas Clave
- No modifiques la lógica de Odoo core, solo extiende mediante herencia y vistas.
- Sigue la convención de permisos y orden de carga para evitar errores de instalación.
- Documenta los cambios en README.md y usa docstrings en Python para mayor claridad.

---
¿Alguna sección necesita más detalle o ejemplos específicos? Indícalo para mejorar estas instrucciones.
