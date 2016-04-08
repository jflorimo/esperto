#!/usr/bin/python
import	sys

facts = {}
rules = {}

def debug( ):
	print "####Facts:####"
	print "####Rules:####"

def read( filePath ):
	result = []
	try: 
		fd = open( filePath, 'r' )
	except Exception:
		print( "[Error] Can't open specified file" )
		exit( -2 )

	for line in fd:
		result.append( line )



