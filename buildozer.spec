[app]

# 应用基本信息
title = TV Player
package.name = tvplayer
package.domain = org.example

# 源码与资源
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,js,css,ttf

version = 0.1

# ★★★ 关键：补全所有必需的依赖 ★★★
# proxy_tools 和 typing_extensions 是 pywebview 在 Android 上的必要依赖[reference:2]
requirements = python3,kivy,pywebview,proxy-tools,typing_extensions

# Android 平台配置
android.permissions = INTERNET
android.api = 30
android.minapi = 21
# ★★★ 关键：明确指定NDK版本，避免兼容性问题 ★★★
android.ndk = 25c
android.archs = arm64-v8a, armeabi-v7a

fullscreen = 0
log_level = 2
android.accept_sdk_license = True

# ★★★ 关键：添加 pywebview 的 Android Java 桥接库 ★★★
# 这个配置告诉 Buildozer 去哪里找 pywebview 所需的 Java 文件[reference:3]
android.add_jars = <path_to_pywebview-android.jar>
