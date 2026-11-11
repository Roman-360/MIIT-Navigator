[app]
title = MIIT Navigator
package.name = miitnav
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1

# Оставляем только имена, чтобы компилятор использовал свои внутренние рецепты
requirements = python3,kivy==2.3.0,kivymd,pillow

orientation = portrait
osx.python_version = 3
osx.kivy_version = 1.9.1
fullscreen = 0
android.permissions = INTERNET
android.api = 33
android.minapi = 24
android.ndk = 25b
android.archs = arm64-v8a
android.accept_sdk_license = True

# Подключаем ветку с исправлениями багов зависимостей
p4a.branch = develop

[buildozer]
log_level = 2
warn_on_root = 1
