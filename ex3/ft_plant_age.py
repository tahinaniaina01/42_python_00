#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_plant_age.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/01 17:26:44 by trakotos            #+#    #+#            #
#   Updated: 2026/03/01 17:26:46 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_plant_age():
    plant_age = int(input("Enter plant age in days: "))
    if plant_age > 60:
        print("Plant is ready to harvest!")
    else:
        print("Plant needs more time to grow.")
