
color_names = {"AliceBlue": "#f0f8ff", "AntiqueWhite": "#faebd7", "AntiqueWhite1": "#ffefdb",
               "AntiqueWhite2": "#eedfcc", "AntiqueWhite3":	"#cdc0b0", "AntiqueWhite4": "#8b8378",
               "aquamarine1": "#7fffd4", "aquamarine2": "#76eec6", "aquamarine4"	: "#458b74", "azure1": "#f0ffff"}

for i in color_names:
    print("{:13} is {}".format(i, color_names[i]))

color = input("Please enter a color name as shown")

while color != "":
    if color in color_names:
        print("{:13} is {}".format(color, color_names[color]))
    else:
        print("Invalid input ")
    color = input("Please enter a color name as shown")