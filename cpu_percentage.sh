#!/bin/bash

main () {
	RATE=5 # seconds
	cpu_label="CPU"

	while true; do
		cpu_load=$(LC_NUMERIC=en_US.UTF-8 top -bn2 -d 0.01 | grep "Cpu(s)" | tail -1 | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1"%"}')
		echo $cpu_label $cpu_load
		sleep $RATE
	done
}

main
