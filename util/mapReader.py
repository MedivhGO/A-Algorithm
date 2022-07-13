import re
import os


class MapReader(object):
    def __init__(self):
        self.start_x = 0
        self.start_z = 0
        self.height = 0
        self.wide = 0
        dir_path = os.path.dirname(__file__)
        dir_path = os.path.dirname(dir_path)
        self.file_path = os.path.join(dir_path, 'resource\\navmesh_matrix.txt')
        self.map_file = open(self.file_path, 'r')
        self.astar_map = []
        self.game_map = []
        self.MAX_LENGTH = 100

        self.init_map()
        self.read_map()

    def init_map(self):
        self.astar_map = []
        for i in range(self.MAX_LENGTH):
            self.astar_map.append([])
            self.game_map.append(100 * [0])

    def read_map(self):
        line_num = 0
        for map_line in self.map_file.readlines():
            if map_line.startswith('startpos'):
                begin = map_line.find('(')
                end = map_line.find(')')
                map_line = map_line[begin + 1:end]
                words = [x for x in re.split(r'[ ,]', map_line) if x != '']
                self.start_x = int(float(words[0]))
                self.start_z = int(float(words[2]))
            elif map_line.startswith('height'):
                begin = map_line.find('=')
                end = map_line.find('\n')
                map_line = map_line[begin + 1: end]
                self.height = int(map_line)
            elif map_line.startswith('wide'):
                begin = map_line.find('=')
                end = map_line.find('\n')
                map_line = map_line[begin + 1: end]
                self.wide = int(map_line)
            elif map_line.startswith('{'):
                words = [x for x in re.split(r'[ ,{}]', map_line) if x != '']
                self.astar_map[self.height - line_num - 1] = words
                line_num += 1

        self.map_file.close()
        self.start_z -= self.height - 1

        self.set_game_map()

    def set_game_map(self):
        for i in range(self.wide):
            for j in range(self.height):
                self.game_map[i][j] = int(self.astar_map[j][i])


if __name__ == '__main__':
    map_reader = MapReader()
    for line in map_reader.game_map:
        print(line)
