# all orig from sentdex's youtube tutorials



import matplotlib.pyplot as plt



def double_line_chart():
        
    x = [1,2,3]
    x2 = [1,2,3]
    y = [5,6,7]
    y2 = [10,14,12]

    plt.plot(x,y, label="first")
    plt.plot(x2, y2, label="second")
    plt.xlabel("plot number x")
    plt.ylabel("important var y")

    plt.title("Interesting Graph\ncheese")
    plt.legend()
    plt.show()
    print("DONE")


def bar_chart():
        
    x = [2,4,6,8,10]
    y = [5,6,7,2,5]

    x2 = [1,3,5,9,11]
    y2 = [3,8,5,7,2]

    plt.bar(x,y, label="bars1", color="red")
    plt.bar(x2, y2, label="second")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.title("Interesting Graph\ncheese")
    plt.legend()
    plt.show()
    print("DONE")


def histogram_chart():
    #distrabution
    y = [33,54,24,99,23,54,23,22,40,2,80,23,54,67,85,63,53,7,86,43,52]

    bins = [0,10,20,30,40,50,60,70,80,90,100,110]

    plt.hist(y, bins, histtype="bar", rwidth=0.8, label="this")

    plt.title("Interesting Graph\ncheese")
    plt.legend()
    plt.show()
    print("DONE")


def scatter_chart():
    #distrabution
    y = [33,54,24,99,23,54,23,2]

    x = [1,2,3,4,5,6,7,8]

    plt.scatter(x, y, label="this", color="b", marker="x", s=100)

    plt.title("Interesting Graph\ncheese")
    plt.legend()
    plt.show()
    print("DONE")



def stack_plot():
    import numpy as np
    #distrabution
    days = [1,2,3,4,5]
    
    sleeping = [7,8,6,11,7]
    eating =   [2,3,4,3,2]
    working =  [7,8,7,2,2]
    playing =  [8,5,7,8,13]

    
    labels = ["sleeping ", "eating", "working","playing"]
    fig, ax = plt.subplots()
    ax.stackplot(days, sleeping, eating, working, playing, labels=labels)
    
    plt.title("Interesting Graph\ncheese")
    ax.legend()
    plt.show()

##    y = np.vstack([sleeping, eating, working, playing])
##    fig, ax = plt.subplots()
##    ax.stackplot(days, y)
##    plt.show()
    print("DONE")




def pie_chart():
    import numpy as np
    #distrabution
    days = [1,2,3,4,5]
    
    sleeping = [7,8,6,11,7]
    eating =   [2,3,4,3,2]
    working =  [7,8,7,2,2]
    playing =  [8,5,7,8,13]

    slices = [7,2,2,13]
    labels = ["sleeping ", "eating", "working","playing"]
    
    plt.pie(slices,
            labels=labels,
            startangle=90,
            shadow=True,
            explode=(0, 0.2, 0, 0),
            autopct="%1.1f%%")
    plt.title("Interesting Graph\ncheese")
    plt.show()

    print("DONE")




def load_from_file():

    import csv

    x = []
    y = []
    with open("example.txt", "r") as csvfile:
        plots = csv.reader(csvfile, delimiter=",")
        for row in plots:
            x.append(int(row[0]))
            y.append(int(row[1]))

    plt.plot(x,y, label="loaded from file")
    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Interesting Graph\ncheese")
    plt.legend()
    plt.show()

    print("DONE")



def load_from_file_with_numpy():
    import numpy as np
    import csv

    x, y = np.loadtxt("example.txt", delimiter=",", unpack=True)

    plt.plot(x,y, label="loaded from file")
    
    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Interesting Graph\ncheese")
    plt.legend()
    plt.show()

    print("DONE")




def load_from_internet():
    import numpy as np
    import urllib
    import matplotlib.dates as mdates

    def bytespdate2num(fmt, encoding='utf-8'):
        strconverter = mdates.strpdate2num(fmt)
        def bytesconverter(b):
            s = b.decode(encoding)
            return strconverter(s)
        return bytesconverter

    def graph_data(stock):
        stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
        source_code = urllib.urlopen(stock_price_url).read().decode()
        stock_data = []
        split_source = source_code.split("\n")

        for line in split_source[1:]:
            split_line = line.split(",")
            if len(split_line) == 7:
                if 'values' not in line and "labels" not in line:
                    stock_data.append(line)

        date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                              delimiter=',',
                                                              unpack=True,
                                                              converters={0: bytespdate2num('%Y-%m-%d')})

        plt.plot_date(date,closep, "-", label="price")
        plt.xlabel("date")
        plt.ylabel("price")
        plt.title("Interesting Graph\ncheese")
        plt.legend()
        plt.show()

    graph_data("AAPL")
    print("DONE")






