process= $(xprop -id $(xdotool getactivewindow) | grep WM_CLASS | awk '{print $3}'| sed 's/"//g' | sed 's/,//g')

eval $process

