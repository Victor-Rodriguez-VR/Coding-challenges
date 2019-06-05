def excel_column_to_number(column):
    value = mathMe(column[0])
    if len(column)>1 :
        
        for number in range(1,len(column)):
            value*=26
            value+= mathMe(column[number])
    
    return(value)
    


def mathMe(letter):
    return ord(letter)-ord('A')+1

