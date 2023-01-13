#! /usr/bin/bash
while true;
do
    echo "Enter number: "
    read number
    if [[ "$number" == 'exit' ]]
    then
        break
    else
        x=$(($number**2))
        echo $x
    fi

done

#     elif [["$number"=='^[0-9]+$']]
#     then
