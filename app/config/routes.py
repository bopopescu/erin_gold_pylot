
from system.core.router import routes


routes['default_controller'] = 'Welcome'
routes['POST']['/process_money'] = 'Welcome#process_money'
routes['/reset'] = 'Welcome#reset'


