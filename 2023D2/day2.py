target_set = {"red": 12,
              "green": 13,
              "blue": 14}


def parse_input(filepath):
    game_sets = []
    file = open(filepath, 'r')
    while True:
        line = file.readline()
        if not line:
            # print(i)
            return game_sets
        game_sets.append(line.strip().split(": ")[1].split("; "))


def check_set_possible(game_set, target_set):
    for one_color_cube_number in game_set.split(','):

        if target_set[one_color_cube_number.strip().split(' ')[1]] < int(one_color_cube_number.strip().split(' ')[0]):
            return False
    return True


def check_game_possible(game, target_set):
    for current_set in game:
        if not check_set_possible(current_set, target_set):
            return False
    return True


result_id_sum = 0
# game_sets = parse_input('test-input.txt')
game_sets = parse_input('input.txt')
current_game_id = 0

for current_game in game_sets:
    current_game_id += 1
    if check_game_possible(current_game, target_set):
        result_id_sum += current_game_id

print(result_id_sum)
