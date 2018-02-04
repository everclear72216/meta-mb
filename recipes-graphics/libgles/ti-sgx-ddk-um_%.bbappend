FILESEXTRAPATHS_append := "${THISDIR}/${PN}:"

# this package contains a service file that will be enabled on install
# - default behavior -
inherit systemd

SYSTEMD_SERVICE_${PN} := "${PN}.service"
SYSTEMD_AUTO_ENABLE := "enable"

SRC_URI += " \
    file://${PN}.service \
    file://0001-change-default-color-format-rgb565.patch \
    "

do_install_usermode_service() {
    install -D -m 0644 ${WORKDIR}/${PN}.service ${D}${systemd_system_unitdir}/${PN}.service
}

do_install[postfuncs] += "do_install_usermode_service"
