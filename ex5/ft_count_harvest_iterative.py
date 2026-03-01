#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/01 17:26:52 by trakotos            #+#    #+#            #
#   Updated: 2026/03/01 17:26:54 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for i in range(days):
        print(f"Day {i + 1}")
    print("Harvest time!")
