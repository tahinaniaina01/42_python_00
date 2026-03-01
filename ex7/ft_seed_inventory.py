#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_seed_inventory.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/01 17:27:05 by trakotos            #+#    #+#            #
#   Updated: 2026/03/01 17:27:09 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if unit == "packets":
        print(f"{seed_type} seeds: {quantity} packets available")
    elif unit == "grams":
        print(f"{seed_type} seeds: {quantity} grams total")
    elif unit == "area":
        print(f"{seed_type} seeds:  covers {quantity} square meters")
    else:
        print("Unknown unit type")
