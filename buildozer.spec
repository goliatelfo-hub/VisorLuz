[app]
title = VisorLuz
package.name = visorluz
package.domain = com.visorluz.app
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 9.7
requirements = python3,kivy
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,CAMERA,FLASHLIGHT
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True

[buildozer]
log_level = 2

# (IMPORTANT) En GitHub
p4a.url = https://github.com/kivy/python-for-android
p4a.branch = master
