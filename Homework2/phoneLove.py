three_letters_dict = {2: ['a', 'b', 'c'], 3: ['d', 'e', 'f'], 4: ['g', 'h', 'i'],
                      5: ['j', 'k', 'l'], 6: ['m', 'n', 'o'], 8: ['t', 'u', 'v']}
four_letters_dict = {7: ['p', 'q', 'r', 's'], 9: ['w', 'x', 'y', 'z']}


def nums_to_text(num_list):
    result_str = ''
    counter = 1
    list_size = len(num_list)
    if list_size == 1:
        for number in three_letters_dict:
            if num_list[0] == number:
                to_search = three_letters_dict.get(number)
                result_str += to_search[(counter % 3) - 1]
                break
        for number in four_letters_dict:
            if num_list[0] == number:
                to_search = four_letters_dict.get(number)
                result_str += to_search[(counter % 4) - 1]
    for index in range(0, list_size - 1):
        if num_list[index] == num_list[index + 1]:
            counter += 1
        if index == list_size - 2 or not num_list[index] == num_list[index + 1]:
            for number in three_letters_dict:
                if num_list[index] == number:
                    to_search = three_letters_dict.get(number)
                    result_str += to_search[(counter % 3 )- 1]
                    counter = 1
                    break
            for number in four_letters_dict:
                if num_list[index] == number:
                    to_search = four_letters_dict.get(number)
                    result_str += to_search[(counter % 4) - 1]
                    counter = 1
    if num_list[list_size - 1] != num_list[list_size - 2]:
        for number in three_letters_dict:
            if num_list[list_size - 1] == number:
                to_search = three_letters_dict.get(number)
                result_str += to_search[(counter % 3) - 1]
                counter = 1
                break
        for number in four_letters_dict:
            if num_list[list_size - 1] == number:
                to_search = four_letters_dict.get(number)
                result_str += to_search[(counter % 4) - 1]
                counter = 1
    return result_str.upper()


def get_key(s_dict, search):
    key_list = list(s_dict.keys())
    val_list = list(s_dict.values())
    position = val_list.index(search)
    return key_list[position]


def text_to_nums(text_str):
    num_list = []
    text_str = text_str.lower()
    last_char = ''
    for char in text_str:
        if char == ' ':
            num_list.append(0)
        for value_list in three_letters_dict.values():
            for ch in value_list:
                if char == ch:
                    if last_char in value_list:
                        num_list.append(-1)
                    last_char = char
                    for i in range(value_list.index(ch) + 1):
                        num_list.append(get_key(three_letters_dict, value_list))
        for value_list in four_letters_dict.values():
            for ch in value_list:
                if char == ch:
                    if last_char in value_list:
                        num_list.append(-1)
                    last_char = char
                    for i in range(value_list.index(ch) + 1):
                        num_list.append(get_key(four_letters_dict, value_list))
    return num_list


def nums_to_angle(num_list):
    angle_tuple = (300, 30, 60, 90, 120, 150, 180, 210, 240, 270)
    angle_return = 0
    for num in num_list:
        angle_return += angle_tuple[num]
    while angle_return > 360:
        angle_return -= 360
    return angle_return


def angles_to_nums(angle_list):
    angle_tuple = (30, 60, 90, 120, 150, 180, 210, 240, 270, 300)
    return_list = []
    for angle in angle_list:
        if 0 < angle < 15 or 300 < angle < 360:
            continue
        while angle < 0:
            angle += 360
        while angle > 360:
            angle -= 360
        if angle in angle_tuple:
            if angle == angle_tuple[9]:
                return_list.append(0)
            else:
                return_list.append(angle_tuple.index(angle) + 1)
        else:
            if angle < angle_tuple[0]:
                return_list.append(1)
            for index in range(len(angle_tuple) - 1):
                if angle_tuple[index] <= angle <= angle_tuple[index + 1]:
                    dif1 = angle - angle_tuple[index]
                    dif2 = angle_tuple[index + 1] - angle
                    if dif1 < dif2:
                        return_list.append(index)
                    else:
                        return_list.append(index + 1)
    return return_list


def is_phone_tastic(word_str):
    num_list = text_to_nums(word_str)
    angle = nums_to_angle(num_list)
    word_len = len(word_str)
    if angle % word_len == 0:
        return True
    return False
