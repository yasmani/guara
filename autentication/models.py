from django.db import models
from django.db import connections


def listar_marcas():
    print("=== entro al models.py ===")
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM marcas
            WHERE estado='1'
        """)

        columns = [col[0] for col in cursor.description]
        libros = [dict(zip(columns, row)) for row in cursor.fetchall()]
        print(f"   resultado marcas: {libros}")
    return libros


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


def primer_categoria():
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM categorias
            WHERE estado='1' LIMIT 1
        """)
        row = cursor.fetchone()
        if row:
            columns = [col[0] for col in cursor.description]
            return dict(zip(columns, row))
        else:
            return {}

def buscar_categoria(valor):
    valor=int(valor)
    
    with connections['default'].cursor() as cursor:
        cursor.execute("""
            SELECT *
            FROM categorias
            WHERE id=%s
            """,[valor])
        row = cursor.fetchone()
        if row:
            columns = [col[0] for col in cursor.description]
            return dict(zip(columns, row))
        else:
            return {}