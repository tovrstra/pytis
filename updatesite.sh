#!/bin/bash

(./cleanfiles.sh; ./cleancode.sh; cd doc; make clean; make html)
rm -rf ../pytis_html
cp -ar doc/_build/html ../pytis_html
./cleanfiles.sh
git checkout gh-pages && (
    git rm -r *;
    cp -ar ../pytis_html/* .;
    mv _static static
    for f in $(find | grep -v '/.git'); do sed -e 's/_static/static/' -i $f; done
    mv _sources sources
    for f in $(find | grep -v '/.git'); do sed -e 's/_sources/sources/' -i $f; done
    git add .;
    git commit -m 'Automatic documentation update'
)
rm -rf ../pytis_html
git checkout master
