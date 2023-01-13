#! /usr/bin/bash
ech "Enter Your Directory:"
read target
cd $target
#file with "a" character in their names
aName=$(find . -type f -name "*a*")

for f in $aName
do
    if [[ $(file -b $f)=="ASCII text" ]];then
        #this has a probleam that cant cp that file in the new Directory
        cp "$f" "$target/result/$f"
    fi
done
