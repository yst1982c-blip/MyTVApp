[app]

title = TV Player
package.name = tvplayer
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,js,css

version = 0.1

# 关键：补全依赖，包括 pywebview 和它的依赖包
requirements = python3,kivy,pywebview,proxy-tools,typing_extensions

android.permissions = INTERNET
android.api = 30
android.minapi = 21
android.ndk = 25c                     # 固定 NDK 版本，避免编译问题
android.archs = arm64-v8a, armeabi-v7a
fullscreen = 0
log_level = 2
android.accept_sdk_license = True

# 关键：pywebview 在 Android 上需要的支持库
android.gradle_dependencies = 'com.android.support:support-v4:28.0.0'
