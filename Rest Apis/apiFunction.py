import pandas as pd
df = pd.read_csv("physician_rx.csv")

def top5(rows_count):
    return df.head(rows_count)

def top5Column(column):
    return df[[column]].head()  #double [] means it will return dataframe
    #other option - df[column].to_frame().head()

def filteredColumn(start, end, column_str):
    #columns=column_str.split(',')
    #columns = list(map(int, columns))
    columns = list(map(lambda x : int(x), column_str.split(',')))
    return df.iloc[start:end,columns]

def specificFilteredColumn(column_name, operator, value):
    if(operator == 'equals'):
        return df[df[column_name]==value]
    elif operator == 'more than':
        return df[df[column_name]>value]
    else:
        return df[df[column_name]<value]
