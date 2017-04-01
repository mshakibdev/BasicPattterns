for r in range(5):
    for c in range(r+2):
        if c<1 :
            print((5-r)*' ',r,end = '')
        elif c>1:
            print('',r,end = '')
        while c==2:
            c=0 
        
    print()
       
