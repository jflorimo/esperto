#!/usr/bin/python
import	sys
from parsing import parseLine
from fact import Fact

facts = {}
rules = {}
input = []
output = []
queries = []

def debug( ):
	print "####Facts:####"
	for fact in sorted(facts):
		facts[fact].display()
	print "####Rules:####"

def parse( lines ):
	for tmp in lines:
		parseLine(tmp, facts, input, output, queries)

def read( filePath ):
	result = []
	try: 
		fd = open( filePath, 'r' )
	except Exception:
		print( "[Error] Can't open specified file" )
		exit( -2 )

	for line in fd:
		result.append( line )

	parse( result )

if ( len( sys.argv ) < 2 ):
	print ( "Usage : " + sys.argv[0] + " [Input file]" )
	exit( -1 )

read(sys.argv[1])

debug()
