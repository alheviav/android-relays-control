# Control de Relés RS485 para Android

Aplicación Android para controlar módulos de relés RS485 via USB OTG con protocolo Modbus RTU.

## 📱 Características

- ✅ Control de 4 relés individuales
- ✅ Botones ON/OFF con retroalimentación visual
- ✅ Control grupal (TODOS ON/OFF)
- ✅ Lectura de estado en tiempo real
- ✅ Secuencia de prueba automática
- ✅ Interfaz táctil optimizada para tablets
- ✅ Soporte USB OTG con conversores USB-RS485
- ✅ Log de actividad integrado

## 🔌 Hardware Requerido

1. **Tablet Android** con soporte USB OTG (Android 5.0+)
2. **Cable USB OTG** (USB-C o Micro USB según tu tablet)
3. **Conversor USB-RS485** (compatible con FTDI, CH340, CP2102, PL2303)
4. **Módulo de relés RS485** con Modbus RTU
5. **Cables RS485** (conectar A y B del conversor al módulo)

## 🛠️ Compilar la Aplicación

### Opción 1: Usando WSL2 en Windows (Recomendada)

#### Paso 1: Instalar WSL2

Abre PowerShell como Administrador y ejecuta:

```powershell
wsl --install
```

Reinicia tu PC y luego abre Ubuntu desde el menú inicio.

#### Paso 2: Configurar WSL2

Dentro de Ubuntu (WSL2), ejecuta:

```bash
# Actualizar paquetes
sudo apt update
sudo apt upgrade -y

# Instalar dependencias
sudo apt install -y python3 python3-pip git openjdk-17-jdk unzip
sudo apt install -y build-essential libssl-dev libffi-dev python3-dev
sudo apt install -y zip zlib1g-dev libncurses5-dev libgdbm-dev libnss3-dev
sudo apt install -y libreadline-dev libsqlite3-dev wget libbz2-dev

# Instalar Cython y Buildozer
pip3 install --upgrade pip
pip3 install cython==0.29.33
pip3 install buildozer
```

#### Paso 3: Copiar archivos al WSL2

Desde PowerShell de Windows:

```powershell
# Navegar a la carpeta del proyecto
cd "C:\Users\ahevi\OneDrive - Labtech Hebro Ltda\Documentos\Proyectos IA\android-relays-control"

# Copiar todo a WSL (ajusta 'usuario' por tu nombre de usuario en WSL)
wsl cp -r . /home/usuario/android-relays-control/
```

O alternativamente, desde WSL puedes acceder a tus archivos de Windows en:
```bash
cd /mnt/c/Users/ahevi/OneDrive\ -\ Labtech\ Hebro\ Ltda/Documentos/Proyectos\ IA/android-relays-control/
```

#### Paso 4: Compilar el APK

En WSL2 (Ubuntu):

```bash
# Ir a la carpeta del proyecto
cd ~/android-relays-control

# Primera compilación (tarda ~30-60 minutos)
buildozer android debug

# El APK se generará en:
# ./bin/relayscontrol-1.0.0-arm64-v8a-debug.apk
```

#### Paso 5: Transferir el APK a tu tablet

El APK estará en la carpeta `bin/`. Puedes:

1. Copiarlo a Windows:
```bash
cp bin/*.apk /mnt/c/Users/ahevi/Desktop/
```

2. Transferirlo a tu tablet vía:
   - Cable USB
   - Email
   - Google Drive
   - Cualquier otro método

### Opción 2: Compilación en la Nube (GitHub Actions)

Si no quieres instalar nada localmente, puedes usar GitHub Actions. Contacta para configurarlo.

## 📲 Instalar en la Tablet

1. Habilita "Orígenes desconocidos" en tu tablet:
   - **Ajustes** → **Seguridad** → **Orígenes desconocidos** (ON)
   - O: **Ajustes** → **Aplicaciones** → **Acceso especial** → **Instalar apps desconocidas**

2. Copia el APK a tu tablet

3. Abre el archivo `.apk` desde el gestor de archivos

4. Toca **Instalar**

## 🚀 Uso de la Aplicación

### Primera Vez

1. **Conecta el hardware:**
   ```
   Módulo Relés ←[RS485 A/B]→ Conversor USB-RS485 ←[USB OTG]→ Tablet
   ```

2. **Alimentación:**
   - Asegúrate de que el módulo de relés tenga alimentación (12V/24V)

3. **Abre la aplicación:**
   - Al conectar el USB te pedirá permiso
   - Acepta el permiso USB

### Conectar

1. Toca el botón **🔄** para buscar dispositivos USB
2. Selecciona el puerto USB de la lista
3. Configura:
   - **Baudrate**: Típicamente `9600` (verifica tu módulo)
   - **Dirección**: `1` (predeterminada de fábrica)
4. Toca **CONECTAR**

### Controlar Relés

- **Relé individual**: Toca ON/OFF en cada relé
- **Todos**: Usa los botones **TODOS ON** / **TODOS OFF**
- **Leer estado**: Toca **LEER ESTADO** para actualizar
- **Secuencia**: Toca **SECUENCIA** para una prueba automática

## ⚙️ Configuración del Módulo

### Baudrates Comunes
- `9600` bps (más común)
- `19200` bps
- `4800` bps

### Direcciones Modbus
- `1` - Predeterminada de fábrica
- `1-247` - Direcciones válidas

## 🔍 Solución de Problemas

### No detecta el dispositivo USB

1. **Verifica el cable OTG:** Muchos cables son solo de carga, no de datos
2. **Permisos USB:** Asegúrate de aceptar el permiso cuando lo solicite
3. **Reinicia la tablet** con el USB conectado
4. **Prueba otro puerto USB** (si tu tablet tiene múltiples)

### No se conecta al módulo

1. **Verifica cables RS485:** A y B bien conectados
2. **Alimentación del módulo:** Debe tener 12V/24V
3. **Baudrate correcto:** Intenta 9600, 19200, 4800
4. **Dirección Modbus:** Verifica que sea `1` o la correcta
5. **Polaridad A/B:** Puede estar invertida, cámbialas

### La app se cierra

1. **Revisa el log:** Mira los mensajes en el panel LOG
2. **Permisos USB:** Ve a Ajustes → Apps → Control Relés RS485 → Permisos
3. **Reinstala la app**

## 📁 Estructura del Proyecto

```
android-relays-control/
├── main.py                     # Aplicación principal Kivy
├── control_reles_android.py    # Lógica de control RS485
├── buildozer.spec             # Configuración de compilación
├── requirements.txt           # Dependencias Python
├── usb_host.xml              # Configuración USB Android
├── device_filter.xml         # Filtros de dispositivos USB
└── README.md                 # Esta documentación

bin/                          # APK compilado (generado)
.buildozer/                   # Archivos de compilación (generado)
```

## 🔧 Desarrollo

### Probar en PC (sin compilar)

Puedes probar la app en tu PC:

```bash
python main.py
```

Nota: Necesitarás tener el conversor USB-RS485 conectado a tu PC.

### Personalizar

- **Cambiar colores:** Edita `main.py` en las secciones `background_color`
- **Más relés:** Modifica el bucle `range(1, 5)` a `range(1, 9)` para 8 relés
- **Comandos adicionales:** Agrega funciones en `control_reles_android.py`

## 📝 Licencia

Proyecto creado para Labtech Hebro Ltda.

## 🆘 Soporte

Para problemas o preguntas, contacta al equipo de desarrollo.

---

**Versión:** 1.0.0  
**Fecha:** Marzo 2026  
**Compatible con:** Android 5.0+ (API 21+)
