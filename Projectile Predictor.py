import numpy as np
import matplotlib.pyplot as plt

angle = [-40, -20, 0, 20, 40, 60, 80]
distance = [61, 177.33, 296.33, 680.33, 651, 534.67, 24.67]

eq = np.polyfit(angle, distance, 4)
readable_eq = np.poly1d(eq)

print readable_eq

ran = np.arange(-40, 90)
y = np.polyval(eq, ran)

plt.plot(angle, distance, label="Data")
plt.plot(ran, y, label="Equation")
plt.legend(loc = 'upper right')
plt.xlabel("Angle of the shot")
plt.ylabel("Distance of the dart")
plt.title("Nerf dart distances at a given angle")
plt.savefig('graph.png')


run = True
while run == True:
    input = raw_input("Enter an angle (q to exit):")
    if input == 'q':
        run = False
    else:
        try:
            input = int(input)
            ans = int(np.polyval(eq, input))
            #ft = ans/12
            #print str(int(ft)) + ' ft. and ' + str(ans % 12) + " ins."
            print ans
        except:
            print "Invalid angle"
