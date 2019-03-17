def list_insert(data, index, value):
    if index>len(data)-1:
        print("Don't try buffer overflow attacks in Python!")
    else:
        data[index]=value
        
