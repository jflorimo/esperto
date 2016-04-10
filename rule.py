# @Author: jflorimo
# @Date:   2016-04-10 12:50:30
# @Last Modified by:   jflorimo
# @Last Modified time: 2016-04-10 18:45:14

class Rule( object ):

	def __init__( self, rule, answer ):
		self.rule = rule;
		self.answer = answer
		self.facts = []

	#GETTER && SETTER
	def getSolution(self):
		return ( self.solution )
	def getResult(self):
		return ( self.right )