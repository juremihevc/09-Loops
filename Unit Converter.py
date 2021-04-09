print("UNIT CONVERTER")

while True:
    km = input("Please eneter distance in km: ")

    km = float(km.replace("," , "."))

    miles = km * 0.621371192

    print(f"{km} km is {miles} miles")

    quest = input("Do you want to do another conversion? (type y or n): ")

    if quest.lower() != "y" and quest.lower() != "yes":
        break

print("Goodbye!")