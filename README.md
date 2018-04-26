# SuiteSparse Conan Package

This is a package for the C++ package manager Conan wrapping [SuiteSparse](http://suitesparse.com), a suite of sparse matrix software.

This package uses the [SuiteSparse + CMake edition called "suitesparse-metis-for-windows"](https://github.com/jlblancoc/suitesparse-metis-for-windows) provided by a third-party.

- OS support: Windows only, currently, although the underlying CMake build architecture definitely supports *nix builds.
- Compiler support: Microsoft Visual Studio only, although the underlying CMake build architecture again supports other compilers as well.

Issues and PRs, especially improving OS and compiler support, are greatly welcome!

## How to use

1. Copy `conanfile.py` into some empty directory on your PC.
2. Run `conan create . temp/libs` from that directory.
3. Add `SuiteSparse/5.1.2@temp/libs` to your project's `conanfile.txt`.


