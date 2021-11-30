import geometry
import autotest


def get_data(filename):
    error = 0
    try:
        fin = open(filename, "r")
        line_cnt = 0
        data = []
        for line in fin.readlines():
            line_cnt += 1
            try:
                x, y = map(float, line.split())
                data.append(geometry.Dot(x, y))
            except ValueError:
                fin.close()
                error += 10
            if error:
                raise Exception("Sorry. Wrong format of input data. Each line must contain two float values.")
        fin.close()
    except FileNotFoundError:
        error += 1
    if error:
        raise FileNotFoundError("Sorry. No such file, please try again.")
    if line_cnt < 6:
        raise Exception("Sorry. Wrong format of input data. Total amount of lines must be 6 or more.")
    return data


autotest.Autotest()
filename = input("filename: ")
dots = get_data(filename)
ans, fig1, fig2 = geometry.find_min_dist(dots, len(dots))
print("The answer is:", ans)
print("Figure 1:")
for i in range(len(fig1)):
    print(fig1[i].x, fig1[i].y)
print("Figure 2:")
for i in range(len(fig2)):
    print(fig2[i].x, fig2[i].y)
