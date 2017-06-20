def print_windchill(windchill, t, v):
    print("{0:8} {1:12} {2:15.5}".format(v, t, windchill))

def compute_windchill():
    t = -20
    v = 0
    while t < 60 and v < 50:
        windchill = 35.74 + (0.6215 * t) - (35.75 * (v ** 0.16)) + (0.4275 * t) * (v ** 0.16)
        t = t + 10
        v = v + 5
        print_windchill(windchill, t, v)

def intro():
    print("This program computes wind chill indexes")
    print("{0:6} {1:6} {2:6}".format("Wind (mph)", "Temperature (F)", "Windchill"))

def main():
    intro()
    compute_windchill()

main()