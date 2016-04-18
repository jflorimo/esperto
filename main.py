#!/usr/bin/python
import	sys
from parsing import parseLine
from parsing_utils import init_factsValue
from parsing_utils import init_factsRules
from parsing import isVar
from graph import generateGraph

facts = {}
rules = []
input = []
output = []


def debug( ):
	print "####Facts:####"
	for fact in sorted(facts):
		facts[fact].display()
		for rule in facts[fact].getRules():
			rule.display()
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

def manualInputOutput(str):
	tmp = list(raw_input(str).upper())
	for x in tmp:
		if isVar( x ) == False:
			print( "[Error] non authorized char" )
			exit( -2 )
	return tmp


if ( len( sys.argv ) < 2 ):
	print ( "Usage : " + sys.argv[0] + " [Input file]" )
	exit( -1 )

deb = False
graph = False
manualIn = False
manualOut = False


for (i,arg) in enumerate(sys.argv):
	if arg == '-d':
		deb = True
	elif arg == '-g':
		graph = True
	elif arg == '-i':
		manualIn = True
	elif i != 0:
		read(sys.argv[i])


# testuru = list(raw_input("kk:").upper())

if manualIn == True:
	input = manualInputOutput("input:")
if manualIn == True:
	output = manualInputOutput("output:")

init_factsValue(facts, input)
init_factsRules(facts, rules)

if deb == True:
	debug()
if graph == True:
	generateGraph(facts, input, output)

for res in output:
	print "" + res + " -> " + str( facts[res].searchValue( facts ) )
