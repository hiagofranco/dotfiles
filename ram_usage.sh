#!/bin/bash

main () {
	RATE=5 # seconds
	ram_label="RAM"

	while true; do
		usage="$(free -h | awk 'NR==2 {print $3}')"
		total="$(free -h | awk 'NR==2 {print $2}')"
		formated="${usage}/${total}"
		echo $ram_label $formated
		sleep $RATE
	done
}

main
