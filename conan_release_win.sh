#!/bin/sh
set -ex

SRC_DIR=`pwd`
BUILD_DIR=${SRC_DIR}/build

name=`grep "name = " conanfile.py | awk -F '["]' '{print $2}'`
version=`grep "version" conanfile.py | awk -F '["]' '{print $2}'`

cd ${BUILD_DIR}

mkdir -p xlnt/bin
cp ${BUILD_DIR}/source/lib*dll xlnt/bin
cp -rf ${SRC_DIR}/include xlnt/
cp -rf ${SRC_DIR}/conanfile.py conanfile.py

conan create . 
conan upload --all -c --force -r ElexDev ${name}/$version
