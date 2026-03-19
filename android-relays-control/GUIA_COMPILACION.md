# 🚀 Guía Rápida: Compilar APK en WSL2

## Paso 1: Instalar WSL2 (5 minutos)

### En Windows PowerShell (como Administrador):

1. Abre **PowerShell como Administrador**:
   - Presiona `Win + X`
   - Selecciona "Windows PowerShell (Administrador)"

2. Ejecuta este comando:
```powershell
wsl --install
```

3. **Reinicia tu PC** cuando te lo pida

4. Después del reinicio, Ubuntu se abrirá automáticamente
   - Te pedirá crear un **usuario** y **contraseña**
   - Recuerda esta contraseña (la necesitarás para `sudo`)

---

## Paso 2: Configurar Ubuntu en WSL2 (10 minutos)

Abre "Ubuntu" desde el menú inicio y ejecuta estos comandos **uno por uno**:

```bash
# 1. Actualizar sistema
sudo apt update && sudo apt upgrade -y

# 2. Instalar Java (necesario para Android SDK)
sudo apt install -y openjdk-17-jdk

# 3. Instalar herramientas de compilación
sudo apt install -y build-essential git unzip zip
sudo apt install -y python3 python3-pip
sudo apt install -y zlib1g-dev libncurses5-dev libffi-dev libssl-dev

# 4. Instalar Buildozer
pip3 install --upgrade pip
pip3 install buildozer
pip3 install cython==0.29.33

# 5. Verificar instalación
buildozer --version
```

Si ves un número de versión, ¡está instalado correctamente! ✅

---

## Paso 3: Copiar Archivos al WSL2 (2 minutos)

### Opción A: Navegar directamente a tus archivos de Windows

Desde Ubuntu (WSL2):

```bash
# Navegar a la carpeta del proyecto
cd "/mnt/c/Users/ahevi/OneDrive - Labtech Hebro Ltda/Documentos/Proyectos IA/android-relays-control"

# Verificar que estás en la carpeta correcta
ls -la
```

Deberías ver los archivos: `main.py`, `buildozer.spec`, etc.

### Opción B: Copiar archivos a tu home de Linux

```bash
# Copiar todo a tu carpeta home
cp -r "/mnt/c/Users/ahevi/OneDrive - Labtech Hebro Ltda/Documentos/Proyectos IA/android-relays-control" ~/

# Ir a la carpeta copiada
cd ~/android-relays-control
```

---

## Paso 4: Compilar el APK (30-60 minutos la primera vez)

Desde la carpeta del proyecto en Ubuntu:

```bash
# Compilar (relájate, toma un café ☕)
buildozer android debug
```

**Nota importante:** La primera compilación puede tardar **30-60 minutos** porque:
- Descarga Android SDK (varios GB)
- Descarga NDK
- Descarga Python para Android
- Compila todas las dependencias

**Las siguientes compilaciones serán mucho más rápidas** (5-10 minutos).

### Durante la compilación verás:

- `Downloading Android SDK...` → Descargando SDK
- `Downloading Android NDK...` → Descargando NDK  
- `Installing requirements...` → Instalando Python para Android
- `Compiling...` → Compilando la app

### Si te pide aceptar licencias:

Escribe `y` y presiona Enter cuando veas mensajes sobre licencias.

---

## Paso 5: Obtener el APK (1 minuto)

Una vez terminada la compilación:

```bash
# Verificar que se creó el APK
ls -lh bin/

# Deberías ver algo como:
# relayscontrol-1.0.0-arm64-v8a-debug.apk
```

### Copiar el APK a Windows:

```bash
# Copiar al Escritorio de Windows
cp bin/*.apk /mnt/c/Users/ahevi/Desktop/

# O copiar a Documentos
cp bin/*.apk "/mnt/c/Users/ahevi/OneDrive - Labtech Hebro Ltda/Documentos/"
```

---

## Paso 6: Instalar en tu Tablet (3 minutos)

1. **Transferir el APK** a tu tablet:
   - USB
   - Email a ti mismo
   - Google Drive / OneDrive
   - Bluetooth

2. **Habilitar instalación de apps desconocidas:**
   - **Android 7 o anterior:**  
     Ajustes → Seguridad → "Orígenes desconocidos" (activar)
   
   - **Android 8 o superior:**  
     Ajustes → Aplicaciones → Acceso especial → "Instalar apps desconocidas" → Selecciona tu gestor de archivos → Permitir

3. **Instalar:**
   - Abre el gestor de archivos en tu tablet
   - Encuentra el archivo `.apk`
   - Tócalo y selecciona "Instalar"
   - Acepta los permisos

---

## 🎉 ¡Listo!

Ahora puedes:

1. **Conectar el hardware:**
   ```
   Módulo Relés ←[RS485]→ Conversor USB ←[OTG]→ Tablet
   ```

2. **Abrir la app** "Control Relés RS485"

3. **Conectar** y controlar tus relés

---

## 🔄 Compilaciones Futuras

Si haces cambios en el código:

```bash
# Ir a la carpeta del proyecto
cd ~/android-relays-control

# Limpiar compilación anterior (opcional)
buildozer android clean

# Compilar de nuevo (mucho más rápido)
buildozer android debug

# Copiar nuevo APK
cp bin/*.apk /mnt/c/Users/ahevi/Desktop/
```

---

## ⚠️ Problemas Comunes

### "buildozer: command not found"

Agrega Python a tu PATH:

```bash
echo 'export PATH=$PATH:~/.local/bin' >> ~/.bashrc
source ~/.bashrc
```

### "Java not found"

Verifica la instalación de Java:

```bash
java -version

# Si no aparece, reinstala:
sudo apt install -y openjdk-17-jdk
```

### "Permission denied"

Dale permisos a buildozer:

```bash
chmod +x ~/.local/bin/buildozer
```

### Errores de espacio en disco

WSL2 puede necesitar espacio. Limpia:

```bash
# Limpiar buildozer
buildozer android clean

# Limpiar APT
sudo apt clean
```

---

## 📞 ¿Necesitas Ayuda?

Si algo no funciona:

1. **Copia el mensaje de error completo**
2. **Toma captura de pantalla**
3. **Comparte el log** del final de la compilación

---

**¡Éxito con tu app! 🚀📱**
