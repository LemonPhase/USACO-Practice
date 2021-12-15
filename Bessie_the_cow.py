import os
dir_path = os.path.dirname(os.path.realpath(__file__))
os.chdir(dir_path)

coord = []

f = open("Bessie_input.txt", 'r')
lst = f.read().splitlines()
f.close()

b1_x1, b1_y1, b1_x2, b1_y2 = int(lst[0].split()[0]), int(
    lst[0].split()[1]), int(lst[0].split()[2]), int(lst[0].split()[3])

b2_x1, b2_y1, b2_x2, b2_y2 = int(lst[1].split()[0]), int(
    lst[2].split()[1]), int(lst[1].split()[2]), int(lst[1].split()[3])

t_x1, t_y1, t_x2, t_y2 = int(lst[2].split()[0]), int(
    lst[2].split()[1]), int(lst[2].split()[2]), int(lst[2].split()[3])

if b1_x1 <= t_x1 <= b1_x2:
    # A part of truck in board 1
    if b1_y1 <= t_y1 <= b1_y2:
        a_1 = (b1_x2 - b1_x1) * (b1_y2 - b1_y2) - \
            (b1_x2 - t_x1) * (b1_y2 - t_y1)
    # A point of truck
    else:
        pass
