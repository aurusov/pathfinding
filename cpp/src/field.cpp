#include "field.h"

namespace pf
{

Field::NodeCost::NodeCost()
	: f(0)
	, g(0)
	, h(0)
{}

Field::Field()
	: map_cost(0)
	, x(0)
	, y(0)
	, closed(false)
{}

Field::Field(unsigned int cost, int x, int y)
	: map_cost(cost)
	, x(x)
	, y(y)
	, closed(false)
{}

bool Field::isBlocked() const
{
	return map_cost == 9;
}

bool Field::operator== (const Field& other) const
{
	return x == other.x
		&& y == other.y;
}

} // namespace pf
