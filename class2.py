class Person:
    '''rep'''
    pop=0
    def __init__(self,name):
        '''init'''
        self.name=name
        print 'init is %s' % self.name
        Person.pop+=1
        
    def hi(self):
    	'''Greeting
    	
    	R...'''
    	print 'hi,my name is%s' % self.name
    	
    def howmany(self):
    	'''print pop'''
    	if Person.pop==1:
    		print 'only 1'
    	else:
    		print 'we have %d' % Person.pop
    		
p = Person ('qqq好i1')
p.hi()
p.howmany()

p = Person ('qqq2')
p.hi()
p.howmany()
    