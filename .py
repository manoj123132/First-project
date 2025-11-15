# Basic if / elif / else example for weather conditions
rain = True
sunshine = False

if rain and not sunshine:
    print("It's a rainy day, but we can still enjoy the pool!")
elif sunshine and not rain:
    print("The weather is perfect for a swim in the pool!")
elif rain and sunshine:
    print("We have both rain and sunshine — look for a rainbow!")
else:
    print("No rain and no sunshine — weather is neutral for outdoor activities.")
