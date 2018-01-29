# the system this bundle is compatible with
PRODBUNDLE_SYSTEMNAME = "UC"

# the system variants this bundle is compatible with
PRODBUNDLE_SYSTEMVARIANTS = "S M L XL"

# the components receiving software from this bundle
PRODBUNDLE_COMPONENTS = "hmi"

# the artifacts to be bundled for the hmi
PRODBUNDLE_ARTIFACTS_hmi = "rootfs"
PRODBUNDLE_CONNECTION_hmi = "userdefined"

# the rootfs image to be bundled
PRODBUNDLE_ARTIFACT_rootfs = "mb-bbb-image-qt"
PRODBUNDLE_ARTIFACT_rootfs[format] = "bin"
PRODBUNDLE_ARTIFACT_rootfs[downgrade] = "yes"
PRODBUNDLE_ARTIFACT_rootfs[type] = "diskimage"
PRODBUNDLE_ARTIFACT_rootfs[name] = "winterhalter-image.ext4"
PRODBUNDLE_ARTIFACT_rootfs[version.type] = "dotted"
PRODBUNDLE_ARTIFACT_rootfs[checksum.type] = "sha256"

inherit mbbundle
