[app]
title = AcuarioApp
package.name = acuarioapp
package.domain = org.acuario
source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json
version = 1.0
orientation = portrait
requirements = python3,kivy

[buildozer]
log_level = 2

[app:android]
android.permissions = INTERNET
android.archs = arm64-v8a
p4a.bootstrap = sdl2
android.api = 33
android.minapi = 21
android.ndk = 28c
android.ndk_api = 21
p4a.build_tools_version = 33.0.3
android.sdk-path = /home/runner/buildozer/andrid/platform/android-sdk
p4a.branch = master
