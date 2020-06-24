#!/bin/bash

# usage:python3 pcfg_guesser.py -r {rule} | ./judge.sh -i {testing data path} -o {output path}

#testing_file=$1
#output_file=$2
silence=0
start_time=`date +"%F %T"`
found=0
guess=0

function help_me()
{
	echo "Usage:"
	echo "    judge.sh [-i testing file] [-o output file] [-s]"
	echo "Description:"
	echo "    -s silence"
}
function echo_outp()
{
	if [[ ${silence} -eq $zero  ]]
	then
       		echo "$@" | tee -a ${output_file} 
	else
		echo "$@" >> ${output_file}
	fi
}
function echo_record()
{
	if [[ ${silence} -eq $zero  ]]
	then
		echo "$@" | tee -a "${output_file}-record"
	else
		echo "$@" >> "${output_file}-record"
	fi
}

function user_interrupt()
{
	end_time=`date +"%F %T"`
	echo_outp "---Stop: ${end_time} Found: ${found} Guess: ${guess}---"
	crontab -r
	exit
}

function add_crontab()
{
	current=`pwd`
	crontab -l > mycron
	echo "*/10 * * * * echo \`cat ${current}/${output_file} | wc -l\` >> "${current}/${output_file}-count"" >> mycron
	cat mycron
	crontab mycron
	rm mycron
}

while getopts "i:o:sh" opt
do
	case "$opt" in
		i) testing_file=${OPTARG};;
		o) output_file=${OPTARG};;
		s) silence=1;;
		h) help_me;exit;;
		*) help_me;exit;;
	esac
done
echo "$testing_file $output_file $silence"
trap user_interrupt SIGINT
#add_crontab
cat /dev/null > ${output_file}
echo_outp "---Start: ${start_time}---"
#watch --interval=10 echo "$guess"
while IFS='$\n' read -r line;
do
	ret=`grep -Fx -e "${line}" ${testing_file} | head -1`
	if [ ! -z "${ret}" ]
	then
		if [ $[${guess} % 10000] -eq 0  ]
		then
			now=`date +"%F %T"`
			echo_record "guess: ${guess} found: ${found} time: ${now} "
		fi
		((found++))
		echo_outp "Found ${ret}"
	fi
	((guess++))
done


