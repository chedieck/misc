#!/bin/bash
# Fixes my remote keyboard after reconnecting it.
setxkbmap -layout br
xmodmap ~/.Xmodmap
sh -c "xset r rate 300 40"


