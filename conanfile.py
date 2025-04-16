from conans import ConanFile
from conan.tools.cmake import CMake, CMakeToolchain
from conan.tools.layout import cmake_layout


class HelloConan(ConanFile):
    name = "xlnt"
    version = "1.5.1"
    license = "<Put the package license here>"
    author = "<Put your name here> <And your email here>"
    url = "https://github.com/daguo999/xlnt"
    description = "<Description of Hello here>"
    topics = ("<Put some tag here>", "<here>", "<and here>")
    settings = "os", "compiler", "build_type", "arch"
    generators = "CMakeToolchain", "CMakeDeps"
    options = {"shared": [True, False]}
    default_options = {"shared": True}
    requires = []
    exports_sources = ["*"]

    def layout(self):
        cmake_layout(self)

    def generate(self):
        toolchain_file = self.conf.get("user.toolchain_file", default=None)
        print("toolchain_file", toolchain_file)
        tc = CMakeToolchain(self)
        # tc.variables["CMAKE_CXX_FLAGS"] = "${CMAKE_CXX_FLAGS} -static-libstdc++"
        if toolchain_file:
            tc.variables["CMAKE_TOOLCHAIN_FILE"] = toolchain_file
        tc.generate()

    def build(self):
        cmake = CMake(self)
        toolchain_file = self.conf.get("user.toolchain_file", default=None)
        if toolchain_file:
            cmake._toolchain_file = toolchain_file
        cmake.configure()
        cmake.build()

    def package(self):
        cmake = CMake(self)
        cmake.install()

    def package_info(self):
        self.cpp_info.libs = ["xlnt"]
