import pandas as pd
#variables
i =0
data = list()

def get_Tags(path):
    global i
    # get data
    ruta = path+'.xlsx'
    df = pd.read_excel(ruta, header=None)
    for tag in df.values:
        if type(tag[0]) == str:
            #print(type(tag[0]))
            data.insert(i, tag[0])
            i += 1
            #print('{}\n'.format(tag[0]))
    #print(i)
    return data





