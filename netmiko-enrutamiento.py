from netmiko import ConnectHandler

router_mikrotik_red_1 = {
    'device_type': 'mikrotik_routeros',
    'host':   '10.0.0.130',
    'username': 'admin',
    'password': '1234',
    'port' : 22,            # optional, defaults to 22
    'secret': '',           # optional, defaults to ''
}

router_mikrotik_red_2 = {
    'device_type': 'mikrotik_routeros',
    'host':   '10.0.0.127',
    'username': 'admin',
    'password': '1234',
    'port' : 22,            # optional, defaults to 22
    'secret': '',           # optional, defaults to ''
}

# Definir comandos a ejecutar
configurar_roter_1 = [
    '/ip dhcp-client add interface=ether1',
    
    '/ip address add address=172.26.26.1/25 interface=ether3 network=172.26.26.0',
    '/ip address add address=192.168.26.1/30 interface=ether2 network=192.168.26.0',
    
    '/ip pool add name=pool-name-1 ranges=172.26.26.2-172.26.26.126',
    '/ip dhcp-server add address-pool=pool-name-1 interface=ether3 name=dhcp-lan-1',
    '/ip dhcp-server network add address=172.26.26.0/25 gateway=172.26.26.1',
    
    '/ip firewall nat add action=masquerade chain=srcnat out-interface=ether1',
    '/ip route add dst-address=172.26.26.128/25 gateway=192.168.26.2',
    
]

# Definir comandos a ejecutar
configurar_roter_2 = [
    '/ip dhcp-client add interface=ether1',
    
    '/ip address add address=172.26.26.129/25 interface=ether3 network=172.26.26.128',
    '/ip address add address=192.168.26.2/30 interface=ether2 network=192.168.26.0',
    
    '/ip pool add name=pool-lan-2 ranges=172.26.26.130-172.26.26.254',
    '/ip dhcp-server add address-pool=pool-lan-2 interface=ether3 name=dhcp-lan-2',
    '/ip dhcp-server network add address=172.26.26.128/25 gateway=172.26.26.129',
    
    '/ip firewall nat add action=masquerade chain=srcnat out-interface=ether1',
    '/ip route add dst-address=172.26.26.0/25 gateway=192.168.26.1',
    
]

conexion = ConnectHandler(**router_mikrotik_red_1)

# Ejecutar comandos (send_config_set - para enviar comandos de configuración)
accion1 = conexion.send_config_set(configurar_roter_1)
print(accion1)

# Visualizar comandos (send_command - para enviar comandos de visualización)
accion2 = conexion.send_command('/ip address print')
print(accion2)

# Cerrar la conexión
conexion.disconnect()



conexion = ConnectHandler(**router_mikrotik_red_2)

# Ejecutar comandos (send_config_set - para enviar comandos de configuración)
accion1 = conexion.send_config_set(configurar_roter_2)
print(accion1)

# Visualizar comandos (send_command - para enviar comandos de visualización)
accion2 = conexion.send_command('/ip address print')
print(accion2)

# Cerrar la conexión
conexion.disconnect()