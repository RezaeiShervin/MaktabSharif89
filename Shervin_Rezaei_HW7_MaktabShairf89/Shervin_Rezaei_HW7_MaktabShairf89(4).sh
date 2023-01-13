#!/bin/bash

echo "Enter your Directory:"
read target
cd "$target"

for f in $1/*
do
	cat * | sed '/^$/d;s/[[:blank:]]//g' | sort > textfile.txt
done
sed -n '5,10p' textfile.txt
