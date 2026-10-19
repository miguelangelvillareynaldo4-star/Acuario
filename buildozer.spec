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
android.minapi = 24
android.ndk = 25b
android.ndk_api = 24
android.accept_sdk_license_agreement = True