
#pragma once

#include <ostream>
#include <boost/shared_ptr.hpp>

namespace pf
{

struct Field
{
	struct NodeCost
	{
		int f;
		int g;
		int h;

		NodeCost();
	};

	unsigned int map_cost;
	int x;
	int y;
	bool closed;
	NodeCost node_cost;

	Field();
	Field(unsigned int cost, int x, int y);

	bool isBlocked() const;
	bool operator== (const Field& other) const;
};

typedef  boost::shared_ptr<Field>  LPField;

} // namespace pf
