[app]

title = AcuarioApp
package.name = acuarioapp
package.domain = com.aquarium.app

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas
platform = android
orientation = portrait

log_level = 2

android.api = 34
android.minapi = 21
android.ndk = 25b
android.ndk_path = /home/runner/.buildozer/android/platform/android-ndk-r25b
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.archs = arm64-v8a
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET
android.enable_androidx = True
android.gradle_dependencies = com.google.android.material:material:1.11.0

requirements = python3,kivy==2.3.1,kivymd==2.0.0rc4,pillow,plyer

version = 0.1.0
android.numeric_version = 1
debug = True

p4a.branch = master
