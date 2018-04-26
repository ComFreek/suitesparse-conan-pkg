from conans import ConanFile, CMake, tools, MSBuild

class SuitesparseConan(ConanFile):
    name = "SuiteSparse"
    version = "5.1.2"
    license = "GNU GPL"
    url = "https://github.com/ComFreek/suitesparse-conan-pkg"
    description = "Suite of sparse matrix software"
    settings = "os", "compiler", "build_type", "arch"
    options = {"shared": [False]}
    default_options = "shared=False"
    generators = "cmake"

    def source(self):
        self.run("git clone --depth 1 https://github.com/ComFreek/suitesparse-metis-for-windows.git suitesparse")
        self.run("cd suitesparse")
        # This small hack might be useful to guarantee proper /MT /MD linkage
        # in MSVC if the packaged project doesn't have variables to set it
        # properly
        tools.replace_in_file("suitesparse/CMakeLists.txt", "PROJECT(SuiteSparseProject)",
                              '''PROJECT(SuiteSparseProject)
include(${CMAKE_BINARY_DIR}/conanbuildinfo.cmake)
conan_basic_setup()''')

    def build(self):
        cmake = CMake(self)
        cmake.configure(source_folder="suitesparse")

        msbuild = MSBuild(self)
        msbuild.build("SuiteSparseProject.sln")

    def package(self):
        # Somehow self.copy("lib/*.lib", dst="lib", keep_path=False) does not copy any file
        # at all
        self.copy("**/*.lib", dst="lib", keep_path=False)
        self.copy("suitesparse/SuiteSparse/AMD/Include/*.h",
          dst="include/amd", keep_path=False)
        self.copy("suitesparse/SuiteSparse/UMFPACK/Include/*.h",
          dst="include/umfpack", keep_path=False)
        self.copy("suitesparse/SuiteSparse/SuiteSparse_config/SuiteSparse_config.h",
          dst="include/suitesparse", keep_path=False)

    def package_info(self):
        self.cpp_info.includedirs = ["include"]

        # Some directories must be globally visible because
        # some files (e.g. umfpack/umfpack.h) try to include from
        # these without specifying a relative path.
        self.cpp_info.includedirs = ["include", "include/amd", "include/suitesparse"]
        self.cpp_info.libs = ["libumfpack"]
        self.cpp_info.libdirs = ["lib"]
