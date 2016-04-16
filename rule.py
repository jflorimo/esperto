# @Author: jflorimo
# @Date:   2016-04-10 12:50:30
# @Last Modified by:   jflorimo
# @Last Modified time: 2016-04-16 18:10:04

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
	def handleFactForParentheses(self, fact):
		tmp = None
		if fact == 1 or fact == 0:
			tmp = Fact("-")
			tmp.setValue(b)
			return tmp
		else:	
			tmp = fact
		return tmp

	def op_add(self, l, r, facts):
		return (l.op_add(r, facts))

	def op_or(self, l, r, facts):
		return (l.op_or(r, facts))

	def op_xor(self, l, r, facts):
		return (l.op_xor(r, facts))


	def opn_add(self, l, r, facts):
		l = self.handleFactForParentheses(l)
		r = self.handleFactForParentheses(r)
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
		l = self.handleFactForParentheses(l)
		r = self.handleFactForParentheses(r)
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
		l = self.handleFactForParentheses(l)
		r = self.handleFactForParentheses(r)
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

	def isOperator( self, string ):
		operator = ['+', '|', '&', '^']
		if (string in operator):
			return (True)
		return (False)

	def getPriority( self, char ):
		operators = ['^', '|', '+'] # priority
		for ( i, op ) in enumerate( operators ):
			if op == char:
				return i
		return None

	def calculAnswer( self, facts ):
		# print (str(self.rule))

		stack = []
		query = []
		oposite = False
		for x in self.rule:
			if (x == '('):
				stack.append(x)
			elif (x == ')'):
				while (stack[len(stack)-1] != '('):
					query.append( stack.pop() )
				stack.pop()
			elif (x == '!'):
				oposite = True
			elif (oposite == True):
				query.append("!"+x)
				oposite = False
			elif (self.isOperator(x) == True):
				# print( "stack:"+ str(stack) + "x:"+x + str(len(stack)) )
				if (len(stack) == 0):
					stack.append(x)
				else:
					peek = stack[len(stack)-1]
					if ( self.getPriority( x ) <=  self.getPriority( stack[ len( stack ) - 1 ] ) ):
						query.append( stack.pop() )
						stack.append(x)
					else: 
						stack.append(x)
			else:
				query.append(x)
		# pop stack
		while (len(stack) > 0):
			query.append( stack.pop() )

		
		return self.calcul(query, facts)

	def getNextOperatorIndexInQuery(self, query):
		for (i,x) in enumerate(query):
			if (self.isOperator(x)):
				return i
		return -1;

	def calcul(self, query, facts):
		ptr = {
			"+": self.op_add,
			"|": self.op_or,
			"^": self.op_xor,
			"!+": self.opn_add,
			"!|": self.opn_or,
			"!^": self.opn_xor
		}
		# print("Query:" + str( query ))


		index = self.getNextOperatorIndexInQuery(query)
		
		while (index != -1):
			# print()
			# print ("index="+str(index))
		 	l = query[index-2]
		 	r = query[index-1]
		 	op = query[index]

		 	# print( l+" "+op+" "+r )
		 	left = None
		 	right = None
		 	if (l[0] == '!'):
		 		tmpFact = Fact(l[1])
				if (l[1] != '0' and l[1] != '1'):
					tmpFact.setValue( facts[l[1]].searchValue(facts))
		 		if (tmpFact.getValue() == 0):
		 			tmpFact.setValue(1)
		 		else:
		 			tmpFact.setValue(0)
		 		left = tmpFact
		 	else:
			 	left = Fact(l) if (l == '0' or l == '1') else facts[l]
			
			if (r[0] == '!'):
				tmpFact = Fact(r[1])
				if (r[1] != '0' and r[1] != '1'):
					tmpFact.setValue( facts[r[1]].searchValue(facts))

		 		if (tmpFact.getValue() == 0):
		 			tmpFact.setValue(1)
		 		else:
		 			tmpFact.setValue(0)
		 		right = tmpFact

			else:
 				right = Fact(r) if (r == '0' or r == '1') else facts[r]

		 	# print("Query1:" + str( query ) +"result="+query[index])

		 	query[index] = str(ptr[op](left, right, facts).getValue())
		 	# print("Query2:" + str( query ) +"result="+query[index])
		 	# print("peek-2:"+query[index-2] + "peek1" + query[index-1] )
		 	query.pop(index-2)
		 	query.pop(index-1 -1)
		 	index = self.getNextOperatorIndexInQuery(query)
		 	# print("new query:" + str( query ) )

		if (query[0] == '0'):
			return 0
		elif (query[0] == '1'):
			return 1
		return facts[query[0]].searchValue(facts)


		# result






	
