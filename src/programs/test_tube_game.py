class TestTubeGame:
    test_tube_count = 0
    test_tube_coordinates = []
    test_tube_colors = []
    max_test_tube_colors = 0
    soln_moves = []
    meta_data = {}
    game_state = {}
    colors_mapping = {}
    color_hash = {}

    def play(self):
        # self.get_number_of_testtubes()
        # self.display_test_tube_count()
        self.get_colors_in_testtubes()
        self.display_test_tube_colors()
        self.solve()
        # self.display_soln_moves()

    def display_test_tube_colors(self):
        if 'test_tube' in self.meta_data:
            rows = len(self.meta_data['test_tube'])
            for row in range(rows):
                print(f'test tube colors in row {row+1} is: {self.meta_data["test_tube"][row]}')

    def display_test_tube_count(self):
        print(f'total number of testubes {self.test_tube_count}')

    def get_number_of_testtubes(self):
        self.test_tube_count = int(input('enter number of testubes: '))

    def get_colors_in_testtubes(self):
        # take colors row wise
        self.test_tube_count = 0
        no_of_rows = int(input('enter number of rows: '))
        self.max_test_tube_colors = int(input('enter maximum number of color a test tube can have: '))
        self.meta_data['test_tube'] = [[]*no_of_rows]
        color_count = 0
        for row in range(no_of_rows):
            no_of_testtube_in_row = int(input(f'enter no of testubes in row no {row+1}: '))
            for col in range(no_of_testtube_in_row):
                colors_in_test_tube = input(f'enter colors from top to bottom seperated with comma for test tube in row {row+1} and {col+1}: ').split(',')
                color_mapping = []
                for color in colors_in_test_tube:
                    if color not in self.color_hash:
                        self.color_hash[color] = color_count
                        color_mapping.append(color_count)
                        color_count += 1
                    else:
                        color_mapping.append(self.color_hash[color])
                self.test_tube_colors.append(color_mapping[::-1])
                self.meta_data['test_tube'][row].append(colors_in_test_tube[::-1])
                self.test_tube_coordinates.append([row, col])
                self.update_colors_mapping(self.test_tube_count, color_mapping)
                self.test_tube_count += 1
        # for test_tube_no in range(self.test_tube_count:
        #     for tt in range(test_tube_no)

    def update_colors_mapping(self, test_tube_no, colors_in_test_tube):
        if len(colors_in_test_tube):
            self.colors_mapping[colors_in_test_tube[0]] = [[test_tube_no, len(colors_in_test_tube)]]
        else:
            self.colors_mapping['empty'] = [[test_tube_no, 0]]

    def get_state_string(self):
        color_mapping = {}
        test_tube_count = 0
        is_game_solved = True
        color_hash = ""
        for test_tube in self.test_tube_colors:
            for color in test_tube:
                if color in color_mapping:
                    color_mapping[color].append(test_tube_count)
                    if len(color_mapping[color]) > 1:
                        is_game_solved = False
                else:
                    color_mapping[color] = [test_tube_count]
                color_hash += f':{color}'
                test_tube_count += 1
        return color_hash, is_game_solved

    def solve(self):
        state_hash, is_game_solved = self.get_state_string()
        if state_hash in self.game_state and self.game_state[state_hash]:
            return
        if is_game_solved:
            self.update_ans()
            return



    def display_soln_moves(self):
        pass


TestTubeGame().play()