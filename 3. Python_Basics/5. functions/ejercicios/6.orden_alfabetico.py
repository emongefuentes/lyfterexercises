def alphabetic_order(text):
    
    list_without_hyphens = text.split("-")
    list_without_hyphens.sort()
    alphabetically_sorted_string = "-".join(list_without_hyphens)
            
    print(list_without_hyphens)
    print(alphabetically_sorted_string)   
    
alphabetic_order("python-variable-funcion-computadora-monitor")         

 
