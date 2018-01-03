FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}-4.9:"
FILESEXTRAPATHS_prepend := "${THISDIR}/${PN}-4.9/ti33x:"

LINUX_VERSION = "4.9"
LINUX_VERSION_EXTENSION = "-ti-mb"

SRC_URI += "file://defconfig \
    file://0001-dts-Revoke-Beaglebone-i2c2-cape-definitions.patch \
    file://0002-dts-Add-custom-dts-files.patch \
    "

KERNEL_DEVICETREE_beaglebone-mb-board = "am335x-boneblack.dtb \
    bbb-hdmi.dtb \
    bbb-nohdmi.dtb \
    bbb-4dcape43t.dtb \
    bbb-4dcape70t.dtb \
    "

KERNEL_DEFAULT_DEVICETREE ?= "bbb-4dcape70t.dtb"

do_default_dtb_symlink() {
    ln -sf ${KERNEL_DEFAULT_DEVICETREE} ${D}/${KERNEL_IMAGEDEST}/devicetree.dtb 
}

do_install[postfuncs] += "do_default_dtb_symlink"
