
#pragma once

#include <ostream>
#include <vector>
#include "field.h"

namespace pf
{

class Map
{
public:
	typedef  std::vector< std::vector<LPField> >  FieldMap;

	Map(const std::vector< std::vector<int> >& arrayValue);
	virtual ~Map();

	const FieldMap& map() const;
	LPField getField(int x, int y) const;
	int getWidth () const;
	int getHeight() const;

private:
	FieldMap fieldMap;
	int width;
	int height;
};

} // namespace pf
