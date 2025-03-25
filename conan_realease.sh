#!/bin/sh
set -ex

name=`grep "name = " conanfile.py | awk -F '["]' '{print $2}'`
version=`grep "version" conanfile.py | awk -F '["]' '{print $2}'`
conan create . 
conan upload --all -c --force -r ElexDev ${name}/$version
