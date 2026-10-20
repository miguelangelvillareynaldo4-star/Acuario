
[app]

# Info de tu app
title = AcuarioApp
package.name = acuarioapp
package.domain = com.miguelangel.acuarioapp

source.dir = .
source.include_exts = py,png,jpg,kv,atlas,json,ttf
source.include_patterns = assets/*,images/*

# ESTO ES LO NUEVO - AQUI ESTAN MIS FUNCIONES
# Agregué requests para buscar, duckduckgo-search para busqueda web, pillow para imagenes
version = 1.0
requirements = python3,kivy==2.3.0,kivymd==1.2.0,requests,pillow,duckduckgo-search,charset-normalizer,certifi
orientation = portrait

# Permisos para que pueda buscar y generar imagenes
android.permissions = INTERNET,ACCESS_NETWORK_STATE,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk_path = /home/runner/.buildozer/android/platform/android-sdk
android.accept_sdk_license_agreement = True

# Configuracion para que no falle mas
p4a.branch = master
p4a.build_tools_version = 33.0.3
android.build_tools_version = 33.0.3
android.archs = arm64-v8a, armeabi-v7a

[buildozer]
log_level = 2
warn_on_root = 1

# Para que el APK no pese 200MB
android.allow_backup = False
