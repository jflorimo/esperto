# @Author: jflorimo
# @Date:   2016-04-10 12:50:30
# @Last Modified by:   jflorimo
# @Last Modified time: 2016-04-10 18:45:14

from __future__ import print_function
from parsing import isVar

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