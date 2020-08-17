# reads a specific CSV file, reads input and checks a dictionary if it is a country. Spits out the capital if so.


def read_countries(file_name):
    result = dict()     # creates dictionary

    first_line = True  # sets up way to skip first line.
    for line in open(file_name):
        if first_line:
            first_line = False

        split_line = line.split(",")  # splits the line by the commas,
        country_name = split_line[0].strip('"')  # gets a value called country_name
        capital_name = split_line[1].strip('"')  # gets a value called capital_name

        result[country_name] = capital_name    # fully creates our dictionary by adding values to our keys

    return result  # returns the dictionary


def main():
    country = read_countries("country-capitals.csv")  # does the read_countries function value on the file name in green

    running = True  # bepis is our looping condition
    while running:

        name = input("Give me a country :)\nIf you want to quit at any time, type quit\n")
        if name == "quit":  # if our name is equal to quit, it breaks.
            print("bye have beautiful time!")
            break
        for xd in country:  # goes through all of our keys

            if xd == name:  # since xd is our keys and the one they type is equal to it, its in there and has a capital
                print("\n%s's capital is %s.\n" % (name, country[name]))
                break
        else:   # if it fully goes through the for, and it doesn't break, the thing they typed isn't in here.
            print("\n%s does not exist.\n" % name)


main()
