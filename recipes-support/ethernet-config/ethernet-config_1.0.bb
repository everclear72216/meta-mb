SUMMARY = "Configuration file to enable ethernet connection with networkd"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta-witekio/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"

FILESEXTRAPATHS_prepend := "${THISDIR}/conf-file:"

SRC_URI = "file://dhcp.network \
          "

#FILES_${PN} += "{sysconfdir}/systemd/network/wired.network"

do_install () {
	install -d ${D}${sysconfdir}/systemd/network/
	install -m 0644 ${WORKDIR}/dhcp.network ${D}${sysconfdir}/systemd/network/wired.network
}
                
RDPEPENDS_${PN} = "systemd"
