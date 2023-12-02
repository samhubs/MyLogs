
# Are you \__init__ or not?

## Introduction
### Python Packages: `__init__.py` vs. Implicit Namespace Packages

In Python, packages are a way to organize and structure code. Two common approaches for organizing code into packages are using `__init__.py` files and `implicit namespace packages`. This document explores both approaches using a simple example.

## Toy Example

Consider a package named `my_package` that contains two subpackages, `subpkg1` and `subpkg2`, each with their own modules. We want to organize this structure and make the modules accessible when we import `my_package`.

### Directory Structure
```
my_package
    __init__.py
    subpkg1
        __init__.py
        module1.py
    subpkg2
        __init__.py
        module2.py
```
Let's import the submodules in `my_package` using the two methods and compare their functionalities.

## A) Using `__init__.py` Files
1. Let's see what's inside my_package `__init__.py`\
In the my_package `__init__.py` file, we can use `__init__.py` files to organize the code and control what is imported when my_package is imported.

```python
# my_package/__init__.py

# Import submodules when the package is imported
from .subpkg1 import module1
from .subpkg2 import module2

# You can also define package-level functions or variables here

```

With this approach:

- `module1` and `module2` from `subpkg1` and `subpkg2` are automatically imported when `my_package` is imported.
- The package's namespace is organized and controlled within the __init__.py file.
- The init files within the subpackages serves the same purpose as shown below:

```py 
# my_package/subpkg1/__init__.py
# This file defines behavior for subpkg1 and imports submodules within subpkg1.

# Import submodules within subpkg1
from . import module1

# You can also define subpackage-level functions or variables here

# my_package/subpkg2/__init__.py
# This file defines behavior for subpkg2 and imports submodules within subpkg2.

# Import submodules within subpkg2
from . import module2
```

## B) Using Implicit Namespace Packages
#### `No __init__.py` Files
With implicit namespace packages, there are no `__init__.py` files. The directory structure remains the same, but you don't create `__init__.py` files in each subpackage.

```
my_package/
    subpkg1/
        module1.py
    subpkg2/
        module2.py
```

To create an implicit namespace package, you simply have the package directories without __init__.py files.

`module1.py` and `module2.py`
You can place your module files directly within the subpackage directories (`subpkg1` and `subpkg2`) without the need for `__init__.py` files.

With this approach:

- Modules `module1` and `module2` are directly within their respective subpackage directories.
- There are no `__init__.py` files.
- The package structure is created implicitly without the need for `__init__.py` files.

## Choosing Between `__init__.py` and `Implicit Namespace Packages`
The choice between using the two depends on your project's requirements and your preferred organization style. Here are some considerations:

- `__init__.py` Files: Useful for explicit control over imports, organizing code, and defining package-level variables/functions. Provides a clear namespace.

- `Implicit Namespace Packages`: Simplifies package creation and organization by omitting `__init__.py` files. Suitable for smaller, loosely organized projects.

Ultimately, the choice is yours, and you can use the approach that best fits your project's needs.