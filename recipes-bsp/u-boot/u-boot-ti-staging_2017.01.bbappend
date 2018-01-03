FILESEXTRAPATHS_append := "${THISDIR}/${PN}-2017.01"

SRC_URI += " \
    file://0001-do-not-try-running-boot-scr.patch \
    file://0002-load-a-generic-device-tree-link.patch \
    "

