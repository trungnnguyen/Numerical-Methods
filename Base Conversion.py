#Program to convert a number of given base to a number of another base

def Input_total():
    #function gets input from user converts it to decimal.
    #the base is given by the user or the base can be acquired
    #depending on the input.
    #returns the total in decimal notation and the base acquired
    #from the input.
    str_input=str(raw_input('Input: '))#input value
    print "Do you want to"
    print "1) give the input of the base or 2) use the minimum " + \
    "base from the input?"

    ch=int(raw_input("Your choice: "))#how to assign the base
    if(ch==1):#user supplies the base
        base_input=int(raw_input('Base Input: '))
    else:#Worst case base
        base_input=36
        
    new_str_input=str_input.upper()
    new_str_input=new_str_input[::-1] #converting input to more useful form

    min_base=check_base(base_input,new_str_input)#finding the base from input
    if(ch==2):
        base_input=min_base #assigning found base

    total =0 #initial value for input

    for i in range(0,len(new_str_input)): #to find the total in decimal value
        if(ord(new_str_input[i])<65):
            total=total + int(new_str_input[i])*(base_input**(i))
        else:
            total=total + int(ord(new_str_input[i])-55)*(base_input**(i))

    return total, min_base


def check_base(base_input,new_str_input):
    #checks if base given as input base is possible and finds base from input
    #corrects base if wrongly given
    #returns min base from input
    ord_input=[]
    for i in new_str_input:
        ord_input.append(int(ord(i)))
        
    min_base=max(ord_input)+1
    

    if(base_input<10):
        base_input=base_input+48
        if(min_base<=base_input):
            base_input=base_input-48
        else:
            print "Base number too low"
            base_input=int(raw_input('Base Input: '))
            check_base(base_input,new_str_input)
            
    if(base_input>=10):
        base_input=base_input+55
        if(min_base<=base_input):
            base_input=base_input-55
        else:
            print "Base number too low"
            base_input=int(raw_input('Base Input: '))
            check_base(base_input,new_str_input)

    if(min_base<65):
        min_base=min_base-48
    else:
        min_base=min_base-55

    return min_base



def output_total(total,base_output):
    #gives output in the base required 
    out_rem=[]
    while(total>=base_output):
        out_rem.append(str(total%base_output))
        total=int(total/base_output)
    out_rem.append(str(total))
    for i in range(0,len(out_rem)):
        if(int(out_rem[i])>=10):
            out_rem[i]=chr(int(out_rem[i])+55)
    out_rev=''.join(out_rem)
    ans=out_rev[::-1]
    return ans

ch='Y'

while(ch.upper()=='Y'):
    total,min_base=Input_total()#starting of program
    print "The total is "+str(total) #total in decimal format
    print "The base based on input is "+str(min_base) #base from input

    base_output=int(raw_input('Base Output: ')) # the base for output
    print "the output for base "+ str(base_output)+ \
    " is "+str(output_total(total,base_output))# final output
    ch=raw_input( "Do you wish to enter another value?(Y/n) ")
    while(ch.upper()!='Y' and ch.upper()!='N'):
        ch=raw_input( "Do you wish to enter another value?(Y/n) ")
    if(ch.upper()=='N'):
        print "Thank You"
        
