#!/bin/bash
for i in $(find pytis test examples | egrep "\.pyc$|\.py~$|\.pyc~$|\.bak$|\.so$") ; do rm -v ${i}; done
rm -vr doc/_build/
rmdir -v doc/_static/
rm -vr output
rm -v MANIFEST
rm -vr dist
rm -vr build
(cd examples; ./clean.sh)
