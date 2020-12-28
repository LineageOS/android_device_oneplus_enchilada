#!/bin/bash
#
# Copyright (C) 2016 The CyanogenMod Project
# Copyright (C) 2017-2020 The LineageOS Project
#
# SPDX-License-Identifier: Apache-2.0
#

set -e

export DEVICE=enchilada
export DEVICE_COMMON=sdm845-common
export VENDOR=oneplus

"./../../${VENDOR}/${DEVICE_COMMON}/setup-makefiles.sh" "$@"
