"""
Control de Relés RS485 para Android
Aplicación Kivy para tablets con USB OTG
"""

from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.spinner import Spinner
from kivy.uix.textinput import TextInput
from kivy.uix.scrollview import ScrollView
from kivy.uix.popup import Popup
from kivy.clock import Clock
from kivy.properties import StringProperty, BooleanProperty
from kivy.graphics import Color, Rectangle
import threading
import time

# Importar módulo de control
from control_reles_android import ControlReles


class ReleButton(BoxLayout):
    """Widget personalizado para cada relé"""
    rele_num = 0
    estado = BooleanProperty(False)
    
    def __init__(self, numero, callback_on, callback_off, **kwargs):
        super().__init__(**kwargs)
        self.orientation = 'vertical'
        self.rele_num = numero
        self.callback_on = callback_on
        self.callback_off = callback_off
        
        self.size_hint_y = None
        self.height = 200
        self.padding = 10
        self.spacing = 10
        
        # Título
        titulo = Label(
            text=f'RELÉ {numero}',
            size_hint_y=None,
            height=40,
            font_size='20sp',
            bold=True
        )
        self.add_widget(titulo)
        
        # Indicador de estado
        self.estado_label = Label(
            text='● OFF',
            size_hint_y=None,
            height=40,
            font_size='18sp',
            color=(0.5, 0.5, 0.5, 1)
        )
        self.add_widget(self.estado_label)
        
        # Botones ON/OFF
        btn_layout = BoxLayout(size_hint_y=None, height=80, spacing=10)
        
        self.btn_on = Button(
            text='ON',
            font_size='24sp',
            bold=True,
            background_color=(0.3, 0.7, 0.3, 1),
            background_normal=''
        )
        self.btn_on.bind(on_press=self.on_encender)
        
        self.btn_off = Button(
            text='OFF',
            font_size='24sp',
            bold=True,
            background_color=(0.8, 0.3, 0.3, 1),
            background_normal=''
        )
        self.btn_off.bind(on_press=self.on_apagar)
        
        btn_layout.add_widget(self.btn_on)
        btn_layout.add_widget(self.btn_off)
        self.add_widget(btn_layout)
    
    def on_encender(self, instance):
        self.callback_on(self.rele_num)
    
    def on_apagar(self, instance):
        self.callback_off(self.rele_num)
    
    def actualizar_estado(self, encendido):
        self.estado = encendido
        if encendido:
            self.estado_label.text = '● ON'
            self.estado_label.color = (0.3, 0.8, 0.3, 1)
        else:
            self.estado_label.text = '● OFF'
            self.estado_label.color = (0.5, 0.5, 0.5, 1)


