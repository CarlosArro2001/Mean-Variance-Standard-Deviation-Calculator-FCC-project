import numpy as np
def calculate(list_values):
    if len(list_values)!=9:
        raise ValueError('List must contain nine numbers.')
        
    li = np.reshape(list_values,(3,3))
    calculation = {
    'mean': [[],[]],
    'variance': [[],[]],
    'standard deviation':[[],[]],
    'max': [[],[]],
    'min': [[],[]],
    'sum': [[],[]]
    }
    x,y = 0,0
    while(y <= 2):
        values = [] #I don't know why .clear() doesn't work
        while(x <= 2):
            values.append(li[x][y])
            x+=1
        calculation['mean'][0].append(np.mean(values))
        calculation['variance'][0].append(np.var(values))
        calculation['standard deviation'][0].append(np.std(values))
        calculation['max'][0].append(max(values))
        calculation['min'][0].append(min(values))
        calculation['sum'][0].append(sum(values))
        x = 0
        y +=1
    x,y= 0,0
    while(x<=2):
        values =[]
        while(y <= 2):
            values.append(li[x][y])
            y +=1
        calculation['mean'][1].append(np.mean(values))
        calculation['variance'][1].append(np.var(values))
        calculation['standard deviation'][1].append(np.std(values))
        calculation['max'][1].append(max(values))
        calculation['min'][1].append(min(values))
        calculation['sum'][1].append(sum(values))
        y=0
        x+=1
    calculation['mean'].append(np.mean(list_values))
    calculation['variance'].append(np.var(list_values))
    calculation['standard deviation'].append(np.std(list_values))
    calculation['max'].append(max(list_values))
    calculation['min'].append(min(list_values))
    calculation['sum'].append(sum(list_values))
    return  calculation