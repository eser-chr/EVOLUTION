#!/bin/bash

print_help(){

	echo "Pass arguments STEPS and BLOCK size"
}


while getopts h OPTION; do
	case $OPTION in
		h) print_help; exit 0 ;;
	esac

done

shift $((OPTIND -1))
if [[$# -gt 0]]; then
	echo "Additional arguments $@"
fi	

rm *.csv

steps=$1
steps=${steps:-100}
blocks=$2
blocks=${blocks:-10}
python main.py ${steps} ${blocks}
python plotter.py
