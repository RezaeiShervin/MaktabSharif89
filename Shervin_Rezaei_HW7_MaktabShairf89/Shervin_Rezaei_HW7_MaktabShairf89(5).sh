#! /usr/bin/bash
read -p "Enter directorry name:" newDir
[ -d "$newDir" ] && echo "This Folder Existed" || mkdir $newDir && echo "This Folder Created"
