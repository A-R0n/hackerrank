#!/bin/bash
sudo mkdir -p temp && sudo chmod a+rwx temp
for f in sample-5.tar; do
    d="$(mktemp -d)"
    tar -xf "$f" -C "$d"
    find "$d" -type f -size +0 -exec mv {} {}".log" \;
    find "$d" -type f -size 0 -delete
    tar -C "$d" -cf "temp/$f" .
    echo "Done"
done