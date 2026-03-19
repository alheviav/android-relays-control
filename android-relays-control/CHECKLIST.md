# ✅ CHECKLIST - Control Relés RS485 Android

## 📋 Archivos del Proyecto Creados

- [x] `main.py` - Aplicación principal Kivy
- [x] `control_reles_android.py` - Lógica de control RS485
- [x] `buildozer.spec` - Configuración para generar APK
- [x] `requirements.txt` - Dependencias Python
- [x] `usb_host.xml` - Permisos USB para Android
- [x] `device_filter.xml` - Filtros de dispositivos USB
- [x] `compilar.sh` - Script automático de compilación
- [x] `README.md` - Documentación completa
- [x] `GUIA_COMPILACION.md` - Guía paso a paso
- [x] Este archivo `CHECKLIST.md`

---

## 🎯 Pasos a Seguir

### ✅ PASO 1: Crear Repositorio en GitHub

- [ ] Ir a https://github.com
- [ ] Crear cuenta (si no tienes) o hacer login
- [ ] Click en "+" → "New repository"
- [ ] Nombre: `android-relays-control`
- [ ] Marcar "Public"
- [ ] Click "Create repository"

**Tiempo estimado:** 5 minutos  
**Archivo de ayuda:** `GUIA_GITHUB.md`

---

### ✅ PASO 2: Subir Archivos a GitHub

**Opción más fácil - Arrastrar archivos:**

- [ ] En GitHub, click "uploading an existing file"
- [ ] Arrastra TODOS los archivos de la carpeta `android-relays-control`
- [ ] Incluir: main.py, buildozer.spec, .github/, etc.
- [ ] Escribir mensaje: "Primera versión"
- [ ] Click "Commit changes"

**Opción con Git (si lo tienes instalado):**

Ver `GUIA_GITHUB.md` - Paso 2, Opción A

**Tiempo estimado:** 3 minutos

---

### ✅ PASO 3: Ejecutar Compilación en GitHub

- [ ] En tu repositorio, click pestaña "Actions"
- [ ] Click "I understand my workflows, go ahead and enable them"
- [ ] Click "Build Android APK" (lado izquierdo)
- [ ] Click "Run workflow" (botón derecho)
- [ ] Click "Run workflow" de nuevo

**Tiempo estimado:** 1 minuto

---

### ✅ PASO 4: Esperar Compilación

- [ ] Esperar 15-20 minutos
- [ ] Marca amarilla 🟡 = compilando
- [ ] Marca verde ✅ = listo
- [ ] Marca roja 🔴 = error (avísame)

**Tiempo estimado:** 15-20 minutos (☕ toma un café)

---

### ✅ PASO 5: Descargar el APK

- [ ] Click en el workflow completado (marca verde)
- [ ] Bajar hasta "Artifacts"
- [ ] Click en "android-apk" para descargar
- [ ] Descomprimir el archivo .zip
- [ ] **Archivo APK:** `relayscontrol-1.0.0-arm64-v8a-debug.apk`

**Tiempo estimado:** 1 minuto

---

### ✅ PASO 6: Preparar la Tablet

- [ ] Habilitar "Orígenes desconocidos" en Android:
  - Ajustes → Seguridad → Orígenes desconocidos (ON)
  - O: Ajustes → Apps → Acceso especial → Instalar apps desconocidas
  
**Tiempo estimado:** 2 minutos

---

### ✅ PASO 7: Instalar APK en Tablet

- [ ] Transferir APK a la tablet (USB/Email/Drive)
- [ ] Abrir APK en la tablet
- [ ] Tocar "Instalar"
- [ ] Aceptar permisos

**Tiempo estimado:** 3 minutos

---

### ✅ PASO 8: Conectar Hardware

- [ ] Verificar módulo de relés tiene alimentación (12V/24V)
- [ ] Conectar cables RS485 (A y B)
- [ ] Conectar: `Módulo ←[RS485]→ Conversor USB ←[OTG]→ Tablet`
- [ ] Cable OTG debe soportar **datos** (no solo carga)

**Tiempo estimado:** 5 minutos

---

### ✅ PASO 9: Probar la App

- [ ] Abrir app "Control Relés RS485"
- [ ] Aceptar permiso USB cuando lo pida
- [ ] Tocar botón 🔄 para buscar dispositivos
- [ ] Seleccionar puerto USB
- [ ] Configurar Baudrate: `9600`
- [ ] Configurar Dirección: `1`
- [ ] Tocar "CONECTAR"
- [ ] Probar botón "LEER ESTADO"
- [ ] Probar encender/apagar un relé
- [ ] ¡Funciona! 🎉

**Tiempo estimado:** 5 minutos

---

## 🔧 Hardware Necesario

### Esenciales:
- [x] Tablet Android (5.0+) con USB OTG
- [x] Cable USB OTG (USB-C o Micro-USB)
- [x] Conversor USB-RS485 (FTDI, CH340, CP2102, etc.)
- [x] Módulo de relés RS485 con Modbus RTU
- [x] Fuente de alimentación para módulo (12V/24V)
- [x] Cables RS485 (para A y B)

### Opcionales:
- [ ] Multímetro (para verificar alimentación)
- [ ] LEDs indicadores (para ver actividad)

---

## 📊 Tiempo Total Estimado

| Etapa | Primera Vez | Siguientes Veces |
|-------|-------------|------------------|
| Crear repositorio GitHub | 5 min | - |
| Subir archivos | 3 min | 1 min |
| Ejecutar workflow | 1 min | 1 min |
| Esperar compilación | 20 min | 20 min |
| Descargar APK | 1 min | 1 min |
| Instalar en tablet | 5 min | 2 min |
| Conectar hardware | 5 min | 1 min |
| **TOTAL** | **~40 min** | **~26 min** |

---

## 🆘 ¿Problemas?

### No compila en GitHub Actions
→ Ver **GUIA_GITHUB.md** sección "Problemas Comunes"

### No puedo subir archivos a GitHub
→ Usa la opción de arrastrar archivos (más fácil)

### No detecta USB en tablet
→ Ver **README.md** sección "Solución de Problemas"

### No se conecta al módulo
→ Verificar:
- Alimentación del módulo (12V/24V)
- Cables A y B bien conectados
- Baudrate correcto (prueba 9600)
- Dirección Modbus correcta (prueba 1)

---

## 📱 Información de la App

**Nombre:** Control Relés RS485  
**Versión:** 1.0.0  
**Paquete:** com.labtech.relayscontrol  
**Tamaño APK:** ~50-80 MB  
**Android mínimo:** 5.0 (API 21)  
**Permisos:** USB, Almacenamiento  

---

## 🎓 Recursos Adicionales

- **Documentación completa:** `README.md`
- **Guía de GitHub (USA ESTA):** `GUIA_GITHUB.md` ⭐
- **Guía de compilación local (WSL2):** `GUIA_COMPILACION.md` (alternativa)
- **Script automático (WSL2):** `compilar.sh` (alternativa)
- **Código fuente:** `main.py`, `control_reles_android.py`

---

## ✨ ¡Éxito!

Una vez completado todo este checklist, tendrás:

✅ Una app Android funcionando  
✅ Control total de tus relés RS485  
✅ Portabilidad con tu tablet  
✅ Independencia de la PC  

**¡Disfruta tu nueva app! 📱🎉**

---

_Última actualización: Marzo 2026_  
_Proyecto: Labtech Hebro Ltda._
