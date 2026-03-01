def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def recursive_print_day(d):
        if d == 0:
            return
        recursive_print_day(d - 1)
        print(f"Day {d}")

    recursive_print_day(days)
    print("Harvest time!")
