#!/usr/bin/python3

count = 1

with open('data.csv', 'r') as data:
    for d in data.readlines():

        if not 'nivel' in d:
            
            valores = d.strip().split(',')
            print (f'Dimension {count}:', end='\t')

            for v in valores:
                if not v == 16:
                    
                    nivel = int(v)
                    porcentaje = (nivel / 16) * 100

                    print(f'{porcentaje}%', end='\t|\t')

            count += 1
            print()
