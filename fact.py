# @Author: jflorimo
# @Date:   2016-04-10 12:42:02
# @Last Modified by:   jflorimo
# @Last Modified time: 2016-04-11 20:16:25

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

	def getRules( self ):
		return ( self.rules )

	# OPERATOR OVERLOADING
	def op_add(self, b, facts):
		tmp = Fact(self.name)
		if (self.searchValue(varMap) == 1 and b.searchValue(varMap) == 1):
			tmp.setValue(1)
		elif ( self.searchValue(varMap) == 0 or b.searchValue(varMap) == 0 ):
			tmp.setValue(0)
		elif ( self.searchValue(varMap) == -1 or b.searchValue(varMap) == -1 ) :
			tmp.setValue(-1)
		else:
			tmp.setValue(0)
		return (tmp)

	def op_xor(self, b, facts):
		tmp = Fact(self.name)
		if ( self.searchValue(varMap) == -1 or b.searchValue(varMap) == -1 ) :
			tmp.setValue(-1)
		elif (self.searchValue(varMap) ^ b.searchValue(varMap)):
			tmp.setValue(1)
		else:
			tmp.setValue(0)
		return (tmp)

	def op_or(self, b, facts):
		tmp = Fact(self.name)
		if (self.searchValue(varMap) == 1 or b.searchValue(varMap) == 1):
			tmp.setValue(1)
		elif ( self.searchValue(varMap) == 0 or b.searchValue(varMap) == 0 ):
			tmp.setValue(0)
		elif ( self.searchValue(varMap) == -1 and b.searchValue(varMap) == -1 ) :
			tmp.setValue(-1)
		else:
			tmp.setValue(0)
		return (tmp)

	#METHODS
	def display( self ):
		print "["+self.name+ ":" + str( self.value ) + "]"
		# for rule in self.rules:
		# 	rule.display()

	def searchValue( self, factsMap ):
		if len(self.rules) > 0:
			for rule in self.rules:
				rule.calculAnswer( factsMap )
		else:
			return self.value

