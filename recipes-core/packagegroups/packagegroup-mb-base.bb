DESCRIPTION = "Default package"
LICENSE = "MIT"
LIC_FILES_CHKSUM = "file://${COREBASE}/meta-mb/COPYING.MIT;md5=3da9cfbcb788c80a0384361b4de20420"
PR = "r1"

PACKAGE_ARCH = "${MACHINE_ARCH}"

inherit packagegroup

MB_BASE = "\
    parted \
    mtd-utils \
    openssh-sftp \
    "

MB_ETH = "\
    iproute2 \
    "

MB_SGX = "\
    libgbm \
    ti-sgx-ddk-km \
    ti-sgx-ddk-um \
    "

MB_SAMBA = "\
    cifs-utils \
    "

RDEPENDS_${PN} = "\
    ${MB_BASE} \
    ${MB_ETH} \
    ${MB_SGX} \
    ${MB_SAMBA} \
    "
