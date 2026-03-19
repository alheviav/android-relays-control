[app]

# Nombre de la aplicación
title = Control Relés RS485

# Nombre del paquete
package.name = relayscontrol

# Dominio del paquete (debe ser único)
package.domain = com.labtech

# Directorio de código fuente
source.dir = .

# Archivo principal
source.include_exts = py,png,jpg,kv,atlas

# Versión de la aplicación
version = 1.0.0

# Requisitos de Python (bibliotecas necesarias)
requirements = python3,kivy==2.3.0,pymodbus==3.5.4,pyserial==3.5,usb4a,usbserial4a

# Orientación de la pantalla (landscape = horizontal, portrait = vertical)
orientation = landscape

# Habilitar depuración
#fullscreen = 0

# Permisos de Android necesarios
android.permissions = INTERNET,WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE,USB_PERMISSION,android.hardware.usb.host

# Características de hardware requeridas
android.features = android.hardware.usb.host

# Arquitecturas de Android a compilar (arm64-v8a es más moderna, armeabi-v7a es compatible)
android.archs = arm64-v8a,armeabi-v7a

# API mínima de Android (21 = Android 5.0 Lollipop)
android.minapi = 21

# API objetivo de Android (33 = Android 13)
android.api = 33

# NDK de Android (versión recomendada)
android.ndk = 25b

# SDK de Android
android.sdk = 33

# Aceptar licencias de SDK automáticamente
android.accept_sdk_license = True

# Habilitar logcat para depuración
android.logcat_filters = *:S python:D

# Manifest XML adicional para USB
android.manifest.intent_filters = usb_host.xml

# Entrypoint
android.entrypoint = org.kivy.android.PythonActivity

# Nombre de la actividad principal
android.activity_class_name = org.kivy.android.PythonActivity

# p4a (python-for-android) configuración adicional
p4a.branch = master

# Configuración adicional
[buildozer]

# Directorio de compilación
build_dir = ./.buildozer

# Directorio de binarios
bin_dir = ./bin

# Nivel de log (0 = solo errores, 1 = normal, 2 = verbose)
log_level = 2

# Número de procesos paralelos (-1 = autodeteción)
# warn_on_root = 1
