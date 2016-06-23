"""
    Routes Configuration File

    Put Routing rules here
"""
from system.core.router import routes

routes['default_controller'] = 'Products'
routes['/'] = "Products#index"
routes['/product/add'] = 'Products#add'
routes['/product/<product_id>/edit'] = 'Products#edit'
routes['/product/<product_id>/show'] = 'Products#show'
routes['/product/<product_id>/delete'] = 'Products#delete'
routes['POST']['/product/add/process'] = 'Products#add_process'
routes['POST']['/product/<product_id>/edit/process'] = 'Products#edit_process'