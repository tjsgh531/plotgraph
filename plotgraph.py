from matplotlib import pyplot as plt
def plot_graph(xValue, yValue,xLabel = '',yLabel = '',titleLabel = '', xMin = 0, xMax = 100, yMin = 0, yMax = 100):    
    plt.plot(xValue,yValue, color='red', marker = 'o')

    plt.axis([xMin,xMax,yMin,yMax])

    plt.xlabel(xLabel)
    plt.ylabel(yLabel)
    plt.title(titleLabel)

    plt.show()
    return 0

x_values = []
while True:
    x_value = input('x값을 입력하세요 : ')
    if x_value == 'N':
        break
    x_values.append(float(x_value))

y_values = []
while True:
    y_value = input('y값을 입력하세요 : ')
    if y_value == 'N' :
        break
    y_values.append(float(y_value))

x_label = input('x_label이름을 입력하세요 :')
y_label = input('y_label이름을 입력하세요 :')
title_label = input('title_label이름을 입력하세요 :')

x_min = float(input("x_min을 입력하세요 :"))
x_max = float(input("x_max을 입력하세요 :"))
y_min = float(input("y_min을 입력하세요 :"))
y_max = float(input("y_max을 입력하세요 :"))

plot_graph(x_values, y_values, x_label, y_label, title_label, x_min, x_max, y_min, y_max)