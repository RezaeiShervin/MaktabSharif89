#! /usr/bin/bash

echo "Enter a directory address:"
read address

file_counter=ls -A $address | grep ^- / | wc -l
folder_Counter=ls -A -l $address | grep ^d | wc -l
echo ${file_counter}
echo ${folder_Counter}
