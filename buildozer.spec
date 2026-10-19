[app]

# (str) Title of your application
title = AcuarioApp

# (str) Package name
package.name = acuarioapp

# (str) Package domain (needed for android packaging)
package.domain = org.acuario

# (str) Source file where the .py files exist
source.dir = .

# (list) Source files to include (let it empty to include all files)
source.include_exts = py,png,jpg,kv,atlas

# (list) Application version
version = 1.0

# (list) Supported orientations
orientation = portrait

# (list) Permissions
android.permissions = INTERNET

# (str) Supported architectures
android.archs = arm64-v8a

# (list) Requirements
requirements = python3,kivy

# --- CONFIGURACIÓN ESTABLE DEL SDK ---
android.api = 33
android.minapi = 24
android.ndk = 25b
andride.ndk_api =24
android.accept_sdk_license = true
