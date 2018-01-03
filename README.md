Purpose
=======

The recipies in this layer are meant to provide a quick start into embedded 
Linux development with Qt and QML on the BeagleBone Black. You can use the
recipies to build your own Linux for the BeagleBone Black and a cross-compile
toolchain for your host PC.

So what is needed for the just-works experience?
- A BeagleBone Black
- A 4D Systems "4DCAPE-70T"
- A fairly powerful PC running Ubuntu, Fedora, CentOS, Debian or openSUSE
- A fair amount of free disk space in the area of 50+ GB

What will you get?
- A bootloader (u-boot) configured to load a kernel that supports the 4DCAPE-70T
- A linux kernel that is SGX enabled (uses the AM3358's graphics accelerator).
- A root filesystem providing:
  - Qt5.9.3
  - SSH + SFTP
  - Busybox tools

There will be no X11 installed on the system!

Steps
=====

Use these steps to generate the linux image.

1 Install Tools
---------------

There are a couple of tools required for the build to run. You can install them
using your favourite package manager. 

For debian you would do:

```shell
$ sudo apt-get install gaw wget git-core diffstat unzip build-essential chrpath \
libsdl1.2-dev xterm curl texinfo lzop
```
The list may not be complete so if the build fails check the logs pointed to in
the error message for "command not found" errors.

2 Clone Poky
------------

The second step is to clone the poky distribution's meta data into a directory
of your choice. Poky's working directory will also be the base for any further 
steps. You will also need to clone additional git repositories into the working
directory.

```shell
$ git clone -b rocko git://git.yoctoproject.org/poky.git <workingdir>
$ cd <workingdir>
$ git clone -b rocko git://git.openembedded.org/meta-openembedded
$ git clone -b rocko git://git.yoctoproject.org/meta-ti
$ git clone -b rocko https://github.com/meta-qt5/meta-qt5
$ git clone -b rocko https://github.com/everclear72216/meta-mb.git
```

3 Environment Setup and Configuration
-------------------------------------

Once you have acquired all the meta data you need to setup a bibake build 
environment. Since bitbake came with poky, all you have to do is source the
environment script in your *workingdir*.

```shell
$ source oe-init-build-env [<builddir>]
```

The *builddir* is an optional argument that specifies where bitbake shall do all
of its work. For now I will assume that you omitted *builddir* so you will end
up with `<workingdir>/build`. The script will automatically change the directory
to your *builddir*. It has already been populated by the script with some files.
The `<builddir>/conf/bblayers.conf` and `<builddir>/conf/local.conf` need to be
replaced with the examples provided by `meta-mb`.

```shell
$ mv ../meta-mb/conf/local.conf.example conf/local.conf
$ mv ../meta-mb/conf/bblayers.conf.example conf/bblayers.conf
```

4 Start Building Linux
----------------------

With the configuration all setup it is time to start building.

```shell
$ bitbake mb-bbb-image-qt
```

Note that bitbake will build everything from scratch so this process will
take several hours when executed for the first time. Do also note that due to
downtime of remote repositories it may not finish the first time. You may have
to repeat the command a couple of times until it eventually succeeds. Do exepect
bitbake to consume all of your machine's resources up to the point that it
becomes unusable. It is best to run everything on a server and check back on the
process every half hour or so.

When Linux is built you're only half-way there. You also need to build the SDK
so you can create apps for the BeagleBone on your host machine. The following
command will build the SDK for you.

```shell
$ bitbake meta-toolchain-qt5
```

5 Create an SD-Card Image for the BeageBone Black
-------------------------------------------------

There are a lot of manuals out there on how to properly create an SD-Card image
that the BeagleBone Black can boot from. I found [this][1] one to be very good.
Note that only the partitioning part and the formatting of the boot partition
are really important. The rest is just a matter of copying the bootloader and
writing the root file system image to the right partition.

The required build artifacts can be found deep in the build tree so you need to:

```shell
$ pushd tmp/deploy/images/beaglebone-mb-board/
```

The directory will contain a lot of files most of which are links to give the
actual build artifacts more user friendly names. The build artifacts have rather
complex names in order to guarantee uniqueness. The links we will be using
always point to the artifacts generated by the latest build.

### 5.1 Copy u-boot to your SD-Card

Due to the limited internal RAM of the AM335x series of processors loading
u-boot is a two-step process. A Secondary Program Loader (a smaller version of
u-boot which only initializes external RAM) must be loaded before the actual
u-boot image can be loaded to external RAM. Therefore we need to place two files
in the boot partition of the SD-Card. Assuming your SD-Card was auto-mounted in
the media filesystem you will need to issue the following commands:

```shell
$ sudo cp MLO u-boot.img /media/<username>/boot/
```

### 5.2 Write the Root File System to the SD-Card

You will need to determine which entry in the /dev filesystem corresponds to the
root file system partition on the SD-Card. I usally do a `du -h` to see which
device corresponds to the `boot` partition. If the device is `/dev/sd<x>1` the
root file system partition will be `/dev/sd<x>2`. So to write the root file
system you need to:

```shell
$ sudo dd if=mb-bbb-image-qt-beaglebone-mb-board.ext4 of=/dev/sd<x>2
```

The root filesystem size is currently limited to 300 MB. So if you want to use
the entire space allocated for the partition you need to resize the filesystem:

```shell
$ sudo resize2fs /dev/sd<x>2
```

Make sure to unmount the SD-Card before removing it from the slot.

### 5.3 Boot the BeagleBone Black from the SD-Card

In order to boot the BeagleBone Black from the SD-Card disconnect the board from
power. Insert the SD-Card into the slot. Depress the boot button which is locted
on the top side over the SD-Card slot. Reconnect the board to power and release
the boot button after a second or so.

6 SDK 
-----

In order to compile software for the BeagleBone Black you need to install the
SDK that was built earlier. The SDK comes in an install script that contains all
the binaries. So you only need one file to deploy the SDK to another machine.

```shell
$ sudo <builddir>/tmp/deploy/sdk/beaglebone-mb-distro-glibc-x86_64-meta-toolchain-qt5-armv7ahf-neon-toolchain-1.0.sh
```

The script will ask you where to install the SDK. It will take a while to
extract and copy all the files.

After installation, whenever you wish to build software for the BeageBone Black
you need to source the environment script before calling any build scripts:

```shell
$ source <sdk_install_dir>/environment-setup-armv7ahf-neon-element14-linux-gnueabi
```

*Now you're done! Happy coding!*

[1]: https://github.com/linneman/planck/wiki/How-to-create-a-Boot-SD-Card-for-the-BeagleBone-black
