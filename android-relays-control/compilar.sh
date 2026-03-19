#!/bin/bash

# Script de compilación automatizada para Control Relés RS485 Android
# Uso: bash compilar.sh

echo "=================================="
echo "Control Relés RS485 - Compilador"
echo "=================================="
echo ""

# Colores
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
RED='\033[0;31m'
NC='\033[0m' # No Color

# Verificar que estamos en la carpeta correcta
if [ ! -f "buildozer.spec" ]; then
    echo -e "${RED}❌ Error: buildozer.spec no encontrado${NC}"
    echo "Por favor, ejecuta este script desde la carpeta del proyecto"
    exit 1
fi

echo -e "${GREEN}✓ Carpeta del proyecto verificada${NC}"
echo ""

# Verificar dependencias
echo "Verificando dependencias..."

# Java
if ! command -v java &> /dev/null; then
    echo -e "${RED}❌ Java no encontrado${NC}"
    echo "Instalando Java..."
    sudo apt install -y openjdk-17-jdk
fi
echo -e "${GREEN}✓ Java instalado${NC}"

# Buildozer
if ! command -v buildozer &> /dev/null; then
    echo -e "${RED}❌ Buildozer no encontrado${NC}"
    echo "Instalando Buildozer..."
    pip3 install buildozer cython==0.29.33
fi
echo -e "${GREEN}✓ Buildozer instalado${NC}"
echo ""

# Preguntar tipo de compilación
echo "Tipo de compilación:"
echo "  1) Debug (más rápido, para pruebas)"
echo "  2) Release (firmado, para distribución)"
read -p "Selecciona [1-2]: " BUILD_TYPE

if [ "$BUILD_TYPE" == "2" ]; then
    BUILD_CMD="buildozer android release"
    echo -e "${YELLOW}⚠ Compilación Release requiere keystore${NC}"
else
    BUILD_CMD="buildozer android debug"
    echo -e "${GREEN}Compilación Debug${NC}"
fi
echo ""

# Preguntar si limpiar compilación anterior
read -p "¿Limpiar compilación anterior? (s/n): " CLEAN
if [ "$CLEAN" == "s" ] || [ "$CLEAN" == "S" ]; then
    echo "Limpiando..."
    buildozer android clean
    echo -e "${GREEN}✓ Limpieza completa${NC}"
fi
echo ""

# Mostrar advertencia sobre tiempo
echo -e "${YELLOW}⚠ IMPORTANTE:${NC}"
echo "  - Primera compilación: 30-60 minutos"
echo "  - Compilaciones siguientes: 5-10 minutos"
echo "  - Descargará varios GB de datos"
echo ""

read -p "¿Continuar? (s/n): " CONTINUE
if [ "$CONTINUE" != "s" ] && [ "$CONTINUE" != "S" ]; then
    echo "Compilación cancelada"
    exit 0
fi

echo ""
echo "=================================="
echo "Iniciando compilación..."
echo "=================================="
echo ""

# Compilar
$BUILD_CMD

# Verificar resultado
if [ $? -eq 0 ]; then
    echo ""
    echo "=================================="
    echo -e "${GREEN}✓ COMPILACIÓN EXITOSA${NC}"
    echo "=================================="
    echo ""
    
    # Mostrar APK generado
    echo "APK generado:"
    ls -lh bin/*.apk
    echo ""
    
    # Preguntar si copiar a Windows
    read -p "¿Copiar APK al escritorio de Windows? (s/n): " COPY
    if [ "$COPY" == "s" ] || [ "$COPY" == "S" ]; then
        # Detectar usuario de Windows
        WIN_USER=$(ls /mnt/c/Users/ | grep -v "Public\|Default" | head -1)
        WIN_DESKTOP="/mnt/c/Users/$WIN_USER/Desktop"
        
        if [ -d "$WIN_DESKTOP" ]; then
            cp bin/*.apk "$WIN_DESKTOP/"
            echo -e "${GREEN}✓ APK copiado a: $WIN_DESKTOP${NC}"
        else
            echo -e "${YELLOW}⚠ No se pudo encontrar el escritorio${NC}"
            echo "Copia manualmente desde: $(pwd)/bin/"
        fi
    fi
    
    echo ""
    echo -e "${GREEN}🎉 ¡Todo listo!${NC}"
    echo ""
    echo "Próximos pasos:"
    echo "  1. Transfiere el APK a tu tablet Android"
    echo "  2. Habilita 'Orígenes desconocidos'"
    echo "  3. Instala el APK"
    echo "  4. Conecta el hardware USB OTG"
    echo "  5. ¡Disfruta!"
    
else
    echo ""
    echo "=================================="
    echo -e "${RED}❌ ERROR EN LA COMPILACIÓN${NC}"
    echo "=================================="
    echo ""
    echo "Revisa los errores arriba"
    echo ""
    echo "Soluciones comunes:"
    echo "  - Ejecuta: buildozer android clean"
    echo "  - Verifica conexión a internet"
    echo "  - Revisa que tengas espacio en disco"
    echo "  - Consulta: GUIA_COMPILACION.md"
    exit 1
fi
