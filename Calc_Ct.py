import string
def mid(s,pos,amout):
    return s[pos:pos+amout]
def calc_ct(expx):
    group_num=""; express=[];oper="";acomulador=0.0;
    #Here will convert from string to List type spliting groups number and operators +-*/
    for i in expx:
        if i in string.ascii_letters+"=$#@!&~_)(^[]{}|?><":return "Error operation"  
        if i in ".0123456789":
            group_num+=i
        elif i in "+-*/":
            if len(group_num)>0:
                express+=[group_num]
                group_num=""
            express+=[i]   
    express+=[group_num]
    #will just return with a single value if exist otherwise return an error
    if len(express)<=2: 
        try:
            return float(expx)
        except:
            return "Error Operation"
  
#The operation start from here--------------------------------------------------------
    
    #if the first item from the list express equal '-' then we'll add new item '0'....
    if express[0]=="-" and len(express)>=4:express=["0"]+express
    #if exist any item like '*' or '/' then execute the multiplication and division...
    while "*" in express or "/" in express:
        for y in range(0,len(express),2):
            try:
                catchx=mid(express,y,3)
                if "*" in catchx:
                    express.pop(y)
                    express.pop(y)
                    express.pop(y)
                    p=float(catchx[0])*float(catchx[2])
                    express.insert(y,str(p))           
                if "/" in catchx:
                    express.pop(y)
                    express.pop(y)
                    express.pop(y)
                    p=float(catchx[0])/float(catchx[2])
                    express.insert(y,str(p))
            except:
                return "Invalid expression"
    acomulador=float(express[0])
    #if exist items like '+' and '-' then proceed with the addition and subtraction
    for x in express:
        if  "." in x or x.isdigit():
            if oper=="+":acomulador=acomulador+float(x)
            if oper=="-":acomulador=acomulador-float(x)
        if x in "+-":oper=x  
    return acomulador





resultado=0.0
#by iCOdexys-------*-*-*-*-
print("Calculator in one line with /*-+")
while  resultado!=0.1:
    resultado=calc_ct(input("Calc: ")) 
    print(resultado)
