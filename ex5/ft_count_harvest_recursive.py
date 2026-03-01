def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))
    def recursive_count_harvest(d):
        if d == 0:
            return
        recursive_count_harvest(d - 1)
        print(f"Day {d}")
    recursive_count_harvest(days)
    print("Harvest time!")
