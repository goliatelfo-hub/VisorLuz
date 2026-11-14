[app]
title = VisorLuz
package.name = visorluz
package.domain = com.goliatelfo.visorluz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 9.9
requirements = python3,kivy==2.3.0
orientation = portrait
android.permissions = INTERNET,CAMERA
android.api = 33
android.minapi = 21
android.ndk = 25b
android.sdk = 33
android.accept_sdk_license_agreement = True
android.ant_path = /usr/share/ant
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25b
android.archs = arm64-v8a
p4a.bootstrap = sdl2

[buildozer]
log_level = 2
warn_on_root = 1
