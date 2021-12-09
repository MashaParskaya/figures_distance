accuracy = 1e-3


class Dot():
    def __init__(self, x, y):
        self.x = x
        self.y = y


def det(a, b, c, d):
    return a * d - b * c


def distance_between_dots(d1, d2):
    return ((d1.x - d2.x) ** 2 + (d1.y - d2.y) ** 2) ** (1/2)


def between(a, b, mid):
    global accuracy

    if ((min(a.x, b.x) <= mid.x + accuracy and max(a.x, b.x) + accuracy >= mid.x)
       and (min(a.y, b.y) <= mid.y + accuracy and max(a.y, b.y) + accuracy >= mid.y)):
        return True


def distance_between_dot_and_line_segment(d, end1, end2):
    global accuracy

    A = end1.y - end2.y
    B = end2.x - end1.x
    C = -A*end1.x - B*end1.y

    A_orth = B
    B_orth = -A
    C_orth = -A_orth * d.x - B_orth * d.y

    zn = det(A, B, A_orth, B_orth)

    x_pr = -det(C, B, C_orth, B_orth) / zn
    y_pr = -det(A, C, A_orth, C_orth) / zn
    proection = Dot(x_pr, y_pr)
    if between(end1, end2, proection):
        return distance_between_dots(d, proection)
    else:
        return min(distance_between_dots(d, end1), distance_between_dots(d, end2))


def distance_between_line_segments(fig1dot1, fig1dot2, fig2dot1, fig2dot2):
    global accuracy

    A1 = fig1dot1.y - fig1dot2.y
    B1 = fig1dot2.x - fig1dot1.x
    C1 = -A1*fig1dot1.x - B1*fig1dot1.y

    A2 = fig2dot1.y - fig2dot2.y
    B2 = fig2dot2.x - fig2dot1.x
    C2 = -A1*fig2dot1.x - B1*fig2dot1.y

    zn = det(A1, B1, A2, B2)

    if abs(zn) > accuracy:
        x_int = -det(C1, B1, C2, B2) / zn
        y_int = -det(A1, C1, A2, C2) / zn
        intersection = Dot(x_int, y_int)

        if (between(fig1dot1, fig1dot2, intersection) and between(fig2dot1, fig2dot2, intersection)):
            return 0
        else:
            dist1 = distance_between_dot_and_line_segment(fig1dot1, fig2dot1, fig2dot2)
            dist2 = distance_between_dot_and_line_segment(fig1dot2, fig2dot1, fig2dot2)
            dist3 = distance_between_dot_and_line_segment(fig2dot1, fig1dot1, fig1dot2)
            dist4 = distance_between_dot_and_line_segment(fig2dot2, fig1dot1, fig1dot2)
            return min(dist1, dist2, dist3, dist4)
    else:
        if abs(det(A1, C1, A2, C2)) < accuracy and abs(det(B1, C1, B2, C2)) < accuracy:
            if (between(fig2dot1, fig2dot2, fig1dot1)
               or between(fig2dot1, fig2dot2, fig1dot1)):
                return 0
            else:
                dist1 = distance_between_dots(fig1dot1, fig2dot1)
                dist2 = distance_between_dots(fig1dot1, fig2dot2)
                dist3 = distance_between_dots(fig1dot2, fig2dot1)
                dist4 = distance_between_dots(fig1dot2, fig2dot2)
                return min(dist1, dist2, dist3, dist4)
        else:
            dist1 = distance_between_dot_and_line_segment(fig1dot1, fig2dot1, fig2dot2)
            dist2 = distance_between_dot_and_line_segment(fig1dot2, fig2dot1, fig2dot2)
            dist3 = distance_between_dot_and_line_segment(fig2dot1, fig1dot1, fig1dot2)
            dist4 = distance_between_dot_and_line_segment(fig2dot2, fig1dot1, fig1dot2)
            return min(dist1, dist2, dist3, dist4)


def min_distance_between_figures(dots1, dots2):
    min_dist = -1
    for i in range(-1, len(dots1)-1):
        for j in range(-1, len(dots2)-1):
            tmp = distance_between_line_segments(dots1[i], dots1[i+1], dots2[j], dots2[j+1])
            if min_dist == -1 or tmp < min_dist:
                min_dist = tmp
    return min_dist
