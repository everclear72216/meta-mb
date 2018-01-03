Yocto
-----

The yocto project is a software project that provides tools to build custom
linux distributions. Its main components are bitbake, and poky. Bitbake is
the buildsystem. Poky is a reference Linux distribution that can be built
with bitbake. Bitbake reads meta data called recpies and configuration files
in order to download, patch, configure and compile the sources. It also packages
and installs the binaries in your root file system that will eventually be
converted into an image.

This project provides a yocto layer.
