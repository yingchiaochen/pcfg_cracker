#!/bin/bash

testing_file=$1
output_file=$2
start_time=`date +"%F %T"`
echo "---Start: ${start_time}---"

function user_interrupt()
{
	end_time=`date +"%F %T"`
	echo "---Stop: ${end_time}---"
}

trap user_interrupt SIGINT

echo "---${start_time}---"
while IFS='$\n' read -r line;
do
	ret=`grep "^${line}$" ${testing_file}` 
	if [ -z "${line}" ]
	then
		echo "NULL"
	else
		echo "Found ${line}"
	fi
done


