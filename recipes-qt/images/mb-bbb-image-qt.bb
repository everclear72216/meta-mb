SUMMARY = "Martin Bertsche's Beaglebone Black image with QT5 and OpenGL on Framebuffer."

LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta-mb/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"

require recipes-core/images/mb-bbb-image-base.bb

IMAGE_INSTALL += "\
    packagegroup-mb-qt5 \
    "
