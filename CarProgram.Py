import CarClass as c


def main():
    my_car = c.Car("Ford", "Mustang", 0)
    SPEEDUP = 5
    SLOWDOWN = -5
    print("Start your engines!")
    print(input("Press ENTER to begin accelerating."))
    for x in range(1, 6):
        increase = my_car.accelerate(SPEEDUP)
        print(
            f"We accelerated by {SPEEDUP} mph.\n\
        The speed is now {my_car.get_speed()}."
        )
    print()
    print(input("Press ENTER to slow down."))
    for x in range(1, 6):
        decrease = my_car.brake(SLOWDOWN)
        print(
            f"We are slowing down by {SLOWDOWN} mph.\n\
        The speed is now {my_car.get_speed()}."
        )


main()
