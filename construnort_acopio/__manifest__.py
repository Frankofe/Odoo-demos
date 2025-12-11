{
    "name": "Construnort Acopio",
    "version": "1.0.0",
    "category": "Sales",
    "summary": "Agrega estado acopio y wizard en sale.order",
    "description": "Extiende sale.order con estado acopio, botón y wizard controlado por permisos.",
    "author": "Construnort",
    "depends": ["sale"],
    "data": [
        "security/construct_acopio_security.xml",
        "security/ir.model.access.csv",
        "views/sale_order_views.xml",
        "views/acopio_wizard_views.xml"
    ],
    "installable": True,
    "application": False,
    "license": "LGPL-3"
}