class RelaysControlApp(App):
    """Aplicación principal"""
    
    def build(self):
        self.title = 'Control Relés RS485'
        self.reles = None
        self.conectado = False
        
        # Layout principal
        main_layout = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Panel de conexión
        self.crear_panel_conexion(main_layout)
        
        # Panel de relés
        self.crear_panel_reles(main_layout)
        
        # Panel de control grupal
        self.crear_panel_control_grupal(main_layout)
        
        # Log
        self.crear_panel_log(main_layout)
        
        return main_layout
    
    def crear_panel_conexion(self, parent):
        """Panel de configuración de conexión"""
        panel = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=180,
            padding=5,
            spacing=5
        )
        
        # Título
        titulo = Label(
            text='CONFIGURACIÓN',
            size_hint_y=None,
            height=30,
            font_size='18sp',
            bold=True
        )
        panel.add_widget(titulo)
        
        # Fila 1: Puerto y refrescar
        fila1 = BoxLayout(size_hint_y=None, height=40, spacing=5)
        fila1.add_widget(Label(text='Puerto USB:', size_hint_x=0.3))
        self.puerto_spinner = Spinner(
            text='Seleccionar...',
            values=[],
            size_hint_x=0.5
        )
        fila1.add_widget(self.puerto_spinner)
        
        btn_refresh = Button(
            text='🔄',
            size_hint_x=0.2,
            font_size='20sp'
        )
        btn_refresh.bind(on_press=self.actualizar_puertos)
        fila1.add_widget(btn_refresh)
        panel.add_widget(fila1)
        
        # Fila 2: Baudrate y Dirección
        fila2 = BoxLayout(size_hint_y=None, height=40, spacing=5)
        fila2.add_widget(Label(text='Baudrate:', size_hint_x=0.25))
        self.baudrate_spinner = Spinner(
            text='9600',
            values=['4800', '9600', '19200'],
            size_hint_x=0.35
        )
        fila2.add_widget(self.baudrate_spinner)
        
        fila2.add_widget(Label(text='Dir:', size_hint_x=0.15))
        self.direccion_input = TextInput(
            text='1',
            multiline=False,
            input_filter='int',
            size_hint_x=0.25
        )
        fila2.add_widget(self.direccion_input)
        panel.add_widget(fila2)
        
        # Fila 3: Botones de conexión
        fila3 = BoxLayout(size_hint_y=None, height=50, spacing=10)
        
        self.btn_conectar = Button(
            text='CONECTAR',
            font_size='18sp',
            bold=True,
            background_color=(0.2, 0.6, 0.8, 1),
            background_normal=''
        )
        self.btn_conectar.bind(on_press=self.conectar)
        
        self.btn_desconectar = Button(
            text='DESCONECTAR',
            font_size='18sp',
            bold=True,
            background_color=(0.6, 0.3, 0.3, 1),
            background_normal='',
            disabled=True
        )
        self.btn_desconectar.bind(on_press=self.desconectar)
        
        fila3.add_widget(self.btn_conectar)
        fila3.add_widget(self.btn_desconectar)
        panel.add_widget(fila3)
        
        parent.add_widget(panel)
        
        # Actualizar puertos al inicio
        Clock.schedule_once(lambda dt: self.actualizar_puertos(None), 0.5)
    
    def crear_panel_reles(self, parent):
        """Panel de control de relés individuales"""
        # Grid de 2x2 para los 4 relés
        grid = GridLayout(
            cols=2,
            rows=2,
            size_hint_y=None,
            height=420,
            spacing=10,
            padding=5
        )
        
        self.rele_widgets = []
        for i in range(1, 5):
            rele_widget = ReleButton(
                i,
                self.encender_rele,
                self.apagar_rele
            )
            self.rele_widgets.append(rele_widget)
            grid.add_widget(rele_widget)
        
        parent.add_widget(grid)
    
    def crear_panel_control_grupal(self, parent):
        """Botones de control grupal"""
        panel = BoxLayout(
            size_hint_y=None,
            height=120,
            orientation='vertical',
            spacing=5,
            padding=5
        )
        
        # Fila 1
        fila1 = BoxLayout(size_hint_y=None, height=55, spacing=10)
        
        btn_todos_on = Button(
            text='TODOS ON',
            font_size='18sp',
            bold=True,
            background_color=(0.3, 0.7, 0.3, 1),
            background_normal=''
        )
        btn_todos_on.bind(on_press=lambda x: self.encender_todos())
        
        btn_todos_off = Button(
            text='TODOS OFF',
            font_size='18sp',
            bold=True,
            background_color=(0.8, 0.3, 0.3, 1),
            background_normal=''
        )
        btn_todos_off.bind(on_press=lambda x: self.apagar_todos())
        
        fila1.add_widget(btn_todos_on)
        fila1.add_widget(btn_todos_off)
        panel.add_widget(fila1)
        
        # Fila 2
        fila2 = BoxLayout(size_hint_y=None, height=55, spacing=10)
        
        btn_leer = Button(
            text='LEER ESTADO',
            font_size='18sp',
            bold=True,
            background_color=(0.5, 0.5, 0.7, 1),
            background_normal=''
        )
        btn_leer.bind(on_press=lambda x: self.leer_estado())
        
        btn_secuencia = Button(
            text='SECUENCIA',
            font_size='18sp',
            bold=True,
            background_color=(0.7, 0.5, 0.3, 1),
            background_normal=''
        )
        btn_secuencia.bind(on_press=lambda x: self.secuencia_prueba())
        
        fila2.add_widget(btn_leer)
        fila2.add_widget(btn_secuencia)
        panel.add_widget(fila2)
        
        parent.add_widget(panel)
    
    def crear_panel_log(self, parent):
        """Panel de log"""
        log_layout = BoxLayout(
            orientation='vertical',
            size_hint_y=None,
            height=150,
            spacing=5
        )
        
        log_layout.add_widget(Label(
            text='LOG',
            size_hint_y=None,
            height=25,
            font_size='16sp',
            bold=True
        ))
        
        scroll = ScrollView(size_hint=(1, 1))
        self.log_label = Label(
            text='',
            size_hint_y=None,
            font_size='12sp',
            halign='left',
            valign='top',
            text_size=(None, None)
        )
        self.log_label.bind(
            width=lambda *x: self.log_label.setter('text_size')(self.log_label, (self.log_label.width, None)),
            texture_size=lambda *x: self.log_label.setter('height')(self.log_label, self.log_label.texture_size[1])
        )
        scroll.add_widget(self.log_label)
        log_layout.add_widget(scroll)
        
        parent.add_widget(log_layout)
    
    def log(self, mensaje):
        """Agregar mensaje al log"""
        timestamp = time.strftime('%H:%M:%S')
        self.log_label.text += f'[{timestamp}] {mensaje}\n'
    
    def actualizar_puertos(self, instance):
        """Actualizar lista de puertos USB"""
        try:
            import usb4a
            from usbserial4a import serial4a
            
            device_list = usb4a.get_usb_device_list()
            puertos = []
            
            for device in device_list:
                puertos.append(f"{device.getDeviceName()}")
            
            if puertos:
                self.puerto_spinner.values = puertos
                self.puerto_spinner.text = puertos[0]
                self.log(f"✓ Encontrados {len(puertos)} dispositivos USB")
            else:
                self.puerto_spinner.values = ['No hay dispositivos']
                self.puerto_spinner.text = 'No hay dispositivos'
                self.log("⚠ No se encontraron dispositivos USB")
        except Exception as e:
            self.log(f"❌ Error al buscar puertos: {e}")
    
    def conectar(self, instance):
        """Conectar con el módulo de relés"""
        try:
            puerto = self.puerto_spinner.text
            baudrate = int(self.baudrate_spinner.text)
            direccion = int(self.direccion_input.text)
            
            if puerto == 'Seleccionar...' or puerto == 'No hay dispositivos':
                self.mostrar_popup('Error', 'Seleccione un puerto USB válido')
                return
            
            self.log(f"Conectando a {puerto} @ {baudrate} bps...")
            
            self.reles = ControlReles(
                port=puerto,
                baudrate=baudrate,
                slave_address=direccion,
                android_mode=True
            )
            
            self.conectado = True
            self.log("✓ Conectado exitosamente")
            
            self.btn_conectar.disabled = True
            self.btn_desconectar.disabled = False
            self.puerto_spinner.disabled = True
            self.baudrate_spinner.disabled = True
            self.direccion_input.disabled = True
            
            # Leer estado inicial
            Clock.schedule_once(lambda dt: self.leer_estado(), 0.5)
            
        except Exception as e:
            self.log(f"❌ Error de conexión: {e}")
            self.mostrar_popup('Error de Conexión', str(e))
    
    def desconectar(self, instance):
        """Desconectar del módulo"""
        if self.reles:
            self.reles.cerrar()
            self.reles = None
        
        self.conectado = False
        self.log("Desconectado")
        
        self.btn_conectar.disabled = False
        self.btn_desconectar.disabled = True
        self.puerto_spinner.disabled = False
        self.baudrate_spinner.disabled = False
        self.direccion_input.disabled = False
        
        # Resetear estados visuales
        for widget in self.rele_widgets:
            widget.actualizar_estado(False)
    
    def verificar_conexion(self):
        """Verificar que esté conectado"""
        if not self.conectado or not self.reles:
            self.mostrar_popup('Advertencia', 'Debe conectarse primero')
            return False
        return True
    
    def encender_rele(self, numero):
        """Encender un relé específico"""
        if not self.verificar_conexion():
            return
        
        def tarea():
            try:
                self.log(f"Encendiendo relé {numero}...")
                if self.reles.encender_rele(numero):
                    Clock.schedule_once(lambda dt: self.rele_widgets[numero-1].actualizar_estado(True), 0)
                    Clock.schedule_once(lambda dt: self.log(f"✓ Relé {numero} encendido"), 0)
            except Exception as e:
                Clock.schedule_once(lambda dt: self.log(f"❌ Error: {e}"), 0)
        
        threading.Thread(target=tarea, daemon=True).start()
    
    def apagar_rele(self, numero):
        """Apagar un relé específico"""
        if not self.verificar_conexion():
            return
        
        def tarea():
            try:
                self.log(f"Apagando relé {numero}...")
                if self.reles.apagar_rele(numero):
                    Clock.schedule_once(lambda dt: self.rele_widgets[numero-1].actualizar_estado(False), 0)
                    Clock.schedule_once(lambda dt: self.log(f"✓ Relé {numero} apagado"), 0)
            except Exception as e:
                Clock.schedule_once(lambda dt: self.log(f"❌ Error: {e}"), 0)
        
        threading.Thread(target=tarea, daemon=True).start()
    
    def encender_todos(self):
        """Encender todos los relés"""
        if not self.verificar_conexion():
            return
        
        def tarea():
            try:
                self.log("Encendiendo todos...")
                self.reles.encender_todos()
                for i, widget in enumerate(self.rele_widgets):
                    Clock.schedule_once(lambda dt, w=widget: w.actualizar_estado(True), 0)
                Clock.schedule_once(lambda dt: self.log("✓ Todos encendidos"), 0)
            except Exception as e:
                Clock.schedule_once(lambda dt: self.log(f"❌ Error: {e}"), 0)
        
        threading.Thread(target=tarea, daemon=True).start()
    
    def apagar_todos(self):
        """Apagar todos los relés"""
        if not self.verificar_conexion():
            return
        
        def tarea():
            try:
                self.log("Apagando todos...")
                self.reles.apagar_todos()
                for i, widget in enumerate(self.rele_widgets):
                    Clock.schedule_once(lambda dt, w=widget: w.actualizar_estado(False), 0)
                Clock.schedule_once(lambda dt: self.log("✓ Todos apagados"), 0)
            except Exception as e:
                Clock.schedule_once(lambda dt: self.log(f"❌ Error: {e}"), 0)
        
        threading.Thread(target=tarea, daemon=True).start()
    
    def leer_estado(self):
        """Leer estado de los relés"""
        if not self.verificar_conexion():
            return
        
        def tarea():
            try:
                estados = self.reles.leer_estado_reles()
                if estados:
                    for i, estado in enumerate(estados[:4]):
                        Clock.schedule_once(lambda dt, idx=i, est=estado: 
                                          self.rele_widgets[idx].actualizar_estado(est), 0)
                    Clock.schedule_once(lambda dt: self.log("✓ Estado actualizado"), 0)
            except Exception as e:
                Clock.schedule_once(lambda dt: self.log(f"❌ Error: {e}"), 0)
        
        threading.Thread(target=tarea, daemon=True).start()
    
    def secuencia_prueba(self):
        """Ejecutar secuencia de prueba"""
        if not self.verificar_conexion():
            return
        
        def tarea():
            try:
                Clock.schedule_once(lambda dt: self.log("Iniciando secuencia..."), 0)
                
                # Apagar todos
                self.reles.apagar_todos()
                for widget in self.rele_widgets:
                    Clock.schedule_once(lambda dt, w=widget: w.actualizar_estado(False), 0)
                time.sleep(1)
                
                # Encender uno por uno
                for i in range(1, 5):
                    self.reles.encender_rele(i)
                    Clock.schedule_once(lambda dt, idx=i-1: 
                                      self.rele_widgets[idx].actualizar_estado(True), 0)
                    time.sleep(1)
                    
                    self.reles.apagar_rele(i)
                    Clock.schedule_once(lambda dt, idx=i-1: 
                                      self.rele_widgets[idx].actualizar_estado(False), 0)
                    time.sleep(0.5)
                
                # Encender todos
                self.reles.encender_todos()
                for widget in self.rele_widgets:
                    Clock.schedule_once(lambda dt, w=widget: w.actualizar_estado(True), 0)
                time.sleep(2)
                
                # Apagar todos
                self.reles.apagar_todos()
                for widget in self.rele_widgets:
                    Clock.schedule_once(lambda dt, w=widget: w.actualizar_estado(False), 0)
                
                Clock.schedule_once(lambda dt: self.log("✓ Secuencia completada"), 0)
            except Exception as e:
                Clock.schedule_once(lambda dt: self.log(f"❌ Error: {e}"), 0)
        
        threading.Thread(target=tarea, daemon=True).start()
    
    def mostrar_popup(self, titulo, mensaje):
        """Mostrar ventana emergente"""
        content = BoxLayout(orientation='vertical', padding=10, spacing=10)
        content.add_widget(Label(text=mensaje))
        
        btn = Button(
            text='Cerrar',
            size_hint_y=None,
            height=50,
            font_size='18sp'
        )
        
        popup = Popup(
            title=titulo,
            content=content,
            size_hint=(0.8, 0.4)
        )
        
        btn.bind(on_press=popup.dismiss)
        content.add_widget(btn)
        popup.open()


if __name__ == '__main__':
    RelaysControlApp().run()
