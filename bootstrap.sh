#!/bin/bash
projDir=$(dirname $(realpath $0))
extDir="${projDir}/ext"
rayURL="https://github.com/raysan5/raylib/releases/download/5.5/raylib-5.5_linux_amd64.tar.gz"
rayArchive="raylib-5.5_linux_amd64.tar.gz"

if [ -d $extDir ]; then
    rm -r $extDir
fi
mkdir $extDir

wget $rayURL -P "${extDir}"
tar -xzf "${extDir}/${rayArchive}" -C $extDir
rm "${extDir}/${rayArchive}"
mv "${extDir}/${rayArchive::-7}" "${extDir}/raylib"