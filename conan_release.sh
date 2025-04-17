#!/bin/sh
set -ex

SRC_DIR=`pwd`
BUILD_DIR=/tmp/build_xlnt
INSTAILL_DIR=tmp/install_xlnt

name=`grep "name = " conanfile.py | awk -F '["]' '{print $2}'`
version=`grep "version" conanfile.py | awk -F '["]' '{print $2}'`

rm -rf ${BUILD_DIR} && mkdir ${BUILD_DIR}
cd ${BUILD_DIR}

cmake -S ${SRC_DIR} -B ${BUILD_DIR} -DCMAKE_BUILD_TYPE=Release
make -j12

patchelf --set-rpath '$ORIGIN:../lib:.:..' ${BUILD_DIR}/source/libxlnt.so

mkdir -p xlnt/bin
cp ${BUILD_DIR}/source/lib*so* xlnt/bin
cp -rf ${SRC_DIR}/include xlnt/
cp -rf ${SRC_DIR}/conanfile.py conanfile.py

conan create . 
conan upload --all -c --force -r ElexDev ${name}/$version
