Purpose
=======

The recipies in this layer are meant to provide a quick start into embedded 
Linux development with Qt and QML on the BeagleBone Black. You can use the
recipies to build your own linux for the BeagleBone Black and a cross-compile
toolchain for your host PC.

So what is needed for the just-works experience?
- A BeagleBone Black
- A 4D Systems "4DCAPE-70T"
- A fairly powerful PC running Ubuntu, Fedora, CentOS, Debian or openSUSE

Yocto
-----

The yocto project is a software project that provides tools to build custom
linux distributions. Its main components are bitbake, and poky. Bitbake is
the buildsystem. Poky is a reference Linux distribution that can be built
with bitbake.
