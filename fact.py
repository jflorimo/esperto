# @Author: jflorimo
# @Date:   2016-04-10 12:42:02
# @Last Modified by:   jflorimo
# @Last Modified time: 2016-04-10 19:14:12

class Fact( object ):

	def __init__( self, name ):
		self.name = name
		self.value = 0
		self.rules = []


	#GETTER && SETTER
	def setValue( self, value ):
		self.value = value

	def addRule( self, rule ):
		self.rules.append( rule )

	def getValue( self ):
		return ( self.value )

	def getName( self ):
		return ( self.name )

	#METHODS
	def display( self ):
		print "["+self.name+ ":" + str( self.value ) + "]"
