import os
import platform
import shutil

from conans import ConanFile


class HelloConan(ConanFile):
    name = "xlnt"
    version = "1.5.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "https://github.com/daguo999/xlnt"
    description = "<Description of Hello here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    generators = "cmake"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    requires = []

    def init(self):
        self.source_path = os.getcwd() + "/xlnt"

    def build(self):
        shutil.copytree(self.source_path, "./xlnt", True)

    def package(self):
        self.copy("*.h", dst="include", src="xlnt/include")
        self.copy("*.hpp", dst="include", src="xlnt/include")
        self.copy("libxlnt*.lib", dst="lib", src="xlnt/bin", keep_path=True)
        self.copy("libxlnt*.dll", dst="bin", src="xlnt/bin", keep_path=True)
        self.copy("libxlnt*.so*", dst="bin", src="xlnt/bin", keep_path=True, symlinks=True)
        self.copy("libxlnt*.dylib", dst="lib", src="xlnt/bin", keep_path=True)

    def package_info(self):
        self.cpp_info.libs = ["xlnt"]
