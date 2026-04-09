from django.db import connections


 #---------------------------------MARCAS-----------------------------------#

def listar_marcas():
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM marcas
            WHERE estado='1'
        """)
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros

def contador_marcas():
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT count(id) as contador
            FROM marcas
            WHERE estado='1'
            """)

        row = cursor.fetchone()
        if row:
            columns = [col[0] for col in cursor.description]
            return dict(zip(columns, row))
        else:
            return 0

def buscar_marca(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM marcas
            WHERE id = %s
        """, [valor])

        columns = [col[0] for col in cursor.description]
        row = cursor.fetchone()
        if row:
            return dict(zip(columns, row))
        return None


 #---------------------------------SERVICIOS-----------------------------------#

def listar_servicios():
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM servicios
            WHERE estado='1'
        """)
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros


def contador_servicios():
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT count(id) as contador
            FROM servicios
            WHERE estado='1'
            """)

        row = cursor.fetchone()
        if row:
            columns = [col[0] for col in cursor.description]
            return dict(zip(columns, row))
        else:
            return 0

def buscar_servicio(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM servicios
            WHERE id = %s
        """, [valor])

        columns = [col[0] for col in cursor.description]
        row = cursor.fetchone()
        if row:
            return dict(zip(columns, row))
        return None


#---------------------------------CLIENTES-----------------------------------#

def listar_clientes():
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM clientes
            WHERE estado='1'
        """)
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros


def contador_clientes():
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT count(id) as contador
            FROM clientes
            WHERE estado='1'
            """)

        row = cursor.fetchone()
        if row:
            columns = [col[0] for col in cursor.description]
            return dict(zip(columns, row))
        else:
            return 0

def buscar_cliente(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM clientes
            WHERE id = %s
        """, [valor])

        columns = [col[0] for col in cursor.description]
        row = cursor.fetchone()
        if row:
            return dict(zip(columns, row))
        return None


#---------------------------------USUARIOS-----------------------------------#

def listado_usuarios():
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM home_usuarios
            WHERE estado='1'
        """)
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros


def buscar_usuario(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM home_usuarios
            WHERE id = %s
        """, [valor])

        columns = [col[0] for col in cursor.description]
        row = cursor.fetchone()
        if row:
            return dict(zip(columns, row))
        return None


#---------------------------------NOTAS-----------------------------------#


def listar_notas():
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT n.*,c.nombre as ncliente
            FROM notas n
            LEFT JOIN clientes c on c.id=n.cliente
            WHERE n.estado='1'
        """)
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros


def buscar_nota(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT n.*,c.nombre as ncliente
            FROM notas n
            LEFT JOIN clientes c on c.id=n.cliente
            WHERE n.id = %s
        """, [valor])

        columns = [col[0] for col in cursor.description]
        row = cursor.fetchone()
        if row:
            return dict(zip(columns, row))
        return None


def buscar_detalle_notas(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM detalle_notas
            WHERE nota=%s
            """,[valor])
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros


#---------------------------------COTIZACION-----------------------------------#

def listar_cotizaciones():
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT c.*,
       (SELECT COUNT(*)
        FROM detalle_cotizaciones cd
        WHERE cd.cotizacion = c.id AND cd.estado = '1') as total_detalles_activos,
               (SELECT COUNT(*)
        FROM cotizaciones c2
        WHERE c2.estado = 1 AND c2.estado <> '0') as total_pendientes,
       (SELECT COUNT(*)
        FROM cotizaciones c3
        WHERE c3.estado = 2 AND c3.estado <> '0') as total_concretados,
        (SELECT COUNT(*)
        FROM cotizaciones c4
        WHERE c4.estado <> '0') as total_contador
        FROM cotizaciones c
        WHERE c.estado <> '0'
        """)
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros




def buscar_cotizacion(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM cotizaciones
            WHERE id = %s
        """, [valor])

        columns = [col[0] for col in cursor.description]
        row = cursor.fetchone()
        if row:
            return dict(zip(columns, row))
        return None

