SUMMARY = "Martin Bertsche's base Beaglebone Black image"

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta-mb/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"

IMAGE_FEATURES += "ssh-server-openssh package-management debug-tweaks"

inherit core-image

IMAGE_INSTALL += "\
    packagegroup-mb-base \
    "
