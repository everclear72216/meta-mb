
LICENSE = "MIT"

PACKAGE_ARCH = "${MACHINE_ARCH}"

PRODBUNDLE_MANIFESTVERSION = "1.0"

do_fetch[cleandirs] = "${S}"
do_patch[noexec] = "1"
do_configure[noexec] = "1"
do_compile[noexec] = "1"
do_install[noexec] = "1"
do_populate_sysroot[noexec] = "1"
do_package[noexec] = "1"
do_package_qa[noexec] = "1"
do_packagedata[noexec] = "1"
do_package_write_ipk[noexec] = "1"
do_package_write_deb[noexec] = "1"
do_package_write_rpm[noexec] = "1"

PRODBUNDLE_FSTYPE ??= "ext4"

PRODBUNDLE_SYSTEMNAME ??= ""
PRODBUNDLE_COMPONENTS ??= ""
PRODBUNDLE_SYSTEMVARIANTS ??= ""

python __anonymous() {
    from prodbundle.bundle import Bundle

    bundle = Bundle(d) 
    bundle.register_dependencies(d)
}

S = "${WORKDIR}/bundle"

python do_populate_bundle() {
    from prodbundle.bundle import Bundle

    bundle = Bundle(d)
    bundle.populate_bundle(d)
}

addtask populate_bundle after do_unpack before do_build

do_create_manifest() {
}

addtask create_manifest after do_configure before do_build

inherit deploy

do_deploy() {
}

addtask deploy after do_create_manifest before do_build
