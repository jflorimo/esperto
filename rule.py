# @Author: jflorimo
# @Date:   2016-04-10 12:50:30
# @Last Modified by:   jflorimo
# @Last Modified time: 2016-04-12 20:24:41

from __future__ import print_function
from parsing import isVar
from fact import Fact
import re

class Rule( object ):

	def __init__( self, ruleQuery, answer ):
		self.rule = ruleQuery;
		self.answer = answer
		self.facts = []
		self.child = 0
		for char in self.rule:
			self.addFact(char)


	#GETTER && SETTER
	def getRule( self ):
		return ( self.rule )
	def getAnswer( self ):
		return ( self.answer )

	#METHODS

	def op_add(self, l, r, facts):
		return (l.op_add(r, facts))

	def op_or(self, l, r, facts):
		return (l.op_or(r, facts))

	def op_xor(self, l, r, facts):
		return (l.op_xor(r, facts))


	def opn_add(self, l, r, facts):
		result = Fact(l.getName)

		if ( l.getValue() == 1 and r.getValue() == 0 ):
			result.setValue( 1 )
		elif ( l.getValue() == 0 or r.getValue() == 1 ):
			result.setValue( 0 )
		elif ( l.getValue() == -1 or r.getValue() == -1 ):
			result.setValue( -1 )
		else:
			result.setValue( 0 )
		return (result)

	def opn_or(self, l, r, facts):
		result = Fact(l.getName())
		if ( l.getValue() == 1 or r.getValue() == 0 ):
			result.setValue( 1 )
		elif ( l.getValue() == 0 or r.getValue() == 1 ):
			result.setValue( 0 )
		elif ( l.getValue() == -1 and r.getValue() == -1 ):
			result.setValue( -1 )
		else:
			result.setValue( 0 )
		return (result)

	def opn_xor(self, l, r, facts):
		result = Fact(l.getName())
		if ( l.getValue() == -1 or r.getValue() == -1 ):
			result.setValue( -1 )
		elif ( l.getValue() == 1 ^ r.getValue() == 0 ):
			result.setValue( 1 )
		else:
			result.setValue( 0 )
		return (result)

	def addFact( self, char ):
		if isVar( char ):
			self.facts.append( char )

	def display( self ):
		print ( "{" + self.rule + "=>" + self.answer + " [" , end="" )
		for fact in self.facts:
			print ( ":"+fact, end="" )
		print ( "]}", end="\n" )

	def isOperator(self, string):
		operator = ['+', '|', '&', '^']
		if (string in operator):
			return (True)
		return (False)


	def calculAnswer( self, facts ):
		resolver = self.handleParentheses()
		tmpSubqueries = {}
		self.child = 0;

		# print ( str(resolver) )
		tmp = -1;
		for ( key, subquery ) in resolver.items():
			# print (str(resolver))
			tmp = self.calcul( key, facts )
			# print ("resolver result:" + str(tmp))
		return tmp

	def calcul( self, query, facts ):
		# print ("query:" + query)
		opposite = 0
		result = -1
		
		ptr = {
			"+": self.op_add,
			"|": self.op_or,
			"^": self.op_xor,
			"!+": self.opn_add,
			"!|": self.opn_or,
			"!^": self.opn_xor
		}
		op = "+"
		if len(query) == 1:
			# print( "pok" )
			result = facts[query].searchValue(facts)
		else:
			tmp = ""
			tmpFact = None
			for (i, x) in enumerate( str( query )):
				if x != "!" and self.isOperator( x ) == False and tmpFact is None:
					tmpFact = facts[x]
				# print ( "i:" + str(i) + " - " + x)
				if (self.isOperator( x ) == True ):
					op = x
				else :
					if ( x != "!" ):
						if ( opposite == 1 ):
							op = "!" + op
						if i > 0:
							result = ptr[op](tmpFact, facts[x], facts).getValue()
							# print ( str(tmpFact.getValue()) + " " + op + " " + str(facts[x].getValue()) + " = " + str(result))
							tmpFact.setValue(result)

						opposite = 0
						tmp = x;
					else :
						opposite = 1			
			tmpFact = result
		return result


	# def calcul():


	# def parseResolver(self, facts, resolver):
	# 	tmp = {}
	# 	tmpVarMap = facts
	# 	elem = None
	# 	self.child = 0

	# 	for (key, value) in resolver.items():
	# 		if (elem == None):
	# 			elem = key
	# 		for (i, query) in enumerate(value):
	# 			tmp[str(self.child)] = self.calcul(query, facts)
	# 			self.child += 1
	# 	for ( i, fact ) in tmp.items():
	# 		elem = str.replace(elem, "?", fact.getName(), 1)
	# 		tmpVarMap[fact.getName()] = var
	# 	return (self.calcul(elem, tmpVarMap))

	def handleParentheses( self ):
		resultold = self.rule
		result = self.rule
		i = 0
		regexp = "(\((!?([A-Z]|\?)[+^|]){1,}!?([A-Z]|\?)\))"

		while ( result != re.sub(regexp, "?", result)):
			result = re.sub(regexp, "?", result)
		tmp_final = result
		resolver = {result:[]}
		result = resultold

		while ( result != re.subn(regexp, "?", result, count=1)[0] ):
			pos = re.search(regexp, result)
			tmp = result[pos.start() + 1:pos.end() - 1]
			result = re.subn(regexp, "?", result, count=1)[0]
			resolver[tmp_final].append(tmp)

		return resolver
