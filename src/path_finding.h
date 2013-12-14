
#pragma once

#include "map.h"
#include "node.h"

namespace pf
{

class PathFinding
{
public:
	static NodeList search(
		const Map&    map,
		const LPNode& nodeStart,
		const LPNode& nodeStop
	);

	static void print(
		const Map&      map,
		const LPNode&   nodeStart,
		const LPNode&   nodeStop,
		const NodeList& path
	);

private:
	static LPNode getBest(const NodeList& nodeList);
	static NodeList reconstructPath(LPNode node);
	static NodeList createChild(const LPNode& node, const Map& map);
	static LPNode   createChild(const LPNode& node, const Map& map, int x, int y);
};

} // namespace pf
