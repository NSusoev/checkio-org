def checkio(teleports_str):
    #return any route from 1 to 1 over all points
    connections = [tuple(sorted([int(x) - 1, int(y) - 1])) for x, y in teleports_str.split(",")]
    path = hamilton_path(0, [], connections)
    result = list(map(lambda x: str(x + 1), path))
    print(result)
    return "".join(result)

def hamilton_path(current_station, path, connections):
    path.append(current_station)
    if len(set(path)) == 8 and current_station == 0:
        return path

    moves = available_moves(current_station, connections)
    for i in range(len(moves)):
        move = None
        if (move_destination(current_station, moves[0]) == 0 and
            len(moves) == 1) or move_destination(current_station, moves[0]) != 0:
            move = moves.pop(0)
            connections.remove(move)
        elif move_destination(current_station, moves[0]) == 0 and len(moves) > 1:
            move = moves.pop(1)
            connections.remove(move)

        if hamilton_path(move_destination(current_station, move), path, connections):
            return path

def available_moves(current_station, connections):
    return [move for move in connections if current_station in move]

def move_destination(current_station, move):
    if move[0] != current_station:
        return move[0]
    else:
        return move[1]


#This part is using only for self-testing
if __name__ == "__main__":
    def check_solution(func, teleports_str):
        route = func(teleports_str)
        teleports_map = [tuple(sorted([int(x), int(y)])) for x, y in teleports_str.split(",")]
        if route[0] != '1' or route[-1] != '1':
            print("The path must start and end at 1")
            return False
        ch_route = route[0]
        for i in range(len(route) - 1):
            teleport = tuple(sorted([int(route[i]), int(route[i + 1])]))
            if not teleport in teleports_map:
                print("No way from {0} to {1}".format(route[i], route[i + 1]))
                return False
            teleports_map.remove(teleport)
            ch_route += route[i + 1]
        for s in range(1, 9):
            if not str(s) in ch_route:
                print("You forgot about {0}".format(s))
                return False
        return True

    assert check_solution(checkio, "12,23,34,45,56,67,78,81"), "First"
    assert check_solution(checkio, "12,28,87,71,13,14,34,35,45,46,63,65"), "Second"
    assert check_solution(checkio, "12,15,16,23,24,28,83,85,86,87,71,74,56"), "Third"
    assert check_solution(checkio, "13,14,23,25,34,35,47,56,58,76,68"), "Fourth"