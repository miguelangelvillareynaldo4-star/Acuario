[app]

# Title of your application
title = AcuarioApp

# Package name
package.name = acuarioapp

# Package domain
package.domain = com.aquarium.app

# Where the source code is
source.dir = .

# Files to pack
source.include_exts = py,png,jpg,jpeg,kv,atlas

# Target platform
platform = android

# App orientation
orientation = portrait

# Build logs
log_level = 2

# Android API levels
android.api = 34
android.minapi = 21
android.ndk = 25b

# Permissions needed for camera/photos
android.permissions = CAMERA,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,INTERNET

# AndroidX support
android.enable_androidx = True

# Architecture
android.archs = arm64-v8a

# Required Python packages
requirements = python3,kivy==2.3.1,kivymd==1.1.1,pillow,plyer

# Versioning
version = 0.1.0
android.numeric_version = 1

# Debug build
debug = True