def load_from_internet_cleaned():
    import numpy as np
    import urllib
    import matplotlib.dates as mdates

    def bytespdate2num(fmt, encoding='utf-8'):
        strconverter = mdates.strpdate2num(fmt)
        def bytesconverter(b):
            s = b.decode(encoding)
            return strconverter(s)
        return bytesconverter

        
    def graph_data(stock):

        fig = plt.figure() # implied, but needed if you want to modify
        ax1 = plt.subplot2grid((1,1), (0,0))  #(shape), (row), (col-span), (row-span)

        stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
        source_code = urllib.urlopen(stock_price_url).read().decode()
        stock_data = []
        split_source = source_code.split("\n")

        for line in split_source[1:]:
            split_line = line.split(",")
            if len(split_line) == 7:
                if 'values' not in line and "labels" not in line:
                    stock_data.append(line)

        date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                              delimiter=',',
                                                              unpack=True,
                                                              # %Y = full year. 2015
                                                              # %y = partial year 15
                                                              # 12-06-2014
                                                              # %m-%d-%Y
                                                              converters={0: bytespdate2num('%Y-%m-%d')})

        ax1.plot_date(date,closep, "-", label="price")

        ax1.plot([], [], linewidth=10, label="loss", color="r", alpha=0.5)
        ax1.plot([], [], linewidth=10, label="gain", color="g", alpha=0.5)

        ax1.axhline(closep[0], color="k", linewidth=5)
        
        ax1.fill_between(date, closep, closep[0],where=(closep > closep[0]), facecolor="green", alpha=0.5)
        ax1.fill_between(date, closep, closep[0],where=(closep < closep[0]), facecolor="red", alpha=0.5)

        #ax1.fill_between(date, closep, 0, alpha=0.5)
        
        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)
            label.set_color("purple")

        ax1.grid(True, color="gray")
        ax1.xaxis.label.set_color('blue')
        ax1.yaxis.label.set_color('red')
        ax1.set_yticks([0,105,210,315,420,525,630,735])

        ax1.spines["left"].set_color("c")
        ax1.spines["right"].set_visible(False)
        ax1.spines["top"].set_visible(False)

        ax1.spines["left"].set_linewidth(10)

        ax1.tick_params(axis="y", colors="#2f2f2f")

        
            
        plt.xlabel("date")
        plt.ylabel("price")
        plt.title(stock)
        plt.legend()

        plt.subplots_adjust(left=0.09, bottom=0.18, right=0.94, top=0.95, wspace=0.2, hspace=0.0)
        plt.show()


    graph_data("AAPL")
    print("DONE")





# styles

def load_from_internet_ohlc():
    import matplotlib.pyplot as plt
    import matplotlib.dates as mdates
    import matplotlib.ticker as mticker
    from matplotlib.finance import candlestick_ohlc
    from matplotlib import style
    print(plt.style.available)

    import numpy as np
    import urllib
    import datetime as dt

    #style.use("ggplot")
    style.use("fivethirtyeight")

    def bytespdate2num(fmt, encoding='utf-8'):
        strconverter = mdates.strpdate2num(fmt)
        def bytesconverter(b):
            s = b.decode(encoding)
            return strconverter(s)
        return bytesconverter

        
    def graph_data(stock):

        fig = plt.figure() # implied, but needed if you want to modify
        ax1 = plt.subplot2grid((1,1), (0,0))  #(shape), (row), (col-span), (row-span)

        stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
        source_code = urllib.urlopen(stock_price_url).read().decode()
        stock_data = []
        split_source = source_code.split("\n")

        for line in split_source[1:]:
            split_line = line.split(",")
            if len(split_line) == 7:
                if 'values' not in line and "labels" not in line:
               
                    stock_data.append(line)

        date, closep, highp, lowp, openp, adj_closep, volume = np.loadtxt(stock_data,
                                                              delimiter=',',
                                                              unpack=True,
                                                              converters={0: bytespdate2num('%Y-%m-%d')})


        shorty = date[:50]
        x = 0
        y = len(shorty)
        ohlc = []
        while x < y:
            append_me = date[x], openp[x], highp[x], lowp[x], closep[x], volume[x]
            ohlc.append(append_me)
            x+=1
            
        #candlestick_ohlc(ax1, ohlc, width=0.4, colorup='#77d879', colordown='#db3f3f')
        candlestick_ohlc(ax1, ohlc, width=0.4)

        
        for label in ax1.xaxis.get_ticklabels():
            label.set_rotation(45)

        ax1.xaxis.set_major_formatter(mdates.DateFormatter('%y-%m-%d'))
        ax1.xaxis.set_major_locator(mticker.MaxNLocator(10))
        ax1.grid(True)

        # ANNOTATIONS
        font_dict = {"family":"serif","color":"darkred","size":15}
        ax1.text(date[5], closep[1], "text thing", fontdict=font_dict)

        ax1.annotate('Bad News!',(date[5],highp[5]),
                 xytext=(0.8, 0.9), textcoords='axes fraction',
                 arrowprops = dict(facecolor='grey',color='grey'))

        # SHOW
        plt.xlabel("date")
        plt.ylabel("price")
        plt.title(stock)
        plt.legend()
        plt.subplots_adjust(left=0.09, bottom=0.18, right=0.94, top=0.95, wspace=0.2, hspace=0.0)
        plt.show()


    graph_data("AAPL")
    print("DONE")



load_from_internet_ohlc()




def load_live_data():
    
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    from matplotlib import style

    style.use('fivethirtyeight')

    fig = plt.figure()
    ax1 = fig.add_subplot(1,1,1)

    def animate(i):
        graph_data = open("example.txt","r").read()
        lines = graph_data.split("\n")
        xs = []
        ys = []
        for line in lines:
            if len(line) > 1:
                x, y = line.split(",")
                xs.append(x)
                ys.append(y)

        ax1.clear()
        ax1.plot(xs, ys)

    ani = animation.FuncAnimation(fig, animate, interval=1000)

    plt.show()       













