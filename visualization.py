#Code written by Shimon Johnson

import matplotlib.pyplot as plt


def make_pie(chartData):
    labels = 'Detected', 'Detected_Uncommon', 'Absent/Undetected'
    sizes = [chartData["Detected_count"], chartData["Detected_Uncommon"], chartData["Absent/Undetected"]]
    explode = (0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')

    fig1, ax1 = plt.subplots()
    ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
            shadow=True, startangle=90)
    ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.

    plt.show()
