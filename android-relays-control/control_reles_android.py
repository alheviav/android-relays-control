"""
Control de Módulo de Relés RS485 con Modbus RTU - Versión Android
Compatible con USB OTG y conversores USB-RS485
"""

import time


class ControlReles:
    def __init__(self, port=None, baudrate=9600, slave_address=1, android_mode=False):
        """
        Inicializa la conexión con el módulo de relés
        
        Args:
            port: Puerto USB/Serial
            baudrate: Velocidad de comunicación (9600, 19200, etc.)
            slave_address: Dirección Modbus del dispositivo (1-247)
            android_mode: True para usar bibliotecas de Android
        """
        self.slave_address = slave_address
        self.baudrate = baudrate
        self.android_mode = android_mode
        self.client = None
        
        if android_mode:
            self._conectar_android(port, baudrate)
        else:
            self._conectar_pc(port, baudrate)
    
    def _conectar_android(self, port, baudrate):
        """Conectar usando librerías de Android (USB OTG)"""
        try:
            # Intentar importar bibliotecas de Android
            from usb4a import usb
            from usbserial4a import serial4a
            
            # Buscar dispositivo USB
            usb_device_list = usb.get_usb_device_list()
            
            if not usb_device_list:
                raise Exception("No se encontró ningún dispositivo USB")
            
            # Usar el primer dispositivo (generalmente el conversor RS485)
            device = usb_device_list[0]
            
            # Solicitar permiso si es necesario
            if not usb.has_usb_permission(device):
                usb.request_usb_permission(device)
                time.sleep(1)  # Esperar a que el usuario conceda permiso
            
            # Crear conexión serial
            self.serial_conn = serial4a.get_serial_port(
                device.getDeviceName(),
                baudrate,
                8,  # bytesize
                'N',  # parity
                1,  # stopbits
                timeout=1
            )
            
            if not self.serial_conn:
                raise Exception("No se pudo abrir el puerto serial")
            
            # Usar pymodbus con el serial ya abierto
            from pymodbus.client import ModbusSerialClient
            self.client = ModbusSerialClient(
                port=self.serial_conn,
                baudrate=baudrate,
                bytesize=8,
                parity='N',
                stopbits=1,
                timeout=1
            )
            
            print(f"✓ Conectado a dispositivo USB Android")
            
        except ImportError:
            # Si no están las bibliotecas de Android, intentar modo PC
            print("⚠ Bibliotecas Android no disponibles, usando modo PC")
            self._conectar_pc(port, baudrate)
        except Exception as e:
            raise Exception(f"Error al conectar en Android: {e}")
    
    def _conectar_pc(self, port, baudrate):
        """Conectar usando pymodbus estándar (PC/Testing)"""
        from pymodbus.client import ModbusSerialClient
        
        self.client = ModbusSerialClient(
            port=port,
            baudrate=baudrate,
            bytesize=8,
            parity='N',
            stopbits=1,
            timeout=1
        )
        
        if not self.client.connect():
            raise Exception(f"No se pudo conectar al puerto {port}")
        
        print(f"✓ Conectado al puerto {port} a {baudrate} bps")
    
    def encender_rele(self, numero_rele):
        """
        Enciende un relé específico (1-4)
        
        Args:
            numero_rele: Número del relé (1, 2, 3 o 4)
        """
        if numero_rele < 1 or numero_rele > 4:
            print("❌ Número de relé inválido. Use 1-4")
            return False
        
        direccion = numero_rele - 1
        
        try:
            result = self.client.write_coil(direccion, True, slave=self.slave_address)
            
            if not result.isError():
                print(f"✓ Relé {numero_rele} ENCENDIDO")
                return True
            else:
                print(f"❌ Error al encender relé {numero_rele}")
                return False
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def apagar_rele(self, numero_rele):
        """
        Apaga un relé específico (1-4)
        
        Args:
            numero_rele: Número del relé (1, 2, 3 o 4)
        """
        if numero_rele < 1 or numero_rele > 4:
            print("❌ Número de relé inválido. Use 1-4")
            return False
        
        direccion = numero_rele - 1
        
        try:
            result = self.client.write_coil(direccion, False, slave=self.slave_address)
            
            if not result.isError():
                print(f"✓ Relé {numero_rele} APAGADO")
                return True
            else:
                print(f"❌ Error al apagar relé {numero_rele}")
                return False
        except Exception as e:
            print(f"❌ Error: {e}")
            return False
    
    def leer_estado_reles(self):
        """Lee el estado actual de todos los relés"""
        try:
            result = self.client.read_coils(0, 4, slave=self.slave_address)
            
            if not result.isError():
                estados = result.bits[:4]
                print("\nEstado de los relés:")
                for i, estado in enumerate(estados, 1):
                    simbolo = "🟢 ON " if estado else "⚫ OFF"
                    print(f"  Relé {i}: {simbolo}")
                return estados
            else:
                print("❌ Error al leer estado de relés")
                return None
        except Exception as e:
            print(f"❌ Error: {e}")
            return None
    
    def encender_todos(self):
        """Enciende todos los relés"""
        print("\nEncendiendo todos los relés...")
        for i in range(1, 5):
            self.encender_rele(i)
            time.sleep(0.1)
    
    def apagar_todos(self):
        """Apaga todos los relés"""
        print("\nApagando todos los relés...")
        for i in range(1, 5):
            self.apagar_rele(i)
            time.sleep(0.1)
    
    def cerrar(self):
        """Cierra la conexión"""
        if self.client:
            try:
                self.client.close()
                print("✓ Conexión cerrada")
            except:
                pass
        
        if hasattr(self, 'serial_conn') and self.serial_conn:
            try:
                self.serial_conn.close()
            except:
                pass
    
    def verificar_conexion(self):
        """Verifica si la conexión está activa"""
        if self.client:
            return True
        return False
    
    @staticmethod
    def calcular_crc16_modbus(data):
        """Calcula CRC16 para Modbus RTU"""
        crc = 0xFFFF
        for byte in data:
            crc ^= byte
            for _ in range(8):
                if crc & 0x0001:
                    crc = (crc >> 1) ^ 0xA001
                else:
                    crc >>= 1
        return crc
    
    def enviar_comando_hex(self, comando_hex):
        """
        Envía un comando en formato hexadecimal
        
        Args:
            comando_hex: String con bytes en hex separados por espacios
                        Ej: "FF 05 00 00 FF 00 99 E4"
        """
        try:
            # Convertir string hex a bytes
            bytes_cmd = bytes.fromhex(comando_hex.replace(' ', ''))
            
            # Enviar por serial directo si está disponible
            if hasattr(self, 'serial_conn') and self.serial_conn:
                self.serial_conn.write(bytes_cmd)
                time.sleep(0.1)
                respuesta = self.serial_conn.read(100)
                return respuesta
            else:
                print("⚠ Comando HEX solo disponible con conexión serial directa")
                return None
        except Exception as e:
            print(f"❌ Error al enviar comando: {e}")
            return None
    
    def activar_rele_flash(self, numero_rele, segundos=2.0):
        """
        Activa un relé por un tiempo determinado (modo flash)
        
        Args:
            numero_rele: Número del relé (1-4)
            segundos: Tiempo en segundos
        """
        self.encender_rele(numero_rele)
        time.sleep(segundos)
        self.apagar_rele(numero_rele)
        print(f"✓ Relé {numero_rele} en modo flash completado")
