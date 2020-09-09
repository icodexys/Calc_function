def calc(expx):
    group_num=""; express=[];oper="";acomulador=0.0;
    #Here will convert from string to List type spliting groups number by operator +-*/
    for i in expx:
        if i in ".0123456789":
            group_num+=i
        elif i in "+-*/":
            if len(group_num)>0:
                express+=[group_num]
                group_num=""
            express+=[i]   
    express+=[group_num]
    #if list express has only a number or a negative number then will return same value, otherwise will return an error messages
    if len(express)<=2: 
        try:
            return float(expx)
        except:
            return "Error operation"
    #here is where will start to calculate every number by its specified operator
    if express[0]=="-" and len(express)>=4:express=["0"]+express
    acomulador=float(express[0])
    for x in express:
        if  "." in x or x.isdigit():
            if oper=="+":acomulador=acomulador+float(x)
            if oper=="-":acomulador=acomulador-float(x)
            if oper=="*":acomulador=acomulador*float(x)
            if oper=="/":acomulador=acomulador/float(x)
        if x in "+-/*":oper=x
    return acomulador
resultado=0.0
#by iCOdexys
print("Calculator in one line with /*-+")
while  resultado!=0.1:
    resultado=calc(input("Calc: "))
    print(resultado)

 
