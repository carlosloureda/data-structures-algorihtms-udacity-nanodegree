from math import pow, sqrt
import heapq

from collections import namedtuple

# needed to use namedtuples for our paths as with dictionaries I had problems

Cost = namedtuple('Cost', ['total', 'journey', 'to_goal'])
Path = namedtuple('Path', ['cost', 'intersections',
                           'previous', 'frontier'])


def euclidean_distance(origin: [float, float], destination: [float, float]) -> float:
    """
    In mathematics, the Euclidean distance or Euclidean metric is the "ordinary" straight-line distance
    between two points in Euclidean space. With this distance, Euclidean space becomes a metric space.
    https://en.wikipedia.org/wiki/Euclidean_distance
    We follow the option for the "Two dimesions": d(p,q) = sqrt[(q1 - p1)^2 + (q2 - p2)^2]
    Being p = (p1+p2) and q = (q1+q2)
    :param origin: origin point, with (x, y) coordinates (2D)
    :param destination: destination point, with (x, y) coordinates (2D)
    :return: euclidean distance
    """
    x_element = pow(destination[0] - origin[0], 2)
    y_element = pow(destination[1] - origin[1], 2)
    return sqrt(x_element + y_element)


def heuristic_distance(from_point: [float, float], goal_point: [float, float]) -> float:
    """
    Estimates the distance between the current path frontier point and the goal. Accomplished the A* optimization
    requirement of having an estimating function that underestimates. As in a 2D-Cartesian space, the straight line is
    always the smallest possible distance between two points; guaranteeing the "underestimation" requirement
    :param from_point: The point from where we want to calculate the heuristic distance
    :param goal_point: The goal point to where we want to calculate the heuristic distance
    :return: heuristic (H) or estimated distance from from_point to goal_point.
    """
    return euclidean_distance(from_point, goal_point)


def path_update(map: object, path: object, frontier: int, goal: int):
    from_point = map.intersections[path.frontier]
    to_point = map.intersections[frontier]

    new_distance = euclidean_distance(from_point, to_point)
    cost_journey = path.cost.journey + new_distance
    cost_to_goal = heuristic_distance(to_point, map.intersections[goal])
    cost_total = cost_journey + cost_to_goal
    intersections = path.intersections + [frontier]

    new_path = Path(
        Cost(cost_total, cost_journey, cost_to_goal),
        intersections,
        path.frontier,
        frontier
    )

    return new_path


def shortest_path(map: object, start: int, goal: int) -> list:

    if start == goal:  # we are there :)
        return [start]

    heuristic_distance_to_goal = heuristic_distance(
        map.intersections[start],  map.intersections[goal])

    # Initial Path

    path = Path(
        Cost(heuristic_distance_to_goal, 0, heuristic_distance_to_goal),
        [start],
        start,
        start
    )

    paths = list()
    heapq.heappush(paths, path)

    path_to_goal_min_val = float('inf')
    path_to_goal_min = -1

    while len(paths) >= 1:
        nearest_path = heapq.heappop(paths)

        for closest_road in map.roads[nearest_path.frontier]:
            if closest_road != nearest_path.previous:  # not going backwards
                new_path = path_update(map, nearest_path, closest_road, goal)

                # Reached destination with a path
                if closest_road == goal:
                    # Better than previous path
                    if new_path.cost.total < path_to_goal_min_val:
                        path_to_goal_min_val = new_path.cost.total
                        path_to_goal_min = new_path.intersections

                # Destination not reached
                else:
                    # Previously found the goal with a path
                    if path_to_goal_min is not None:
                        # Cheaper path, keep exploring
                        if new_path.cost.total < path_to_goal_min_val:
                            heapq.heappush(paths, new_path)
                    # Not yet found the goal, keep exploring
                    else:
                        heapq.heappush(paths, new_path)

    return path_to_goal_min
