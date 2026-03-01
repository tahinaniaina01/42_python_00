#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_recursive.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/01 17:26:55 by trakotos            #+#    #+#            #
#   Updated: 2026/03/01 17:26:57 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_count_harvest_recursive():
    days = int(input("Days until harvest: "))

    def recursive_print_day(d):
        if d == 0:
            return
        recursive_print_day(d - 1)
        print(f"Day {d}")

    recursive_print_day(days)
    print("Harvest time!")
