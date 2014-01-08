#!usr/bin/python
import sys
import re

def solution1a():                            #function for part1
	
	p=re.compile('NP[\w\W]*')                 #RE for part 1
	
	m=p.match('NP@');                          #matching performed
	if m:
		print 'match found : ', m.group();       #if match fund
	else:
		print 'Not found'                        # if not
	
def solution1b():
	p=re.compile('^[\w\s\W]*the\sthe[\s\w\W]*$')   #same as above
	
	m=p.match('I am the the boy');
	if m:
		print 'match found : ', m.group();
	else:
		print 'Not found'
	
	
def solution1c():            #same as above
	p=re.compile('^\:[(\))(\()(\D)(\*)(\P)(\\)(\()(\|)(\$)(\O)]$')
	
	m=p.match(':|')
	if m:
		print 'match found : ', m.group();
	else:
		print 'Not found'


if __name__=='__main__':
	solution1a()
	#solution1b()
	#solution1c()                  #enter the function name here which you wish to run
