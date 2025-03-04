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
- We can understand the anatomy of a program here. Suppose we have three files: main.cpp, my_math.h, and my_math.cpp.

```c++
// my_math.h
#ifndef MY_MATH_H
#define MY_MATH_H

int add(int a, int b); // Function declaration

#endif

// my_math.cpp
#include "my_math.h"

int add(int a, int b) {
  return a + b;
}

// main.cpp
#include <iostream>
#include "my_math.h" // Include custom header

int main() {
  int x = 5, y = 3;
  int sum = add(x, y); // Call the function declared in my_math.h
  std::cout << "The sum is: " << sum << std::endl;
  return 0;
}
```

`CMakeLists.txt`:
```cmake
cmake_minimum_required(VERSION 3.10)
project(MathProgram)

add_executable(math_program main.cpp my_math.cpp)
```

Let's trace the steps:

1. Preprocessing (main.cpp):

The preprocessor includes the contents of <iostream> and "my_math.h" into main.cpp.

2. Compilation (main.cpp):

The compiler translates the preprocessed main.cpp into assembly code.

The assembler converts the assembly code into machine code, creating the main.o object file.

The main.o file contains machine code for main(), including a call to the add function. However, at this point, the compiler only knows of the add function (from the header file), it does not yet have the implementation.

3. Preprocessing and Compilation (my_math.cpp):

The preprocessor includes "my_math.h" into my_math.cpp.

The compiler and assembler translate my_math.cpp into the my_math.o object file.

The my_math.o file contains the machine code implementation of the add function.

4. Linking:

The linker takes main.o and my_math.o.

It finds the machine code for add() in my_math.o and links it with the call to add() in main.o. This resolves the external reference.

The linker also includes code from the standard C++ library (e.g., for std::cout). This is usually done dynamically (the code is not copied into the executable itself, but rather a pointer to the code in the shared library).

The linker creates the final executable file, math_program.

5. Execution: When you run math_program, the operating system loads the executable into memory, the code is executed, and you see "The sum is: 8" printed to the console.