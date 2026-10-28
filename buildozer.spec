[app]

title = Acuario
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
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET,AUDIO,IMAGES,RECORD_MEDIA,RECOD_AUDIO
android.window_softinput_mode = adjustResize
android.enable_androidx = True

requirements = python3,kivy,plyer,pillow

version = 0.1.0
android.numeric_version = 1
debug = True

p4a.branch = v2024.01.21
