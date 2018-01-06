DESCRIPTION = "QT5 package"
LICENSE = "MIT"
PR = "r1"

PACKAGE_ARCH = "${MACHINE_ARCH}"

inherit packagegroup

MB_QT_BASE = "\
    qtbase \
    qtbase-plugins \
    "

MB_QT_SERIALPORT = "\
    qtserialport \
    "

MB_QT_DECLARATIVE = "\
    qtdeclarative \
    qtquickcontrols \
    qtquickcontrols2 \
    "

MB_QT_QUICK = "\
    qtquick1 \
    qtscript \
    "

MB_QT_SVG = "\
    qtsvg \
    qtsvg-plugins \
    "

MB_QT_XMLPATTERNS = "\
    qtxmlpatterns \
    "

MB_QT_QMLPLUGINS = "\
    qtdeclarative-qmlplugins \
    qtquickcontrols-qmlplugins \
    qtquickcontrols2-qmlplugins \
    qtgraphicaleffects-qmlplugins \
    "

MB_QT_WAYLAND = "\
    qtwayland \
    qtwayland-plugins \
    "

MB_QT_DEV = "\
    openssh-sftp-server \
    "

MB_FONTS = "\
    fontconfig \
    fontconfig-utils \
    ttf-bitstream-vera \    
    "

MB_TSLIB = "\
    tslib \
    tslib-calibrate \
    tslib-conf \
    "

RDEPENDS_${PN} = "\
    ${MB_QT_BASE} \
    ${MB_QT_SERIALPORT} \
    ${MB_QT_DECLARATIVE} \
    ${MB_QT_QUICK} \
    ${MB_QT_SVG} \
    ${MB_QT_XMLPATTERNS} \
    ${MB_QT_QMLPLUGINS} \
    ${MB_QT_WAYLAND} \
    ${MB_QT_DEV} \
    ${MB_FONTS} \
    ${MB_TSLIB} \
    "

