

def parse_input(filepath):
    game_sets = []
    file = open(filepath, 'r')
    while True:
        line = file.readline()
        if not line:
            # print(i)
            return game_sets
        game_sets.append(line.strip().split(": ")[1].split("; "))


def check_game_powers(game):
    minimum_set = {"red": 0,
                   "green": 0,
                   "blue": 0}
    for current_set in game:
        for one_color_cube_number in current_set.split(','):
            current_cube_color = one_color_cube_number.strip().split(' ')[1]
            current_cube_num = int(one_color_cube_number.strip().split(' ')[0])

            if minimum_set[current_cube_color] < current_cube_num:
                minimum_set[current_cube_color] = current_cube_num

    return minimum_set['red']*minimum_set['green']*minimum_set['blue']


result_id_powers_sum = 0
# game_sets = parse_input('test-input.txt')
game_sets = parse_input('input.txt')

for current_game in game_sets:
    result_id_powers_sum += check_game_powers(current_game)

print(result_id_powers_sum)
