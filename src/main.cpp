#include "map.h"
#include "node.h"
#include "path_finding.h"
#include <iostream>
#include <boost/assert.hpp> 
#include <boost/assign/list_inserter.hpp>

pf::Map generateMap()
{
	std::vector<int> q0, q1, q2, q3, q4, q5, q6, q7, q8, q9;

	boost::assign::push_back(q0) (1)(1)(1)(1)(1)(9)(1)(1)(1)(1);
	boost::assign::push_back(q1) (1)(1)(1)(1)(1)(9)(1)(1)(1)(1);
	boost::assign::push_back(q2) (1)(1)(9)(9)(9)(9)(9)(9)(9)(1);
	boost::assign::push_back(q3) (1)(1)(1)(1)(1)(1)(1)(1)(9)(1);
	boost::assign::push_back(q4) (9)(9)(9)(9)(9)(9)(9)(1)(9)(1);
	boost::assign::push_back(q5) (1)(1)(1)(1)(1)(1)(9)(1)(9)(1);
	boost::assign::push_back(q6) (1)(1)(1)(1)(9)(9)(9)(1)(9)(1);
	boost::assign::push_back(q7) (1)(1)(1)(1)(1)(1)(1)(1)(9)(1);
	boost::assign::push_back(q8) (1)(1)(1)(1)(9)(9)(9)(9)(9)(1);
	boost::assign::push_back(q9) (1)(1)(1)(1)(1)(1)(1)(1)(1)(1);

	std::vector< std::vector<int> > fieldMap;
	boost::assign::push_back(fieldMap)
		(q0)(q1)(q2)(q3)(q4)(q5)(q6)(q7)(q8)(q9)
	;

	pf::Map map(fieldMap);
	return map;
}

void main()
{
	pf::Map map = generateMap();

	pf::LPNode nodeStart(new pf::Node(map.getField(0, 3)));
	pf::LPNode nodeStop (new pf::Node(map.getField(9, 3)));

	std::cout << "before" << std::endl;
	pf::PathFinding::print(map, nodeStart, nodeStop, pf::NodeList());

	pf::NodeList path = pf::PathFinding::search(map, nodeStart, nodeStop);

	std::cout << std::endl << "after" << std::endl;
	pf::PathFinding::print(map, nodeStart, nodeStop, path);
	std::cout << std::endl;
}
