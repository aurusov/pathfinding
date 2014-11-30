#include "path_finding.h"
#include <iostream>
#include <boost/foreach.hpp>

namespace pf
{

NodeList PathFinding::search(
	const Map&    map,
	const LPNode& nodeStart,
	const LPNode& nodeStop)
{
	NodeList path;

	for (int y = 0; y < map.getHeight(); y++)
	{
		for (int x = 0; x < map.getWidth(); x++)
		{
			LPField field = map.getField(x, y);
			field->closed = false;
			field->node_cost = Field::NodeCost();
		}
	}

	NodeList open;

	nodeStart->setCost(0, nodeStart->calcH(nodeStop));
	open.push_back(nodeStart);

	while (!open.empty())
	{
		LPNode node = getBest(open);

		if (*node == nodeStop->field)
		{
			path = reconstructPath(node);
			break;
		}

		open.remove(node);
		node->field->closed = true;

		NodeList childList = createChild(node, map);

		BOOST_FOREACH(const LPNode& child, childList)
		{
			int tentative_g_score = node->field->node_cost.g + child->calcGFromParent(node);

			NodeList::iterator openIt = open.begin();
			while (openIt != open.end())
			{
				if (**openIt == child)
				{
					break;
				}
				++openIt;
			}
			if (openIt != open.end())
			{
				if (tentative_g_score < (*openIt)->field->node_cost.g)
				{
					LPNode parent = (*openIt)->parent;
					parent->child.remove(*openIt);
					open.erase(openIt);
				}
				else
				{
					continue;
				}
			}

			child->parent = node;
			node->child.push_back(child);

			child->setCost(tentative_g_score, child->calcH(nodeStop));
			open.push_back(child);
		}
	}

	return path;
}

LPNode PathFinding::getBest(const NodeList& nodeList)
{
	NodeList::const_iterator it = nodeList.begin();
	LPNode result = *it;
	++it;
	while (it != nodeList.end())
	{
		if ((*it)->field->node_cost.f < result->field->node_cost.f)
		{
			result = *it;
		}
		++it;
	}
	return result;
}

NodeList PathFinding::reconstructPath(LPNode node)
{
	NodeList path;

	while (node->parent)
	{
		path.push_front(node);
		node = node->parent;
	}
	path.push_front(node);

	return path;
}

NodeList PathFinding::createChild(const LPNode& node, const Map& map)
{
	NodeList nodeList;
	LPNode child;

	child = createChild(node, map, node->field->x + 1, node->field->y);
	if (child)
	{
		nodeList.push_back(child);
	}
	child = createChild(node, map, node->field->x - 1, node->field->y);
	if (child)
	{
		nodeList.push_back(child);
	}
	child = createChild(node, map, node->field->x, node->field->y + 1);
	if (child)
	{
		nodeList.push_back(child);
	}
	child = createChild(node, map, node->field->x, node->field->y - 1);
	if (child)
	{
		nodeList.push_back(child);
	}
	child = createChild(node, map, node->field->x + 1, node->field->y + 1);
	if (child)
	{
		nodeList.push_back(child);
	}
	child = createChild(node, map, node->field->x - 1, node->field->y - 1);
	if (child)
	{
		nodeList.push_back(child);
	}
	child = createChild(node, map, node->field->x + 1, node->field->y - 1);
	if (child)
	{
		nodeList.push_back(child);
	}
	child = createChild(node, map, node->field->x - 1, node->field->y + 1);
	if (child)
	{
		nodeList.push_back(child);
	}

	return nodeList;
}

LPNode PathFinding::createChild(const LPNode& node, const Map& map, int x, int y)
{
	if (0 <= x && x < map.getWidth() &&
		0 <= y && y < map.getHeight())
	{
		if (!node->isParentPosition(x, y))
		{
			LPField field = map.getField(x, y);
			if (!field->isBlocked() && !field->closed)
			{
				LPNode child(new Node(field));
				return child;
			}
		}
	}

	return LPNode();
}

void PathFinding::print(
		const Map& map,
		const LPNode& nodeStart,
		const LPNode& nodeStop,
		const NodeList& path)
{
	for (int y = 0; y < map.getHeight(); y++)
	{
		std::cout << "    ";
		for (int x = 0; x < map.getWidth(); x++)
		{
			LPField field = map.getField(x, y);
			if (*field == *nodeStart->field)
			{
				std::cout << "  o";
			}
			else if (*field == *nodeStop->field)
			{
				std::cout << "  k";
			}
			else if (field->isBlocked())
			{
				std::cout << "###";
			}
			else
			{
				bool found = false;
				BOOST_FOREACH(const LPNode& node, path)
				{
					if (*field == *node->field)
					{
						found = true;
						break;
					}
				}
				if (found)
				{
					std::cout << " + ";
				}
				else
				{
					std::cout.width(3);
					std::cout << field->node_cost.g;
				}
			}
		}
		std::cout << std::endl;
	}
}

}
