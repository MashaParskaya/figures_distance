class Dot():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def mass_center(dots):
    x_sum = 0
    y_sum = 0
    for i in range(len(dots)):
        x_sum += dots[i].x
        y_sum += dots[i].y
    return (Dot(x_sum / len(dots), y_sum / len(dots)))


def dist(dot1, dot2):
    return ((dot1.x - dot2.x) ** 2 + (dot1.y - dot2.y) ** 2) ** (1/2)


def not_line(dots):
    lines = []
    for i in range(len(dots) - 1):
        lines.append([dots[i].x - dots[i+1].x, dots[i].y - dots[i+1].y])
    cnt = 0
    for i in range(len(lines) - 1):
        if (lines[i][0] * lines[i+1][1] != lines[i+1][0] * lines[i][1]):
            cnt += 1
    return (cnt == len(lines) - 1)


def find_min_dist(unused, total, fig1=list(), fig2=list()):
    if (len(fig1) + len(fig2) == total):
        if (not_line(fig1) and not_line(fig2)):
            return dist(mass_center(fig1), mass_center(fig2)), fig1, fig2
        else:
            return -1, [], []
    else:
        minleft = -1
        leftfig1 = []
        leftfig2 = []
        minright = -1
        rightfig1 = []
        rightfig2 = []
        if (len(fig1) != total - 3):
            minleft, leftfig1, leftfig2 = find_min_dist(unused[1:], total,
                                                        fig1 + [unused[0]],
                                                        fig2)
        if (len(fig2) != total - 3):
            minright, rightfig1, rightfig2 = find_min_dist(unused[1:], total,
                                                           fig1,
                                                           fig2 + [unused[0]])
        if (minleft < minright and minleft != -1) or minright == -1:
            return minleft, leftfig1, leftfig2
        else:
            return minright, rightfig1, rightfig2
