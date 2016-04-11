#!/usr/bin/python
import	sys
from parsing import parseLine
from parsing_utils import init_factsValue
from parsing_utils import init_factsRules

facts = {}
rules = []
input = []
output = []


def debug( ):
	print "####Facts:####"
	for fact in sorted(facts):
		facts[fact].display()
		for tt in facts[fact].getRules():
			print tt
	print "####Rules:####"
	for query in rules:
		print(query)
	print("######Input:######")
	print(input)
	print("######OutPut:######")
	print(output)

def parse( lines ):
	for tmp in lines:
		parseLine(tmp, facts, input, output, rules)

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
init_factsValue(facts, input)
init_factsRules(facts, rules)
debug()
