#!/usr/bin/env bash

set -m

for i in `seq 2`; do
	sleep 3 &
	echo ""
done

while [1]; do fg 2> /dev/null; [ &? == 1 ] && break; done

