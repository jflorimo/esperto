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
		print line

if ( len( sys.argv ) < 2 ):
	print ( "Usage : " + sys.argv[0] + " [Input file]" )
	exit( -1 )

read(sys.argv[1])

