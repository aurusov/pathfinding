#include "node.h"

namespace pf
{

Node::Node(LPField field)
	: field(field)
{}

bool Node::operator== (const LPField& field) const
{
	return *this->field == *field;
}

bool Node::operator== (const LPNode& node) const
{
	return *this->field == *node->field;
}

bool Node::operator== (const Node& node) const
{
	return *this->field == *node.field;
}

bool Node::isParentPosition(int x, int y) const
{
	if (!parent)
		return false;

	return parent->field->x == x && parent->field->y == y;
}

int Node::calcGFromParent(const LPNode& parent) const
{
	//bool diagonal = parent->field->x != field->x && parent->field->y != field->y;
	//return diagonal ? 3 : 2;
	return field->map_cost;
}

int Node::calcH(const LPNode& other) const
{
	return abs(field->x - other->field->x) + abs(field->y - other->field->y);
}

void Node::setCost(int g, int h)
{
	field->node_cost.g = g;
	field->node_cost.h = h;
	field->node_cost.f = field->node_cost.g + field->node_cost.h;
}

} // namespace pf
