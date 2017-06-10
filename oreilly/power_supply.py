plants = {}

def power_supply(network, power_plants):
    plants = power_plants
    result = []
    cities = set([obj for connection in network for obj in connection if plants.get(obj) is None])

    for plant in power_plants:
        power = power_plants.get(plant)
        supplied = supply_objects(plant, network[:], power, [])
        result.extend(supplied)

    result = set(result)
    return cities.difference(result)

def supply_objects(current_object, network, power, supplied):
    if power == 0 or len(network) == 0:
        return supplied
    else:
        power -= 1

    connected = connected_objects(current_object, network)
    supplied.extend(connected)
    for obj in connected:
        return supply_objects(obj, network, power, supplied)

def connected_objects(current_object, network):
    object_connections = [connection for connection in network if current_object in connection]
    for connection in object_connections:
        network.remove(connection)

    objects = []
    for connection in object_connections:
        if connection[0] != current_object:
            objects.append(connection[0])
        elif plants.get(connection[1]) is None:
            objects.append(connection[1])

    return objects


if __name__ == '__main__':
    assert power_supply([['p1', 'c1'], ['c1', 'c2']], {'p1': 1}) == set(['c2']), 'one blackout'
    assert power_supply([['c0', 'c1'], ['c1', 'p1'], ['c1', 'c3'], ['p1', 'c4']], {'p1': 1}) == set(['c0', 'c3']), 'two blackout'
    assert power_supply([['p1', 'c1'], ['c1', 'c2'], ['c2', 'c3']], {'p1': 3}) == set([]), 'no blackout'
    assert power_supply([['c0', 'p1'], ['p1', 'c2']], {'p1': 0}) == set(['c0', 'c2']), 'weak power-plant'
    assert power_supply([['p0', 'c1'], ['p0', 'c2'], ['c2', 'c3'], ['c3', 'p4'], ['p4', 'c5']], {'p0': 1, 'p4': 1}) == set([]), 'cooperation'
    assert power_supply([['c0', 'p1'], ['p1', 'c2'], ['c2', 'c3'], ['c2', 'c4'], ['c4', 'c5'],
                         ['c5', 'c6'], ['c5', 'p7']],
                        {'p1': 1, 'p7': 1}) == set(['c3', 'c4', 'c6']), 'complex cities 1'
    assert power_supply([['p0', 'c1'], ['p0', 'c2'], ['p0', 'c3'],
                         ['p0', 'c4'], ['c4', 'c9'], ['c4', 'c10'],
                       ['c10', 'c11'], ['c11', 'p12'], ['c2', 'c5'],
                       ['c2', 'c6'], ['c5', 'c7'], ['c5', 'p8']],
                      {'p0': 1, 'p12': 4, 'p8': 1}) == set(['c6', 'c7']), 'complex cities 2'
    assert power_supply([['c1', 'c2'], ['c2', 'c3']], {}) == set(['c1', 'c2', 'c3']), 'no power plants'
    assert power_supply([['p1', 'c2'], ['p1', 'c4'], ['c4', 'c3'], ['c2', 'c3']], {'p1': 1}) == set(['c3']), 'circle'
    assert power_supply([['p1', 'c2'], ['p1', 'c4'], ['c2', 'c3']], {'p1': 4}) == set([]), 'more than enough'
    print("Looks like you know everything. It is time for 'Check'!")