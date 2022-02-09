import InsectClass as i


def main():
    new_insect = i.Insect(2, 4)
    new_insect.length_of_flight()
    miles = str(new_insect.get_lenflight())
    print("This insect can fly for " + miles + " miles.")


main()
