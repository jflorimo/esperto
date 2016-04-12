# @Author: jflorimo
# @Date:   2016-04-10 12:50:30
# @Last Modified by:   jflorimo
# @Last Modified time: 2016-04-11 20:15:27

from __future__ import print_function
from parsing import isVar
import re

class Rule( object ):

	def __init__( self, ruleQuery, answer ):
		self.rule = ruleQuery;
		self.answer = answer
		self.facts = []
		for char in self.rule:
			self.addFact(char)


	#GETTER && SETTER
	def getRule( self ):
		return ( self.rule )
	def getAnswer( self ):
		return ( self.answer )

	#METHODS
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
		for (key, value) in resolver.items():
			print ( str(key) + ":" + str(value) )

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
