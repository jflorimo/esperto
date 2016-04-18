# -*- coding: utf-8 -*-
# @Author: jflorimo
# @Date:   2016-04-18 13:45:55
# @Last Modified by:   jflorimo
# @Last Modified time: 2016-04-18 15:21:38

from graphviz import Digraph


def generateGraph( facts, input, output ):
	dot = Digraph(comment='expert_system')
	dot.strict = True

	for fact in sorted(facts):
		dot.attr('node', shape='circle')
		dot.node(fact)
		for rule in facts[fact].getRules():
			dot.attr('node', shape='box')
			dot.node(rule.getRule())

	for fact in sorted(facts):
		for rule in facts[fact].getRules():
			dot.edge(rule.getRule(),fact)
			for factFromRule in rule.getFacts():
				dot.edge(factFromRule, rule.getRule())


	print(dot.source)
	dot.render('output', view=True)