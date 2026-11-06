# SPDX-License-Identifier: MIT
zephyr_include_directories(include)
if(CONFIG_ZMK_DEFAULT_LAYER AND CONFIG_ZMK_SPLIT_ROLE_CENTRAL)
  target_sources(app PRIVATE drivers/keymap/default_layer.c)
endif()
