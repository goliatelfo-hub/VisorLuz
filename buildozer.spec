[app]
title = VisorLuz
package.name = visorluz
package.domain = com.goliatelfo.visorluz
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 9.7
requirements = python3,kivy==2.3.0,requests,urllib3,charset-normalizer,idna,certifi
orientation = portrait
fullscreen = 0
android.permissions = INTERNET,ACCESS_NETWORK_STATE,CAMERA
android.api = 33
android.minapi = 21
android.ndk = 25b
android.accept_sdk_license_agreement = True
[buildozer]
log_level = 2
warn_on_root = 1