def revisar_cotizaciones(cliente):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT c.*,
       (SELECT COUNT(*)
        FROM detalle_cotizaciones cd
        WHERE cd.cotizacion = c.id AND cd.estado = '1') as total_detalles_activos
        FROM cotizaciones c
        WHERE c.estado <> '0'
        and c.cliente = %s
        """,[cliente])
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros


def buscar_detalle_cotizacion(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM cotizaciones_detalle
            WHERE cotizacion=%s
            """,[valor])
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros



def revisar_detalles_cotizacion(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT d.*,h.nombre
            FROM detalle_cotizaciones d
            LEFT JOIN home_usuarios h on h.id=d.usuario_carga
            WHERE d.cotizacion=%s
            and d.estado=1
            """,[valor])
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros




#---------------------------------RECIBOS-----------------------------------#

def listar_recibos():
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT n.*,c.nombre as ncliente
            FROM recibos n
            LEFT JOIN clientes c on c.id=n.cliente
            WHERE n.estado='1'
        """)
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros


def buscar_recibo(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT n.*,c.nombre as ncliente,c.correo,c.celular
            FROM recibos n
            LEFT JOIN clientes c on c.id=n.cliente
            WHERE n.id = %s
        """, [valor])

        columns = [col[0] for col in cursor.description]
        row = cursor.fetchone()
        if row:
            return dict(zip(columns, row))
        return None




def revisar_pagos(cliente,cotizacion):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT n.*,c.nombre as ncliente,
            c.correo,c.celular
            FROM recibos n
            LEFT JOIN clientes c on c.id=n.cliente
            WHERE n.cliente = %s
            and n.cotizacion = %s
            and n.estado='1'
        """,[cliente,cotizacion])
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros


def buscar_detalle_recibos(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM recibos_detalle
            WHERE recibo=%s
            and estado='1'
            """,[valor])
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros



def buscar_saldo(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            select saldo,fecha
            from recibos
            where estado='1' and cliente=%s
            order by fecha desc limit 1
        """, [valor])

        columns = [col[0] for col in cursor.description]
        row = cursor.fetchone()
        if row:
            return dict(zip(columns, row))
        return None


#---------------------------------PAGOS-----------------------------------#

def listar_pagos():
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM egresos
            WHERE estado='1'
        """)
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros


def buscar_pago(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM egresos
            WHERE id = %s
        """, [valor])

        columns = [col[0] for col in cursor.description]
        row = cursor.fetchone()
        if row:
            return dict(zip(columns, row))
        return None



def revisar_pagos_cotizacion(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT e.*,h.nombre as nombre
            FROM egresos e
            LEFT JOIN home_usuarios h on h.id=e.usuario_carga
            WHERE e.estado='1' and e.cotizacion=%s
        """,[valor])
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros


#---------------------------------CATEGORIAS-----------------------------------#

def listar_categorias():
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM categorias
            WHERE estado='1'
        """)
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros


def buscar_categoria(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM categorias
            WHERE id = %s
        """, [valor])

        columns = [col[0] for col in cursor.description]
        row = cursor.fetchone()
        if row:
            return dict(zip(columns, row))
        return None



#---------------------------------PROVEEDORES-----------------------------------#

def listar_proveedores():
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM proveedor
            WHERE estado='1'
        """)
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros


def buscar_proveedor(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM proveedor
            WHERE id = %s
        """, [valor])

        columns = [col[0] for col in cursor.description]
        row = cursor.fetchone()
        if row:
            return dict(zip(columns, row))
        return None

#---------------------------------PRODUCTOS-----------------------------------#

def listar_productos():
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM productos
            WHERE estado='1'
        """)
        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
    return libros


def buscar_producto(valor):
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM productos
            WHERE id = %s
        """, [valor])

        columns = [col[0] for col in cursor.description]
        row = cursor.fetchone()
        if row:
            return dict(zip(columns, row))
        return None