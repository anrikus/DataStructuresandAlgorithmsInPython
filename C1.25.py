def del_punc(data):
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    copy_data = ""
    for x in data:
        if x not in punctuations:
            copy_data = copy_data + x
    return copy_data
        
