###  Installation guide on MacOS
ref: [[macOS] Install CMake](https://gist.github.com/fscm/29fd23093221cf4d96ccfaac5a1a5c90)

### Notes:
- Sequence of compiling and running c++ code with cmake:
    1. create `CMakeLists.txt` with appropriate information and source files
    2. make a directory `/build` and cd into it
    3. run `cmake ..`
    4. run `make`
    5. `./executable_file`
- Although both `cmake .` and `cmake ..` are special cases of `cmake -S . -B`, they have subtle differences in terms of where the source and the build files are located. `cmake .` is typically run in the same directory as `CMakeLists.txt` while `cmake ..` is executed inside a build directory and it signifies that the source is in the parent `..` directory. 
- Actions associated with `cmake`:
    1. reads `CMakeLists.txt` file
    2. detects environment: compiler (gcc, clang, etc) and OS (Mac, Linux, Win)
    3. generates build and cache files need to build an executable
- The code is compiled with `make -C <Makefile location>` whose actions are:
    1. reads `Makefile`
    2. executes build rules
    3. creates executables or libraries, e.g. .exe, .so, .dll, .s.