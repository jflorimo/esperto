# @Author: jflorimo
# @Date:   2016-04-10 12:50:30
# @Last Modified by:   jflorimo
# @Last Modified time: 2016-04-10 13:25:01

class Rule( object ):

	def __init__( self, rule, answer ):
		self.rule = rule;
		self.answer = answer

	#GETTER && SETTER
	def getSolution(self):
		return ( self.solution )
	def getResult(self):
		return ( self.right )