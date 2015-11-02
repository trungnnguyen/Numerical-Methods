n=float(raw_input('Value: '))



def bin_conv_int(k):
    #integer to binary conversion
    #b_rev -  reverse of binary of k
    #k - integer to be converted
    #b - binary of given integer (str)
    b_rev=[]
    while(k>0):
        b_rev.append(str(k%2))
        k=k/2
    b_rev=''.join(b_rev)
    b=b_rev[::-1]
    return b    
    
def bin_conv_fraction(m):
    #fraction part to binary conversion
    #fb - binary of fraction
    #tot - Temporary variable for iteration
    #m - fraction of a number to be converted to binary
    fb=[]
    tot=3.2 # any number as long as tot!=1
    while(m!=0):
        tot=m*2
        fb.append(str(int(tot)))
        m=tot-int(tot)
    fb=''.join(fb)
    return fb

b=bin_conv_int(int(n))
fb=bin_conv_fraction(n-int(n))

Full_binary=b+fb
e=len(b)-1
E=127+e #for 32 bit system

if(n>=0):
    s='0'
else:
    s='1'

E_binary=bin_conv_int(E)
len_E_binary=len(E_binary)
for i in range(0,8-len_E_binary):
    E_binary='0'+E_binary

for i in range(0,23-len(Full_binary)):
    Full_binary=Full_binary+'0'
full_32bit=s+'-'+E_binary+'-'+Full_binary

print 'The 32-bit binary is: '+full_32bit
print 'The sign bit(1) is: '+s
print 'The exponent bit(8) is: ' +E_binary
print 'The mantissa bit(23) is: ' +Full_binary
print 'The exponent is: '+str(e)
print 'The Bias is: ' + str(E)
