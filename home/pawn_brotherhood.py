#!/usr/bin/env python3

VERTICALS = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h')
PAWN_ATTACK_SIDES = ('left', 'right')

def safe_pawns(pawns):
    safed_pawns_count = 0

    protected_cells = find_protected_cells(pawns)
    for pawn in pawns:
        if pawn in protected_cells:
            safed_pawns_count += 1
    return safed_pawns_count

def find_protected_cells(pawns):
    vertical_index = 0
    protected_cells = []
    white_pawn_attack_horizontal = 0

    for pawn in pawns:
        vertical_index = VERTICALS.index(pawn[0])

        for attack_side in PAWN_ATTACK_SIDES:
            if vertical_index == 0 and attack_side == PAWN_ATTACK_SIDES[0]:
                continue
            elif vertical_index == len(VERTICALS) - 1 and attack_side == PAWN_ATTACK_SIDES[1]:
                continue

            white_pawn_attack_horizontal = str((int(pawn[1]) + 1))

            if attack_side == PAWN_ATTACK_SIDES[0]:
                protected_cells.append(VERTICALS[vertical_index - 1] + white_pawn_attack_horizontal)
            else:
                protected_cells.append(VERTICALS[vertical_index + 1] + white_pawn_attack_horizontal)

    return set(protected_cells)


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert safe_pawns({"b4", "d4", "f4", "c3", "e3", "g5", "d2"}) == 6
    assert safe_pawns({"b4", "c4", "d4", "e4", "f4", "g4", "e5"}) == 1
