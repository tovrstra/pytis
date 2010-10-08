#!/bin/bash

(./cleanfiles.sh; ./cleancode.sh; cd doc; make clean; make html)
cp -ar doc/_build/html ../pytis_html
git checkout gh-pages && (rm -rf *; cp -ar ../pytis_html/* .; git add .; git commit -m 'Automatic documentation update')
rm -rf ../pytis_html
git checkout master
