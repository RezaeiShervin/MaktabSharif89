#! /usr/bin/bash

echo "Enetr Your Url:"
read url    #http://dl.sarimusic.net/1395/10/11/Old/Shadmehr%20Aghili%20-%20Taghdir/Shadmehr%20Aghili%20-%20Taghdir/01.%20Shadmehr%20Aghili%20-%20Taghdir.mp3

wget "$url" > Music
echo $url > log.txt
