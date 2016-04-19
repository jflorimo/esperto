# @Author: jflorimo
# @Date:   2016-04-10 12:42:02
# @Last Modified by:   jflorimo
# @Last Modified time: 2016-04-16 16:24:24

class Fact( object ):

	def __init__( self, name ):
		self.name = name
		self.value = 0
		self.rules = []
		self.isCalculated = False
		if (name == '1' or self.value == 1):
			self.value = 1
			self.isCalculated == True

	#GETTER && SETTER
	def setValue( self, value ):
		self.value = value
		if (value == 1):
			self.isCalculated == True

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
		# if b == 1 or b == 0:
		# 	tmp = Fact("-")
		# 	tmp.setValue(b)
		# else:	
		# 	tmp = Fact(self.name)
		tmp = Fact(self.name)
		if (self.searchValue(facts) == 1 and b.searchValue(facts) == 1):
			tmp.setValue(1)
		elif ( self.searchValue(facts) == 0 or b.searchValue(facts) == 0 ):
			tmp.setValue(0)
		elif ( self.searchValue(facts) == -1 or b.searchValue(facts) == -1 ) :
			tmp.setValue(-1)
		else:
			tmp.setValue(0)
		return (tmp)

	def op_xor(self, b, facts):
		# if b == 1 or b == 0:
		# 	tmp = Fact("-")
		# 	tmp.setValue(b)
		# else:	
		# 	tmp = Fact(self.name)
		tmp = Fact(self.name)
		if ( self.searchValue(facts) == -1 or b.searchValue(facts) == -1 ) :
			tmp.setValue(-1)
		elif (self.searchValue(facts) ^ b.searchValue(facts)):
			tmp.setValue(1)
		else:
			tmp.setValue(0)
		return (tmp)

	def op_or(self, b, facts):
		# if b == 1 or b == 0:
		# 	tmp = Fact("-")
		# 	tmp.setValue(b)
		# else:	
		# 	tmp = Fact(self.name)
		tmp = Fact(self.name)
		if (self.searchValue(facts) == 1 or b.searchValue(facts) == 1):
			tmp.setValue(1)
		elif ( self.searchValue(facts) == 0 or b.searchValue(facts) == 0 ):
			tmp.setValue(0)
		elif ( self.searchValue(facts) == -1 and b.searchValue(facts) == -1 ) :
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
		if len(self.rules) > 0 and self.isCalculated == False and self.value != 1:
			tmp = -1
			for ( i, rule ) in enumerate( self.rules ):

				tmp = rule.calculAnswer( factsMap )
				# print "loop:" + str( i ) + " result: " + str(tmp)
				if (tmp == 1):
					self.isCalculated = True
					self.value = 1
					return tmp
			return tmp
		else:
			return self.value
		# 	# print "number of rules: " + str( len( self.rules ) ) 
		# 	tmp = -1
		# 	for ( i, rule ) in enumerate(self.rules):
		# 		tmp = rule.calculAnswer( factsMap )
		# 		# print "loop:" + str( i ) + " result: " + str( i )
		# 	return tmp
		# else:
		# 	return self.value

