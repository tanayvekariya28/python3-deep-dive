# Modules
print('---------{0}---------\n\n'.format(__name__))

def pprint_dict(header,d):
    print('\n\n------------------------------')
    print('***********{0}***********'.format(header))
    for key,value in d.items():
        print(key, value)

    print('--------------------------------\n\n')

pprint_dict('Module1.global()', globals())

print('------------END OF {0}----------'.format(__name__))