print('====================================\n\n')
print('Running main.py - module name {0}'.format(__name__))

import Modules

print(Modules)

Modules.pprint_dict('main.globals', globals())

print('=========================================')