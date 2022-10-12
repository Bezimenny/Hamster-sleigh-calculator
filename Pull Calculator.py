
object = input("Object: ")
oweight = input(object + "'s weight in kg: ")
animal = input("Animal: ")
aweight = input(animal + "'s weight in kg: ")
street = input("Length of motion in meters: ")
time = input("Time of motion in seconds: ")

htime = float(time) / 60
oweight = float(oweight) * 9.8
aweight = float(aweight) * 9.8
lstreet = float(street) / 1000

opower = float(oweight) * float(street) / float(time)
anumber = float(opower) * float(time) / float(aweight)

print("Number of " + str(animal) + "s necessary to pull the " + str(object) + " for " + str(float(lstreet)) + "km in " +
      str(round(htime)) + "min is " + str(round(anumber)))
