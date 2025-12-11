*Se requiere crear un nuevo modulo llamado construnort_acopio, este se encontrara dentro del repositorio Odoo-demos
*Crear un botón en el header en el modelo de sale.order que se llame acopio.
*Este botón debe abrir un wizard y dentro del mismo crear un campo booleano que al aceptar cambie el campo state de sale.order
*Al campo state en sale.order agregar sumarle esta nueva clave llamada acopio la cual se debe incorporar visiblemente en el statusbar.
*El boton nuevo debe ser visible segun los permisos que tenga el usuario, es decir, debe visualizarse siempre que el usuario tenga el grupo de permiso construct_acopio.
*Este requerimiento es para odoo v15
*El boton nuevo debe ser visible en estado borrador y en estado acopio. Setear el booleano en verdadero y confirmar el wizard aplica el estado acopio mientras que dejar el booleano en false aplica el estado borrador nuevamente.