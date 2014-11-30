
#pragma once

#include "field.h"
#include "map.h"
#include <list>
#include <boost/shared_ptr.hpp>

namespace pf
{

class Node;
typedef  boost::shared_ptr<Node>  LPNode;
typedef  std::list<LPNode>        NodeList;

class Node
{
public:
	Node(LPField field);

	LPField        field;
	LPNode         parent;
	NodeList       child;

	bool operator== (const LPField& field) const;
	bool operator== (const LPNode& node) const;
	bool operator== (const Node& node) const;

	bool isParentPosition(int x, int y) const;

	int  calcGFromParent(const LPNode& parent) const;
	int  calcH  (const LPNode& other) const;
	void setCost(int g, int h);
};

} // namespace pf