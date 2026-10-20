[app]
title = AcuarioApp
package.name = acuarioapp
package.domain = org.acuarioapp
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy==2.3.0
orientation = portrait
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 21
android.sdk = 33
android.ndk = 25b
android.build_tools = 33.0.2
android.build_tools_version = 33.0.2
android.accept_sdk_license_agreement = True
p4a.branch = v2024.01.21
p4a.bootstrap = sdl2
p4a.fork = kivy
p4a.local_recipes =

[buildozer]
log_level = 2
warn_on_root = 1

[app:android:permissions]
