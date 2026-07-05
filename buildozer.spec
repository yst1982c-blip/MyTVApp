[app]

title = TV Player
package.name = tvplayer
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,js,css

version = 0.1
requirements = python3,kivy,pywebview,proxy-tools,typing_extensions

android.permissions = INTERNET
android.api = 28              # 降低 API 级别
android.minapi = 21
android.ndk = 19c             # 使用更稳定的 NDK
android.archs = arm64-v8a, armeabi-v7a
fullscreen = 0
log_level = 2
android.accept_sdk_license = True
android.gradle_dependencies = 'com.android.support:support-v4:28.0.0'
android.python_version = 3.11
