def sum_of_diagonals(num):
    last_number = num * num
    odd_numbers = range(1,last_number+1,2)

    i = 0
    gap = 1
    solution = 1

    while odd_numbers[i] != last_number:
        for j in range(4):
            i+= gap
            solution += odd_numbers[i]
        gap += 1
    return solution

print('answer = {}'.format(sum_of_diagonals(1001)), '\n')


# It was not necessary, but I wanted to write a class that draws the spirals shown in the task. 
# You can change a number at the bottom (number % 2 != 0)

class Spiral:
    def __init__(self, num):
        self.num = num
        self.matrix = self.fill_spiral()
        self.show_spiral()

    def fill_axis_x(self, matrix, last_row = 0):
        for i in range(self.dif - last_row):
            self.x += self.direction
            matrix[self.y][self.x] = self.count
            self.count += 1

    def fill_axis_y(self, matrix):
        for i in range(self.dif):
            self.y += self.direction
            matrix[self.y][self.x] = self.count
            self.count += 1
        self.direction *= -1


    def fill_spiral(self):
        matrix = [[0 for x in range(self.num)] for y in range(self.num)]

        self.y = self.x = round((self.num-1) / 2)
        matrix[self.y][self.x] = 1

        self.dif = 1; self.count = 2
        self.direction = 1
        
        while self.dif < self.num:
            self.fill_axis_x(matrix)
            self.fill_axis_y(matrix)
            self.dif += 1

        self.fill_axis_x(matrix, 1)
        return matrix

    def show_spiral(self):
        for y in range(len(self.matrix)):
            for x in range(len(self.matrix[0])):
                print('%3d' % self.matrix[y][x], end = ' ')
            print()

test1 = Spiral(5)


