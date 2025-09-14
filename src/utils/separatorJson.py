
def separatorJson(json):
    fields = None
    records = None
    
    for k,v in json.items():
        if k == 'fields':
            fields = v
        elif k == 'records':
            records = v
        else:
            break
        
    return fields, records
        