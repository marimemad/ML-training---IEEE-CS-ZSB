import csv
import matplotlib.pyplot as plt

def hypothesis(x,y,theta0,theta1):
    h=[]
    for i in range(len(x)):
        h.append((theta0+theta1*x[i])-y[i])
    return(h)


def gradient_descent(x,y,theta0,theta1):
    m=len(x)
    alpha=0.0002
    repeat=20
    for i in range(repeat):
        h=hypothesis(x,y,theta0,theta1)
        hx=sum([h[i]*x[i] for i in range(len(h))])

        temp=theta0-(alpha/m)*sum(h)
        theta1=theta1-(alpha/m)*hx

        theta0=temp

    return(theta0,theta1)


def main():
    x_axis = []
    y_axis = []
    with open('dataset.csv') as dataset:
        reader = csv.reader(dataset, delimiter=',')
        line_count = 0
        for row in reader:
            if (line_count == 0):
                line_count+=1
            else:
                line_count+=1
                x_axis.append(float(row[0]))
                y_axis.append(float(row[1]))

    plt.plot(x_axis, y_axis, 'bo')
    theta0,theta1=gradient_descent(x_axis, y_axis,0,0)
    print(theta0,theta1)
    y=[theta0+theta1*x for x in x_axis]
    plt.plot(x_axis,y)
    plt.show()

if __name__ == '__main__':
    main()
