def machine_epsilon():
	x=1.0
	y=1.0
	while(y<2.0):
    	y=y+x/2.0
    	x=x/2.0
	return x
    
