[app]

title = TV Player
package.name = tvplayer
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas

version = 0.1
requirements = python3,kivy,pywebview

android.permissions = INTERNET
android.api = 30
android.minapi = 21
android.ndk = 25c
android.archs = arm64-v8a, armeabi-v7a
fullscreen = 0
log_level = 2
android.accept_sdk_license = True