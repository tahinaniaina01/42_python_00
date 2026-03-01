#!/usr/bin/env python3
# ########################################################################### #
#                                                                             #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: trakotos <trakotos@student.42antananarivo.   +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: 2026/03/01 17:26:48 by trakotos            #+#    #+#            #
#   Updated: 2026/03/01 17:26:50 by trakotos           ###   ########.fr      #
#                                                                             #
# ########################################################################### #


def ft_water_reminder():
    days = int(input("Days since last watering: "))
    if days > 2:
        print("Water the plants!")
    else:
        print("Plants are fine")
