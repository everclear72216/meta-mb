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
- A fair amount of free disk space in the area of 50+ GB

What will you get?
- A bootloader (u-boot) configured to load a kernel that supports the 4DCAPE-70T
- A linux kernel that is SGX enabled (i.e. makes use of the hardware graphics
accelerator embedded in the TI AM3358 microcontroller).
- A root filesystem providing:
  - Qt5.9.3
  - SSH + SFTP
  - Busybox tools

There will be no X11 installed on the system!

Steps
=====

Use these steps to generate the linux image.

1 Install Required Tools
------------------------

There are a couple of tools required for the build to run. You can install them
using your favourite package manager. 
- gawk
- wget
- git-core
- diffstat
- unzip
- build-essential
- chrpath
- libsdl1.2-dev
- xterm
- curl
- texinfo
- lzop
The list may not be complete so if the build fails check the logs pointed to in
the error message "command not found" errors.

2 Clone Poky
------------

The second step is to clone the poky distribution's meta data into a directory
of your choice. This directory will also be the base for any further steps. You
will also need to clone additional git repositories into the working directory
of poky. 

