
[app]

# (str) Title of your application
title = AcuarioApp

# (str) Package name
package.name = acuarioapp

# (str) Package domain (needed for android/ios packaging)
package.domain = com.aquarium.app

# (str) Source code where the main.py lives
source.dir = .

# (list) Source files to include
source.include_exts = py,png,jpg,jpeg,kv,atlas

# (list) List of platform to build for
platform = android

# (str) Android package orientation
orientation = portrait

# (list) Source files to exclude
source.exclude_exts = spec

# (bool) Indicate whether to display build logs
log_level = 2

# (int) Target Android API, should be compatible with Kivy's Android packaging
android.api = 34
android.minapi = 21
android.ndk = 25b
android.gradle_dependencies = com.google.android.material:material:1.11.0

# (list) Permissions needed by the app
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET

# (bool) Use AndroidX support
android.enable_androidx = True

# (list) Python requirements
requirements = python3,kivy==2.3.1,kivymd==1.1.1,pillow,plyer

# (list) Android architecture
android.archs = arm64-v8a

# (str) Version
version = 0.1.0

# (int) Global version code
android.numeric_version = 1

# (bool) Whether to use the debug build
debug = True

# (list) File type support
# android.add_jars =

# If you want custom icon or splash screen:
# icon.filename = %(source.dir)s/icon.png
# splash.filename = %(source.dir)s/splash.png

# Buildozer should package the app with this layout
# if additional Android-specific modules are used.
