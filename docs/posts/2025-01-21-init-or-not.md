# Are you `__init__` or not?

<p class="post-meta">January 21, 2025 · 5 min read · Python</p>

Python packaging looks simple until it does not. One of the first design choices people run into is whether a package should include `__init__.py` files everywhere, or whether it should rely on implicit namespace packages instead.

Both work. They just optimize for slightly different things.

## The toy structure

Imagine a package called `my_package` with two subpackages:

```text
my_package
    __init__.py
    subpkg1
        __init__.py
        module1.py
    subpkg2
        __init__.py
        module2.py
```

The question is what those `__init__.py` files buy us, and what changes when we remove them.

## Option A: explicit packages with `__init__.py`

With classic packages, the top-level `__init__.py` can define the public shape of the package:

```python
from .subpkg1 import module1
from .subpkg2 import module2
```

That means importing `my_package` can also expose selected submodules directly. The file becomes a small control surface for package behavior rather than just a marker.

The same idea applies one level down:

```python
# my_package/subpkg1/__init__.py
from . import module1

# my_package/subpkg2/__init__.py
from . import module2
```

This style is useful when:

- you want explicit control over what importing the package does
- you want a clear namespace boundary
- you need package-level setup, exports, or compatibility glue

In other words, `__init__.py` is not just ceremony. It can be part of the API design.

## Option B: implicit namespace packages

Now remove every `__init__.py`:

```text
my_package/
    subpkg1/
        module1.py
    subpkg2/
        module2.py
```

Python can still treat this structure as a package. The package exists implicitly through the directory layout itself.

This style is nice when:

- the package layout is simple
- you do not need import-time behavior
- you want less boilerplate
- parts of the package may live across multiple directories or distributions

The tradeoff is that you lose the natural place where explicit package behavior would normally live.

## Which one should you choose?

If you are building a small or medium project and you care about predictability, `__init__.py` is usually the more readable default. It makes package boundaries obvious and gives you a home for exports when the project grows.

If you want the lightest possible structure, or you are deliberately using namespace-package behavior, implicit namespaces are perfectly valid and sometimes cleaner.

## The practical rule I use

I treat `__init__.py` as the default when I want the package to feel intentional. I skip it when I genuinely want the directory tree to stay passive.

That sounds like a small distinction, but in practice it is the difference between "this package has an interface" and "this folder just happens to contain Python modules."
