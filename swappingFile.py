def swapdata():
    file1=input('enter file name')
    file2=input('enter file name')
    a=open(file1,'r')
    data_a=a.read()
    b=open(file2,'r')
    data_b=b.read()
    a=open(file1,'w')
    a.write(data_b)
    b=open(file2,'w')
    b.write(data_a)
swapdata()    
    
    



























































































