import re
# from var_solution import VarSolution
from parsing import getRuleRegex
# from parsing import isVar


def init_factsValue(facts, input):
	for char in input:
		facts[char].setValue(1)

# def isResultQueryUndefined(resultQuery):
# 	for char in resultQuery:
# 		if char == "^" or char == "|":
# 			return True
# 	return False

def init_factsRules(facts, rules):
	for rule in rules:
		regex = re.search(getRuleRegex(), rule)
		# print("Solution: " + regex.group(1) + " cr: " + regex.group(5) + "result: "+ regex.group(6))
		setFactRules(facts, regex.group(1), regex.group(5), regex.group(6))

def setFactRules(facts, rule, comparator, answer):
	print("Solution: " + rule + " comp: " + comparator + "result: "+ answer)
# def setVarsSolution(vars, solutionQuery, resultQuery, boolean):
# 	if not isResultQueryUndefined(resultQuery):
# 		for char in resultQuery:
# 			if isVar(char):
# 				solution = VarSolution(solutionQuery, resultQuery, char)
# 				if not boolean:
# 					vars[char].setSolutionQuery(solution)
# 				else:
# 					vars[char].setSolutionQueryAtBegin(solution)

# def setVarsData(vars, solution, comparator, result):
# 	if comparator == "<=>":
# 		setVarsSolution(vars, solution, result, True)
# 		setVarsSolution(vars, result, solution, True)
# 	else:
# 		setVarsSolution(vars, solution, result, False)




# def init_varsQueries(vars, queries):
# 	for query in queries:
# 		regex = re.search(getQueryRegex(), query)
# # print("Solution: " + regex.group(1) + " cr: " + regex.group(5) + "result: "+ regex.group(6))
# 		setVarsData(vars, regex.group(1), regex.group(5), regex.group(6))
		