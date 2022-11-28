move_dict = {"00C000": [1, 0], "C0FFC0": [-1, 0], "C00000": [-1, 0], "FFFFFF": [0, 0], "C0C000": [0, 1],
             "FFFFC0": [0, -1], "FFC0C0": [1, 0], "C0C0FF": [0, 1], "0000C0": [0, -1]}


def calculate_final_vector(coord_tuple, hex_list):
    coord_list = []
    coord_list.append(coord_tuple[0])
    coord_list.append(coord_tuple[1])
    for code in hex_list:
        if code.upper() == '000000':
            print(tuple(coord_list))
            break
        else:
            for key in move_dict:
                if code.upper() == key:
                    new_coord = move_dict.get(code.upper())
                    coord_list[0] += new_coord[0]
                    coord_list[1] += new_coord[1]
                    break
    return (tuple(coord_list))


