
#include "map.h"
#include <boost/iostreams/copy.hpp>

namespace pf
{

Map::Map(const std::vector< std::vector<int> >& arrayValue)
	: width(0)
	, height(0)
{
	if (arrayValue.empty())
		return;

	width  = arrayValue[0].size();
	height = arrayValue.size();
	for (int y = 0; y < height; ++y)
	{
		BOOST_ASSERT(arrayValue[y].size() == width);
		fieldMap.push_back(std::vector<LPField>());
		for (int x = 0; x < width; ++x)
		{
			LPField field(new Field(arrayValue[y][x], x, y));
			fieldMap.back().push_back(field);
		}
	}
}

Map::~Map()
{}

const Map::FieldMap& Map::map() const
{
	return fieldMap;
}

int Map::getWidth() const
{
	return width;
}

int Map::getHeight() const
{
	return height;
}

LPField Map::getField(int x, int y) const
{
	return fieldMap[y][x];
}

} // namespace
