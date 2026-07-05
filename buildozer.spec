[app]

title = TV Player
package.name = tvplayer
package.domain = org.example

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,html,js,css

version = 0.1
requirements = python3,kivy==2.2.1,pyjnius==1.5.0,pywebview==4.2.2,proxy-tools,typing_extensions

android.permissions = INTERNET
android.api = 30
android.minapi = 21
android.ndk = 25c
android.archs = arm64-v8a, armeabi-v7a
fullscreen = 0
log_level = 2
android.accept_sdk_license = True
android.gradle_dependencies = 'com.android.support:support-v4:28.0.0'
android.python_version = 3.11
