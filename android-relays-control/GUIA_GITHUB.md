# 🚀 Guía: Compilar APK con GitHub Actions

## ✨ Ventajas de este método:
- ✅ **No instalas nada** en tu PC
- ✅ **GitHub compila gratis** (cuentas gratuitas tienen 2000 minutos/mes)
- ✅ **Tarda ~15-20 minutos** en compilar
- ✅ **Descargas el APK listo**

---

## 📋 Paso 1: Crear Repositorio en GitHub (5 minutos)

### 1.1 Ir a GitHub

Abre tu navegador y ve a: **https://github.com**

- Si no tienes cuenta: **Sign Up** (gratis)
- Si ya tienes cuenta: **Sign In**

### 1.2 Crear Nuevo Repositorio

1. Click en el botón **"+"** (arriba derecha)
2. Selecciona **"New repository"**
3. Configura:
   - **Repository name:** `android-relays-control`
   - **Description:** `Control de Relés RS485 para Android`
   - **Visibilidad:** ✅ Public (o Private si prefieres)
   - **NO** marcar "Initialize with README" (ya tienes archivos)
4. Click **"Create repository"**

GitHub te mostrará una página con instrucciones. **Déjala abierta.**

---

## 📤 Paso 2: Subir Código a GitHub (3 minutos)

### Opción A: Usando Git (si lo tienes instalado)

Abre PowerShell en la carpeta del proyecto:

```powershell
# Ir a la carpeta del proyecto
cd "C:\Users\ahevi\OneDrive - Labtech Hebro Ltda\Documentos\Proyectos IA\android-relays-control"

# Inicializar Git
git init
git add .
git commit -m "Primera versión de la app Android"

# Conectar con GitHub (reemplaza TU-USUARIO con tu nombre de usuario)
git remote add origin https://github.com/TU-USUARIO/android-relays-control.git
git branch -M main
git push -u origin main
```

Te pedirá credenciales de GitHub. **Importante:**
- **Username:** Tu usuario de GitHub
- **Password:** Necesitas un **Personal Access Token** (no tu contraseña normal)

#### Crear Personal Access Token:
1. En GitHub: **Settings** → **Developer settings** → **Personal access tokens** → **Tokens (classic)**
2. Click **"Generate new token (classic)"**
3. Nombre: `buildozer-upload`
4. Marcar: ✅ `repo` (todos los permisos de repositorio)
5. Click **"Generate token"**
6. **Copia el token y guárdalo** (solo se muestra una vez)
7. Usa ese token como "password" cuando git lo pida

---

### Opción B: Subir archivos manualmente (MÁS FÁCIL)

1. En la página de tu repositorio en GitHub
2. Click **"uploading an existing file"** o **"Add file"** → **"Upload files"**
3. **Arrastra TODOS los archivos** de tu carpeta `android-relays-control`:
   - main.py
   - control_reles_android.py
   - buildozer.spec
   - requirements.txt
   - usb_host.xml
   - device_filter.xml
   - README.md
   - .github (carpeta completa)
   - etc.
4. En el campo de commit escribe: `Primera versión`
5. Click **"Commit changes"**

---

## ⚙️ Paso 3: Ejecutar Compilación (1 minuto)

Una vez que los archivos estén en GitHub:

1. Ve a tu repositorio en GitHub
2. Click en la pestaña **"Actions"**
3. Si ves un mensaje de activación, click **"I understand my workflows, go ahead and enable them"**
4. Click en **"Build Android APK"** (lado izquierdo)
5. Click en **"Run workflow"** (botón derecho)
6. Click **"Run workflow"** de nuevo (confirmación)

**¡Listo!** GitHub empezará a compilar.

---

## ⏱️ Paso 4: Esperar Compilación (15-20 minutos)

Verás el progreso en tiempo real:

- 🟡 Amarillo = Compilando
- 🟢 Verde = ✅ Exitoso
- 🔴 Rojo = ❌ Error

**Tips mientras esperas:**
- Puedes cerrar la pestaña, GitHub sigue compilando
- Refresca la página para ver el progreso
- Toma un café ☕

---

## 📥 Paso 5: Descargar el APK (1 minuto)

Cuando termine (marca verde ✅):

1. Click en el nombre del workflow que se ejecutó
2. Baja hasta la sección **"Artifacts"**
3. Click en **"android-apk"** para descargar
4. Se descargará un archivo `.zip`
5. Descomprime el .zip
6. ¡Ahí está tu APK! 🎉

**Nombre del archivo:** `relayscontrol-1.0.0-arm64-v8a-debug.apk`

---

## 📱 Paso 6: Instalar en Tablet

1. Transfiere el APK a tu tablet (USB/Email/Drive)
2. Habilita "Orígenes desconocidos" en Android
3. Abre el APK desde tu gestor de archivos
4. Toca **"Instalar"**
5. ¡Listo! 🎉

---

## 🔄 Compilaciones Futuras

Cuando hagas cambios en el código:

### Opción 1: Git (recomendado)

```powershell
cd "C:\Users\ahevi\OneDrive - Labtech Hebro Ltda\Documentos\Proyectos IA\android-relays-control"
git add .
git commit -m "Descripción de los cambios"
git push
```

GitHub compilará automáticamente.

### Opción 2: Manual

1. Ve a GitHub → Tu repositorio
2. Click en el archivo que quieres editar
3. Click en el ícono del lápiz (editar)
4. Haz tus cambios
5. Click **"Commit changes"**

GitHub compilará automáticamente.

### Opción 3: Ejecutar manualmente

1. GitHub → Actions → Build Android APK
2. Run workflow

---

## ⚠️ Problemas Comunes

### "Workflow not found"

Asegúrate de subir la carpeta `.github/workflows/` completa.

### "Build failed" (compilación falló)

1. Click en el workflow que falló
2. Click en "build" para ver el log
3. Busca líneas rojas con "ERROR"
4. Copia el error y consúltame

### "Artifacts expired"

Los APK se borran después de 30 días. Solo ejecuta el workflow de nuevo.

### No puedo instalar el APK en la tablet

Ve a: Ajustes → Seguridad → Orígenes desconocidos (ON)

---

## 💡 Tips Útiles

### Ver el log de compilación

1. Actions → Click en un workflow
2. Click en "build"
3. Expande cada paso para ver detalles

### Cancelar una compilación

Si ejecutaste por error:
1. Actions → Click en el workflow en ejecución
2. Click en "Cancel workflow" (arriba derecha)

### Hacer el repositorio privado

Si no quieres que otros vean tu código:
1. Repositorio → Settings
2. Baja hasta "Danger Zone"
3. "Change visibility" → Private

GitHub Actions funciona igual en repositorios privados.

---

## 📊 Tiempos Estimados

| Paso | Tiempo |
|------|--------|
| Crear repositorio GitHub | 3 min |
| Subir archivos | 2 min |
| Ejecutar workflow | 15-20 min |
| Descargar APK | 1 min |
| Instalar en tablet | 2 min |
| **TOTAL** | **~25 min** |

---

## 🎉 ¡Listo!

Ahora tienes:
- ✅ Compilación automática en la nube
- ✅ No necesitas instalar nada
- ✅ Puedes compilar desde cualquier PC
- ✅ Historial de versiones en GitHub

**¿Necesitas ayuda?** Avísame en qué paso estás.

---

**Última actualización:** Marzo 2026  
**Proyecto:** Labtech Hebro Ltda.
