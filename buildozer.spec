[app]
title = AcuarioApp
package.name = acuarioapp
package.domain = org.acuarioapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.accept_sdk_license_agreement = True
p4a.branch = v2024.01.21
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
