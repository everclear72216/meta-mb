FILESEXTRAPATHS_append := "${THISDIR}/${PN}:"

DEPENDS_remove_class-target = "libxkbcommon"

# the patch currently supplied with the package is insufficient
# because the dependency has been introduced in many qmake .pro
# files ...
SRC_URI_remove = " \
    file://0001-fix-build-without-xkbcommon-evdev.patch \
    "

# ... therefore a different patch is needed to remove xkbcommon
SRC_URI += " \
    file://0001-qtwayland-remove-xkbcommon-dependency.patch \
    " 
