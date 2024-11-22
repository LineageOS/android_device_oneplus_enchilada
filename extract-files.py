#!/usr/bin/env -S PYTHONPATH=../../../tools/extract-utils python3
#
# SPDX-FileCopyrightText: 2024 The LineageOS Project
# SPDX-License-Identifier: Apache-2.0
#

from extract_utils.fixups_blob import (
    blob_fixup,
    blob_fixups_user_type,
)
from extract_utils.main import (
    ExtractUtils,
    ExtractUtilsModule,
)

namespace_imports = [
    'hardware/oneplus',
    'vendor/oneplus/sdm845-common',
]

blob_fixups: blob_fixups_user_type = {
    'vendor/etc/init/android.hardware.biometrics.fingerprint@2.1-service.oneplus.rc': blob_fixup()
        .regex_replace('@2.1-service\n', '@2.1-service.oneplus\n'),
}  # fmt: skip

module = ExtractUtilsModule(
    'enchilada',
    'oneplus',
    namespace_imports=namespace_imports,
    blob_fixups=blob_fixups,
    add_firmware_proprietary_file=True,
)

if __name__ == '__main__':
    utils = ExtractUtils.device_with_common(
        module, 'sdm845-common', module.vendor
    )
    utils.run()
