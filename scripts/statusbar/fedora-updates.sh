#! /bin/bash

dnfupdates=$(dnf check-update| grep -Ec ' updates$')

# TODO:
# flatpakupdates=$()
