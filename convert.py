# convert.py
#
# User inputs speed in mph
# Program outputs speed in kph, ft/s, m/s depending on user choice.
#
# Three functions are defined, each with 1 parameter and returning a value:
#   mph -> kph
#   mph -> ft/s
#   mph -> m/s

# Defining the conversion funcations for the rates
def mph_to_kph(mph):
    return 1.609*mph
def mph_to_ms(mph):
    return mph_to_kph(mph)*1000/3600
def mph_to_fts(mph):
    return mph*5280/3600

# Gettingput from the user
mph = input("Input speed in mph: ")

# Changing input to float
mph = float(mph)

# Shows the user their different options for converting
print("These are your options: (1) Convert and output to kph. (2) Convert and output to m/s. (3) Convert and output to ft/s.")

# The user selects their option
value = int(input("What is your option?   "))

# Conditional based on the user input and outputs the conversion
if value == 1:
    print("Speed in kph is", mph_to_kph(mph))
elif value == 2:
    print("Speed in m/s is", mph_to_ms(mph))
elif value == 3:
    print("Speed in ft/s is", mph_to_fts(mph))
else:
    print("Not an option :/")