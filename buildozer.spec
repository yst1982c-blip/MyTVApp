[app]

title = TV Player
package.name = tvplayer
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy,pywebview==4.2.2

android.permissions = INTERNET
android.api = 30
android.minapi = 21
# 删除或注释掉下面这行，让 Buildozer 使用系统自带的 NDK
# android.ndk = 25c
android.archs = arm64-v8a, armeabi-v7a
fullscreen = 0
log_level = 2
android.accept_sdk_license = True

# 关键：添加 pywebview 所需的 Android 支持库
android.gradle_dependencies = 'com.android.support:support-v4:28.0.0'

# 如果仍然失败，可以尝试以下额外配置（解除注释）：
# android.add_src = <路径>
# android.add_jar = <路径>
