# Construnort Acopio

Este módulo extiende el modelo `sale.order` en Odoo, agregando un nuevo estado llamado "acopio" y un wizard para gestionar la transición entre estados, controlado por permisos de usuario.

## 🚀 Características
- Nuevo estado `acopio` en el flujo de ventas.
- Botón "Acopio" en el encabezado de la orden de venta, visible solo para usuarios con el grupo de permisos correspondiente.
- Wizard con campo booleano para cambiar entre estado borrador y acopio.
- Control de visibilidad del botón según grupo de seguridad.

## 📦 Requisitos
- Odoo 15
- Módulo base `sale` instalado

## ⚙️ Instalación
1. Copia la carpeta `construnort_acopio` en tu directorio de addons.
2. Actualiza la lista de aplicaciones en Odoo.
3. Instala el módulo desde el menú de aplicaciones.

## 🔒 Configuración
- Asigna el grupo de seguridad `Construct Acopio` a los usuarios que deban ver y usar el botón/wizard.

## 🛠️ Uso
1. Abre una orden de venta en estado borrador o acopio.
2. Haz clic en el botón "Acopio" en el encabezado.
3. Usa el wizard para cambiar el estado según el valor del booleano.

## 🧪 Testing
- Verifica que el botón solo sea visible para usuarios con el grupo de seguridad.
- Prueba la transición entre estados usando el wizard.

## 📄 Licencia
LGPL-3

---
Desarrollado por Construnort.
