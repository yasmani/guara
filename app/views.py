from django import template
from django.templatetags.static import static
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse,FileResponse,Http404
from django.template import loader
from django.urls import reverse
from .utils import session_required
from django.shortcuts import render, redirect
import os
from django.conf import settings
from django.core.files.storage import default_storage
import base64
from .models import  listar_marcas,buscar_marca,listar_servicios,buscar_servicio,listar_clientes,buscar_cliente,listar_notas,buscar_nota,listar_categorias,buscar_categoria,listar_productos,buscar_producto
from .models import buscar_detalle_notas,listado_usuarios,buscar_usuario,listar_recibos,buscar_recibo,buscar_detalle_recibos,listar_cotizaciones,buscar_cotizacion,buscar_detalle_cotizacion,listar_pagos,buscar_pago
from .models import listar_proveedores,buscar_proveedor,revisar_detalles_cotizacion,buscar_saldo,revisar_pagos,revisar_cotizaciones,revisar_pagos_cotizacion
import io
from django.core import signing
import json
from decimal import Decimal
from django.db import connections
from django.contrib import messages
from django.utils.timezone import now
from urllib.parse import quote
from datetime import datetime
from django.db import connection
from datetime import  timedelta







@session_required
def pages(request):

    if request.path.startswith('/configuracion/eliminar_marca/'):
        tarea_id = request.path.split('/')[-1]
        return eliminar_marca(request, tarea_id)

    if request.path.startswith('/configuracion/editar_marca/'):
        tarea_id = request.path.split('/')[-1]
        return editar_marca(request, tarea_id)

    if request.path.startswith('/configuracion/eliminar_servicio/'):
        tarea_id = request.path.split('/')[-1]
        return eliminar_servicio(request, tarea_id)

    if request.path.startswith('/configuracion/editar_servicio/'):
        tarea_id = request.path.split('/')[-1]
        return editar_servicio(request, tarea_id)

    if request.path.startswith('/configuracion/eliminar_cliente/'):
        tarea_id = request.path.split('/')[-1]
        return eliminar_cliente(request, tarea_id)

    if request.path.startswith('/configuracion/editar_cliente/'):
        tarea_id = request.path.split('/')[-1]
        return editar_cliente(request, tarea_id)

    if request.path.startswith('/configuracion/eliminar_usuario/'):
        tarea_id = request.path.split('/')[-1]
        return eliminar_usuario(request, tarea_id)

    if request.path.startswith('/configuracion/editar_usuario/'):
        tarea_id = request.path.split('/')[-1]
        return editar_usuario(request, tarea_id)

    if request.path.startswith('/configuracion/eliminar_nota/'):
        tarea_id = request.path.split('/')[-1]
        return eliminar_nota(request, tarea_id)

    if request.path.startswith('/configuracion/editar_nota/'):
        tarea_id = request.path.split('/')[-1]
        return editar_nota(request, tarea_id)

    if request.path.startswith('/configuracion/ver_nota/'):
        tarea_id = request.path.split('/')[-1]
        return ver_nota(request, tarea_id)


    if request.path.startswith('/configuracion/eliminar_cotizacion/'):
        tarea_id = request.path.split('/')[-1]
        return eliminar_cotizacion(request, tarea_id)

    if request.path.startswith('/configuracion/editar_cotizacion/'):
        tarea_id = request.path.split('/')[-1]
        return editar_cotizacion(request, tarea_id)

    if request.path.startswith('/configuracion/ver_cotizacion/'):
        tarea_id = request.path.split('/')[-1]
        return ver_cotizacion(request, tarea_id)

    if request.path.startswith('/configuracion/eliminar_recibo/'):
        tarea_id = request.path.split('/')[-1]
        return eliminar_recibo(request, tarea_id)

    if request.path.startswith('/configuracion/editar_recibo/'):
        tarea_id = request.path.split('/')[-1]
        return editar_recibo(request, tarea_id)

    if request.path.startswith('/configuracion/revisar_saldo/'):
        tarea_id = request.path.split('/')[-1]
        return revisar_saldo(request, tarea_id)

    if request.path.startswith('/configuracion/revisar_saldo_cotizacion/'):
        tarea_id = request.path.split('/')[-1]
        return revisar_saldo_cotizacion(request, tarea_id)

    if request.path.startswith('/configuracion/ver_recibo/'):
        tarea_id = request.path.split('/')[-1]
        return ver_recibo(request, tarea_id)


    if request.path.startswith('/configuracion/eliminar_pago/'):
        tarea_id = request.path.split('/')[-1]
        return eliminar_pago(request, tarea_id)

    if request.path.startswith('/configuracion/editar_pago/'):
        tarea_id = request.path.split('/')[-1]
        return editar_pago(request, tarea_id)

    if request.path.startswith('/configuracion/ver_pago/'):
        tarea_id = request.path.split('/')[-1]
        return ver_pago(request, tarea_id)

    if request.path.startswith('/configuracion/eliminar_categoria/'):
        tarea_id = request.path.split('/')[-1]
        return eliminar_categoria(request, tarea_id)

    if request.path.startswith('/configuracion/editar_categoria/'):
        tarea_id = request.path.split('/')[-1]
        return editar_categoria(request, tarea_id)

    if request.path.startswith('/configuracion/eliminar_producto/'):
        tarea_id = request.path.split('/')[-1]
        return eliminar_producto(request, tarea_id)

    if request.path.startswith('/configuracion/editar_producto/'):
        tarea_id = request.path.split('/')[-1]
        return editar_producto(request, tarea_id)

    if request.path.startswith('/configuracion/eliminar_proveedor/'):
        tarea_id = request.path.split('/')[-1]
        return eliminar_proveedor(request, tarea_id)

    if request.path.startswith('/configuracion/editar_proveedor/'):
        tarea_id = request.path.split('/')[-1]
        return editar_proveedor(request, tarea_id)


    if request.path.startswith('/configuracion/detalle_cotizacion/'):
        tarea_id = request.path.split('/')[-1]
        return detalle_cotizacion(request, tarea_id)

    if request.path.startswith('/configuracion/mostrar_detalle/'):
        tarea_id = request.path.split('/')[-1]
        return mostrar_detalle(request, tarea_id)

    if request.path.startswith('/configuracion/mostrar_detalle/comentarios_cotizacion/'):
        tarea_id = request.path.split('/')[-1]
        return comentarios_cotizacion(request, tarea_id)

    if request.path.startswith('/configuracion/mostrar_detalle/adjuntos_cotizacion/'):
        tarea_id = request.path.split('/')[-1]
        return adjuntos_cotizacion(request, tarea_id)

    if request.path.startswith('/configuracion/mostrar_detalle/firmar_contrato/'):
        tarea_id = request.path.split('/')[-1]
        return firmar_contrato(request, tarea_id)

    if request.path.startswith('/configuracion/mostrar_detalle/revertir_contrato/'):
        tarea_id = request.path.split('/')[-1]
        return revertir_contrato(request, tarea_id)

    if request.path.startswith('/configuracion/mostrar_detalle/eliminar_adjuntos/'):
        tarea_id = request.path.split('/')[-1]
        return eliminar_adjuntos(request, tarea_id)

    if request.path.startswith('/configuracion/grafico_reporte/'):
        tarea_id = request.path.split('/')[-1]
        return grafico_reporte(request, tarea_id)

    if request.path.startswith('/configuracion/grafico2_reporte/'):
        tarea_id = request.path.split('/')[-1]
        return grafico2_reporte(request, tarea_id)

    context = {}
    try:

        load_template = request.path.split('/')[-1]

        extensiones_permitidas = ['.pdf', '.jpg', '.png', '.docx','.msg']
        _, ext = os.path.splitext(load_template)

        if ext.lower() in extensiones_permitidas:

            file_paths = [
                os.path.join(settings.STATICFILES_DIRS[0], 'adjuntos', load_template),
                os.path.join(settings.STATICFILES_DIRS[0], 'libreria', load_template),
            ]

            # Comprobamos ambas rutas
            for file_path in file_paths:

                if os.path.exists(file_path):
                    return FileResponse(open(file_path, 'rb'), content_type="application/octet-stream")

            # Si no se encuentra en ninguna de las rutas, generamos un error 404
            raise Http404("Archivo no encontrado")

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('inicio'))

        context['segment'] = load_template
        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:
        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))



@session_required
def configuracion(request):
    cargo = request.session.get("cargo", 2)
    clientes = listar_clientes()
    return render(request, "home/index.html",{'clientes': clientes,'cargo':cargo,})


  #---------------------------------MARCAS-----------------------------------#

def lista_marcas(request):
    tareas = listar_marcas()  # Obtener datos
    return JsonResponse({'tareas': tareas})


def registra_marca(request):
    if request.method == "POST":
        tipo = int(request.POST.get("tipom", 0))
        marca_id = int(request.POST.get("marca_id",0))
        brandName = request.POST.get("brandName", "")
        imagen = request.FILES.get("brandLogo", None)
        usuario_registra = request.session.get("dpilogin", "Desconocido")
        fecha = now().strftime("%Y-%m-%d %H:%M:%S")

        adjuntos_portada = None

        if imagen:
            adjuntos_path_portada = os.path.join("biblioteca/marcas", imagen.name)
            full_path = os.path.join(settings.STATICFILES_DIRS[0], adjuntos_path_portada)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "wb+") as destination:
                for chunk in imagen.chunks():
                    destination.write(chunk)
            adjuntos_portada = imagen.name

        try:
            with connections['default'].cursor() as cursor:
                if tipo == 1:
                    cursor.execute("""
                        INSERT INTO marcas
                        (nombre, imagen,estado,fecha_carga, usuario_carga)
                        VALUES (%s, %s, %s, %s, %s)
                        """, [brandName, adjuntos_portada,'1', fecha, usuario_registra])


                else:
                    if tipo == 2 and marca_id:
                        if not adjuntos_portada:
                            cursor.execute("SELECT imagen FROM marcas WHERE id = %s", [marca_id])
                            result = cursor.fetchone()
                            adjuntos_portada = result[0] if result else None

                        # ACTUALIZAR PRODUCTO EXISTENTE
                        cursor.execute("""
                        UPDATE marcas
                        SET nombre=%s, imagen=%s
                        WHERE id=%s
                        """, [brandName, adjuntos_portada,marca_id])
                    else:
                        messages.error(request, "ocurrio un error al modificar")
                        return redirect("configuracion")
            messages.success(request, "Marca guardada correctamente.")
            return redirect("configuracion")
        except Exception as e:
            messages.error(request, f"Ocurrió un error: {e}")
            return redirect("configuracion")

    return HttpResponse("Método no permitido", status=405)


def eliminar_marca(request,valor):

    try:

        with connections['default'].cursor() as cursor:
            cursor.execute("""
                UPDATE marcas
                SET estado='0'
                WHERE id=%s
            """,[valor])
        respuesta="Se realizo con exito"

    except Exception as e:
            return redirect("configuracion")
    return JsonResponse({'respuesta': respuesta})


def editar_marca(request,valor):
    marca= buscar_marca(valor)
    str_html = ""
    if marca:
        if marca['imagen']:
            img_url = static(f"biblioteca/marcas/{marca['imagen']}")
        else:
            img_url = static(f"biblioteca/marcas/nulo.jpg")

        str_html += f'''
                    <input type="hidden" id="tipom" name="tipom" value="2">
                     <input type="hidden" id="marca_id" name="marca_id" value="{marca['id']}">


                    <div class="form-group">
                        <label for="brandName">Nombre de la Marca *</label>
                        <input type="text" id="brandName" name="brandName" class="form-control" required value="{marca['nombre']}">
                    </div>

                    <div class="form-group">
                        <label for="brandLogo">Imagen</label>
                        <input type="file" id="brandLogo" name="brandLogo" class="form-control" accept=".jpg,.jpeg,.png,image/jpeg,image/png">

                    </div>

                    <div class="form-group">
                        <label for="brandLogo">Imagen Actual</label>
                        <img src="{img_url}" alt="Producto"  style="width:25%;heigth:25%;" >

                    </div>'''

    return JsonResponse({'resultado': str_html})




 #---------------------------------SERVICIOS-----------------------------------#


def lista_servicios(request):
    tareas = listar_servicios()  # Obtener datos
    return JsonResponse({'tareas': tareas})


def registra_servicio(request):
    if request.method == "POST":
        tipo = int(request.POST.get("tipos", 0))
        servicio_id = int(request.POST.get("servicio_id",0))
        serviceTitle = request.POST.get("serviceTitle", "")
        serviceDescription = request.POST.get("serviceDescription", "")
        imagen = request.FILES.get("serviceImage", None)
        usuario_registra = request.session.get("dpilogin", "Desconocido")
        fecha = now().strftime("%Y-%m-%d %H:%M:%S")

        adjuntos_portada = None

        if imagen:
            adjuntos_path_portada = os.path.join("biblioteca/servicios", imagen.name)
            full_path = os.path.join(settings.STATICFILES_DIRS[0], adjuntos_path_portada)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "wb+") as destination:
                for chunk in imagen.chunks():
                    destination.write(chunk)
            adjuntos_portada = imagen.name
      
        try:
            with connections['default'].cursor() as cursor:
                if tipo == 1:
                    cursor.execute("""
                        INSERT INTO servicios
                        (titulo,detalle, imagen,estado,fecha_carga, usuario_carga)
                        VALUES (%s, %s,%s, %s, %s, %s)
                        """, [serviceTitle,serviceDescription, adjuntos_portada,'1', fecha, usuario_registra])


                else:
                    if tipo == 2 and servicio_id:
                        if not adjuntos_portada:
                            cursor.execute("SELECT imagen FROM servicios WHERE id = %s", [servicio_id])
                            result = cursor.fetchone()
                            adjuntos_portada = result[0] if result else None

                        # ACTUALIZAR PRODUCTO EXISTENTE
                        cursor.execute("""
                        UPDATE servicios
                        SET titulo=%s,detalle=%s, imagen=%s
                        WHERE id=%s
                        """, [serviceTitle,serviceDescription,adjuntos_portada,servicio_id])
                    else:
                        messages.error(request, "ocurrio un error al modificar")
                        return redirect("configuracion")
            messages.success(request, "Servicio guardado correctamente.")
            return redirect("configuracion")
        except Exception as e:
            messages.error(request, f"Ocurrió un error: {e}")
            return redirect("configuracion")

    return HttpResponse("Método no permitido", status=405)


def eliminar_servicio(request,valor):

    try:

        with connections['default'].cursor() as cursor:
            cursor.execute("""
                UPDATE servicios
                SET estado='0'
                WHERE id=%s
            """,[valor])
        respuesta="Se realizo con exito"

    except Exception as e:
            return redirect("configuracion")
    return JsonResponse({'respuesta': respuesta})


def editar_servicio(request,valor):
    servicio= buscar_servicio(valor)
    str_html = ""
    if servicio:
        if servicio['imagen']:
            img_url = static(f"biblioteca/servicios/{servicio['imagen']}")
        else:
            img_url = static(f"biblioteca/marcas/nulo.jpg")

        str_html += f'''
                    <input type="hidden" id="tipos" name="tipos" value="2">
                     <input type="hidden" id="servicio_id" name="servicio_id" value="{servicio['id']}">


                    <div class="form-group">
                        <label for="brandName">Título del Servicio *</label>
                        <input type="text"  id="serviceTitle" name="serviceTitle"  class="form-control" required value="{servicio['titulo']}">
                    </div>

                        <div class="form-group">
                        <label for="serviceDescription">Descripción *</label>
                        <textarea id="serviceDescription" name="serviceDescription" class="form-control" required>{servicio['detalle']}</textarea>
                    </div>
                    <div class="form-group">
                        <label for="brandLogo">Imagen</label>
                        <input type="file"  id="serviceImage" name="serviceImage" class="form-control" accept=".jpg,.jpeg,.png,image/jpeg,image/png">

                    </div>

                    <div class="form-group">
                        <label for="brandLogo">Imagen Actual</label>
                        <img src="{img_url}" alt="Producto"  style="width:25%;heigth:25%;" >

                    </div>'''

    return JsonResponse({'resultado': str_html})


 #---------------------------------USUARIOS-----------------------------------#

def lista_usuarios(request):
    tareas = listado_usuarios()  # Obtener datos
    return JsonResponse({'tareas': tareas})


def registra_usuarios(request):
    if request.method == "POST":
        tipo = int(request.POST.get("tipousuario", 0))
        usuario_id = int(request.POST.get("usuario_id",0))
        nombre = request.POST.get("nombre", "")
        correo = request.POST.get("correo", "")
        cargo = request.POST.get("cargou", "")
        username = request.POST.get("username", "")
        password = request.POST.get("password", "")
        fecha = now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with connections['default'].cursor() as cursor:
                if tipo == 1:
                    cursor.execute("""
                        INSERT INTO home_usuarios
                        (nombre,correo,username,password,cargo,estado,fecha_creacion)
                        VALUES (%s, %s,%s, %s, %s, %s, %s)
                        """, [nombre,correo,username,password,cargo,1, fecha])


                else:
                    if tipo == 2 and usuario_id:
                        # ACTUALIZAR PRODUCTO EXISTENTE
                        cursor.execute("""
                        UPDATE home_usuarios
                        SET nombre=%s,correo=%s,username=%s, password=%s,
                        cargo=%s
                        WHERE id=%s
                        """, [nombre,correo,username,password,cargo,usuario_id])
                    else:
                        messages.error(request, "ocurrio un error al modificar")
                        return redirect("configuracion")
            messages.success(request, "Usuario guardado correctamente.")
            return redirect("configuracion")
        except Exception as e:
            messages.error(request, f"Ocurrió un error: {e}")
            return redirect("configuracion")

    return HttpResponse("Método no permitido", status=405)


def eliminar_usuario(request,valor):

    try:

        with connections['default'].cursor() as cursor:
            cursor.execute("""
                UPDATE home_usuarios
                SET estado='0'
                WHERE id=%s
            """,[valor])
        respuesta="Se realizo con exito"

    except Exception as e:
            return redirect("configuracion")
    return JsonResponse({'respuesta': respuesta})



def editar_usuario(request,valor):
    usuario= buscar_usuario(valor)
    str_html = ""
    if usuario:
        str_html += f'''
                    <input type="hidden" id="tipousuario" name="tipousuario" value="2">
                     <input type="hidden" id="usuario_id" name="usuario_id" value="{usuario['id']}">


                    <div class="form-group">
                        <label for="serviceTitle">Nombre del Usuario *</label>
                        <input type="text" id="nombre" name="nombre" class="form-control" required value="{usuario['nombre']}">
                    </div>

                     <div class="form-group">
                        <label for="serviceTitle">correo</label>
                        <input type="email" id="correo" name="correo" class="form-control" value="{usuario['correo']}">
                    </div>


                    <div class="form-group">
                        <label for="serviceDescription">Username *</label>
                        <input type="text" id="username" name="username" class="form-control" required value="{usuario['username']}">
                    </div>

                     <div class="form-group">
                        <label for="serviceTitle">Contraseña *</label>
                        <input type="password" id="password" name="password" class="form-control" required value="{usuario['password']}">
                    </div>
                    '''
        seleccionado=""
        seleccionado2=""
        if usuario['cargo'] == '1':
            seleccionado="selected"
        else:
            seleccionado2="selected"
        str_html += f'''<div class="form-group">
                        <label for="serviceTitle">Cargo *</label>
                        <select id="cargou" name="cargou" class="form-control" required>
                        <option value="1" {seleccionado}>Administrador</option>
                        <option value="2" {seleccionado2}>Trabajador</option>
                        </select>
                    </div>'''

    return JsonResponse({'resultado': str_html})



#---------------------------------CLIENTES-----------------------------------#


def lista_clientes(request):
    tareas = listar_clientes()  # Obtener datos
    return JsonResponse({'tareas': tareas})


def registra_cliente(request):
    if request.method == "POST":
        tipo = int(request.POST.get("tipocliente", 0))
        cliente_id = int(request.POST.get("cliente_id",0))
        nombre = request.POST.get("nombrec", "")
        titular = request.POST.get("titularc", "")
        detallecliente = request.POST.get("detallecliente", "")
        correo = request.POST.get("correoC", "")
        celular = request.POST.get("celular", "")
        usuario_registra = request.session.get("dpilogin", "Desconocido")
        fecha = now().strftime("%Y-%m-%d %H:%M:%S")
        try:
            with connections['default'].cursor() as cursor:
                if tipo == 1:
                    cursor.execute("""
                        INSERT INTO clientes
                        (nombre,titular,detalle, correo,celular,estado,fecha_carga, usuario_carga)
                        VALUES (%s, %s,%s, %s, %s, %s,%s,%s)
                        """, [nombre,titular,detallecliente, correo,celular,1, fecha, usuario_registra])


                else:
                    if tipo == 2 and cliente_id:
                        # ACTUALIZAR PRODUCTO EXISTENTE
                        cursor.execute("""
                        UPDATE clientes
                        SET nombre=%s,titular=%s,detalle=%s, correo=%s, celular=%s
                        WHERE id=%s
                        """, [nombre,titular,detallecliente,correo,celular,cliente_id])
                    else:
                        messages.error(request, "ocurrio un error al modificar")
                        return redirect("configuracion")
            messages.success(request, "Cliente guardado correctamente.")
            return redirect("configuracion")
        except Exception as e:
            messages.error(request, f"Ocurrió un error: {e}")
            return redirect("configuracion")

    return HttpResponse("Método no permitido", status=405)


def eliminar_cliente(request,valor):

    try:

        with connections['default'].cursor() as cursor:
            cursor.execute("""
                UPDATE clientes
                SET estado='0'
                WHERE id=%s
            """,[valor])
        respuesta="Se realizo con exito"

    except Exception as e:
            return redirect("configuracion")
    return JsonResponse({'respuesta': respuesta})



def editar_cliente(request,valor):
    cliente= buscar_cliente(valor)
    str_html = ""
    if cliente:
        str_html += f'''
                    <input type="hidden" id="tipocliente" name="tipocliente" value="2">
                     <input type="hidden" id="cliente_id" name="cliente_id" value="{cliente['id']}">

                        <div class="form-group">
                        <label for="serviceTitle">Nombre del Cliente *</label>
                        <input type="text" id="nombre" name="nombre" class="form-control" value="{cliente['nombre']}" required>
                    </div>

                     <div class="form-group">
                        <label for="serviceTitle">Titular *</label>
                        <input type="text" id="titular" name="titular" class="form-control" value="{cliente['titular']}" required>
                    </div>


                    <div class="form-group">
                        <label for="serviceDescription">Descripción *</label>
                        <textarea id="detallecliente" name="detallecliente" class="form-control" required>{cliente['detalle']}</textarea>
                    </div>

                     <div class="form-group">
                        <label for="serviceTitle">Correo *</label>
                        <input type="mail" id="correo" name="correo" class="form-control" required value="{cliente['correo']}">
                    </div>

                     <div class="form-group">
                        <label for="serviceTitle">Celular </label>
                        <input type="phone" id="celular" name="celular" class="form-control" value="{cliente['celular']}">
                    </div>'''

    return JsonResponse({'resultado': str_html})




#---------------------------------NOTAS-----------------------------------#


def lista_notas(request):
    tareas = listar_notas()  # Obtener datos
    return JsonResponse({'tareas': tareas})


def registra_nota(request):
    if request.method == "POST":
        tipo = int(request.POST.get("tiponota", 0))
        nota_id = int(request.POST.get("nota_id",0))
        cliente = request.POST.get("cliente", "")
        fecha = request.POST.get("fechan", "")
        usuario_registra = request.session.get("dpilogin", "Desconocido")
        fecha_registra = now().strftime("%Y-%m-%d %H:%M:%S")
        detalles = request.POST.getlist('detalle[]')
        cantidades = request.POST.getlist('cantidad[]')
        precios = request.POST.getlist('precio[]')
        tallas = request.POST.getlist('talla[]')
        try:
            with connections['default'].cursor() as cursor:
                if tipo == 1:
                    cursor.execute("""
                        INSERT INTO notas
                        (cliente,fecha,estado,fecha_carga, usuario_carga)
                        VALUES (%s, %s,%s, %s, %s)
                        """, [cliente,fecha,1, fecha_registra, usuario_registra])

                     # OBTENER EL ÚLTIMO ID INSERTADO
                    ultimo_id = cursor.lastrowid
                    cantidad_contador=0
                    precio_total = 0
                    tallas_lista = ''
                    detalle_lista = ''
                    for detalle_,talla_,cantidad_,precio_ in zip(detalles, tallas, cantidades,precios):
                        try:
                            cantidad_val = float(cantidad_) if cantidad_ else 0
                            precio_val = float(precio_) if precio_ else 0
                            cantidad_contador = cantidad_contador + cantidad_val
                            precio_total = precio_total + (cantidad_val*precio_val)
                            tallas_lista = talla_ + ',' + tallas_lista
                            detalle_lista = detalle_ + ',' + detalle_lista
                            cursor.execute("""
                            INSERT INTO detalle_notas
                            (nota,cliente,fecha,detalle,talla,cantidad,precio,estado,fecha_carga, usuario_carga)
                            VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s)
                            """, [ultimo_id,cliente,fecha,detalle_,talla_,cantidad_val,precio_val,1,fecha_registra,usuario_registra])
                        except Exception as e:
                            messages.warning(request, f"Error al insertar el detalle: {str(e)}")

                    cursor.execute("""
                                UPDATE notas
                                SET cantidad = %s,
                                precio = %s,
                                talla = %s,
                                detalle=%s
                                WHERE id = %s
                                """, [cantidad_contador,precio_total,tallas_lista,detalle_lista, ultimo_id])
                else:
                    if tipo == 2 and nota_id:
                        cursor.execute("""
                            UPDATE notas
                            SET cliente = %s,
                            fecha = %s
                            WHERE id = %s
                            """, [cliente,fecha,nota_id])

                        cursor.execute("""
                                DELETE FROM detalle_notas
                                WHERE nota=%s
                            """, [nota_id])
                        cantidad_contador=0
                        precio_total = 0
                        tallas_lista = ''
                        detalle_lista = ''

                        for detalle_,talla_,cantidad_,precio_ in zip(detalles, tallas, cantidades,precios):
                            try:
                                cantidad_val = float(cantidad_) if cantidad_ else 0
                                precio_val = float(precio_) if precio_ else 0
                                cantidad_contador = cantidad_contador + cantidad_val
                                precio_total = precio_total + (cantidad_val*precio_val)
                                tallas_lista = talla_ + ',' + tallas_lista
                                detalle_lista = detalle_ + ',' + detalle_lista
                                cursor.execute("""
                                INSERT INTO detalle_notas
                                (nota,cliente,fecha,detalle,talla,cantidad,precio,estado,fecha_carga, usuario_carga)
                                VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s,%s)
                                """, [nota_id,cliente,fecha,detalle_,talla_,cantidad_val,precio_val,1,fecha_registra,usuario_registra])
                            except Exception as e:
                                messages.warning(request, f"Error al insertar el detalle: {str(e)}")

                        cursor.execute("""
                                    UPDATE notas
                                    SET cantidad = %s,
                                    precio = %s,
                                    talla = %s,
                                    detalle=%s
                                    WHERE id = %s
                                    """, [cantidad_contador,precio_total,tallas_lista,detalle_lista, nota_id])

            messages.success(request, "Nota guardada correctamente.")
            return redirect("configuracion")
        except Exception as e:
            messages.error(request, f"Ocurrió un error: {e}")
            return redirect("configuracion")

    return HttpResponse("Método no permitido", status=405)


def eliminar_nota(request,valor):

    try:

        with connections['default'].cursor() as cursor:
            cursor.execute("""
                UPDATE notas
                SET estado='0'
                WHERE id=%s
            """,[valor])
        respuesta="Se realizo con exito"

    except Exception as e:
            return redirect("configuracion")
    return JsonResponse({'respuesta': respuesta})


def editar_nota(request,valor):
    nota= buscar_nota(valor)
    clientes = listar_clientes()
    str_html = ""
    if nota:
        str_html += f'''
                    <input type="hidden" id="tiponota" name="tiponota" value="2">
                     <input type="hidden" id="nota_id" name="nota_id" value="{nota['id']}">
                         <div class="form-group">
                        <label for="serviceTitle">Cliente *</label>
                        <select id="cliente" name="cliente" class="form-control" required>'''
        for cliente in clientes:
            if cliente['id'] == nota['cliente']:
                str_html += f'''<option value="{cliente['id']}" selected>{cliente['nombre']}</option>'''
            else:
                str_html += f'''<option value="{cliente['id']}">{cliente['nombre']}</option>'''

        str_html += f'''</select>
                    </div>

                     <div class="form-group">
                        <label for="serviceTitle">Fecha *</label>
                        <input type="date" id="fechan" name="fechan" class="form-control" required value="{nota['fecha']}">
                    </div>

                     <div class="table-responsive">
                    <table id="tabla-registro" class="table table-bordered">
                                <thead>
                                    <tr>
                                            <td width="4%" height="31">#</td>
                                            <td width="65%">ITEM</td>
                                            <td>TALLA</td>
                                            <td>CANTIDAD</td>
                                            <td>MONTO</td>
                                            <td width="5%">ANULAR</td>
                                    </tr>
                                </thead>
                                <tbody id="tbody-registro" >'''
        valor = nota['id']
        listados =buscar_detalle_notas(valor)
        total=0
        total_precio=0
        if listados:
            contador=0
            for listado in listados:
                contador=contador + 1
                total_item=0
                total_item = float(listado['cantidad']) if listado['cantidad'] else 0
                precio_item=0
                precio_item = float(listado['precio']) if listado['precio'] else 0
                total = total + total_item
                total_precio = total_precio + (total_item*precio_item)
                str_html += f''' <tr>
                                <td width="4%" align="center">{contador}</td>
                                <td width="65%">
                                    <input type="text" class="form-control detalle" name="detalle[]" value="{listado['detalle']}">
                                </td>
                                <td><input type="text" class="form-control talla" name="talla[]" value="{listado['talla']}"></td>
                                <td><input type="text" class="form-control cantidad" name="cantidad[]" value="{listado['cantidad']}"></td>
                                <td><input type="text" class="form-control precio" name="precio[]" value="{listado['precio']}"></td>
                                <td align="center">
                                    <button type="button" class="btn btn-danger btn-eliminarFila btn-sm">
                                        <span class="fa fa-times"></span>
                                    </button>
                                </td>
                            </tr>'''


        str_html += f'''    </tbody>
                                <tfoot class="table-active text-right" >
                                  <tr>
                                        <td align="center"> <button type="button" class="btn btn-sm" id="btn-addFila"> <span class="fa fa-plus"></span> </button></td>
                                        <td colspan="2">Totales</td>
                                        <td><input type="text" class="form-control-plaintext text-right" id="total_general" name="total_general"  value="{float(total):.2f}" disabled></td>
                                        <td><input type="text" class="form-control-plaintext text-right" id="total_precio" name="total_precio"  value="{float(total_precio):.2f}" disabled></td>
                                        <td>&nbsp;</td>

                                  </tr>

                              </tfoot>
                            </table>
                             </div>
                     '''

    return JsonResponse({'resultado': str_html})





def ver_nota(request, valor):
    nota = buscar_nota(valor)
    if not nota:
        return HttpResponse("No se encontró", status=404)

    # Formatear fecha en español
    fecha_str = formatear_fecha_espanol(nota['fecha'])
    img_url = static(f"biblioteca/logo/IMG-20251216-WA0012.ico")
    img_logo = static(f"biblioteca/logo/IMG-20251216-WA0012.jpg")

    str_html = f'''
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guara - Nota de Venta</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
        <link rel="icon" href="{img_url}">
    <style>
        /* Estilos para impresión */
        @page {{
            size: A4;
            margin: 2cm;
        }}

        @media print {{
            body {{
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }}

            .no-print {{
                display: none;
            }}

            .print-btn {{
                display: none;
            }}
        }}

        /* Estilos generales */
        body {{
            font-family: "Arial", sans-serif;
            margin: 0;
            padding: 0;
            color: #000;
            background-color: #fff;
            line-height: 1.4;
        }}

        .container {{
            max-width: 21cm;
            margin: 0 auto;
            padding: 0;
            position: relative;
        }}

        /* Encabezado */
        .header {{
            text-align: left;
            margin-bottom: 30px;
            padding-bottom: 15px;

        }}

        .company-name {{
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 8px;
            letter-spacing: 1px;
        }}

        .company-info {{
            font-size: 14px;
            line-height: 1.6;
        }}

        /* Fecha */
        .fecha {{
            text-align: right;
            margin: 25px 0;
            font-size: 14px;
            font-weight: bold;
        }}

        .fecha-label {{
            color: #000;
        }}

        /* Destinatario */
        .destinatario {{
            margin: 25px 0 40px 0;
            font-size: 14px;
            font-weight: bold;
        }}

        .destinatario-label {{
            color: #000;
        }}

        /* Título principal */
        .titulo-principal {{
            text-align: center;
            margin: 40px 0;
            font-size: 28px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        /* Tabla */
        .tabla-contenedor {{
            margin: 30px 0 50px 0;
            width: 100%;
        }}

        .tabla-productos {{
            width: 100%;
            border-collapse: collapse;
            border: 2px solid #333;
        }}

        .tabla-productos th {{
            background-color: #f0f0f0;
            border: 2px solid #333;
            padding: 12px 8px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
        }}

        .tabla-productos td {{
            border: 1px solid #333;
            padding: 10px 8px;
            text-align: center;
            font-size: 13px;
        }}

        .tabla-productos .col-detalle {{
            text-align: center;
            width: 70%;
            background-color: #918787;
            color:#FFFFFF;
        }}

        .tabla-productos .col-detalle2 {{
            text-align: left;
            width: 70%;
            background-color: #FFFFFF;
            color:#292626;
        }}
        .tabla-productos .col-talla {{
            width: 15%;
            background-color: #918787;
            color:#FFFFFF;
        }}

        .tabla-productos .col-talla2 {{
            width: 15%;
            background-color: #FFFFFF;
            color:#292626;
        }}
        .tabla-productos .col-cantidad {{
            width: 15%;
            background-color: #918787;
            color:#FFFFFF;
        }}

        .tabla-productos .col-cantidad2 {{
            width: 15%;
            background-color: #FFFFFF;
            color:#292626;
        }}
        /* Firmas */
        .firmas {{
            margin-top: 100px;
            padding-top: 30px;
            border-top: 1px solid #333;
        }}

        .firma-container {{
            display: flex;
            justify-content: space-between;
        }}

        .firma-col {{
            width: 45%;
        }}

        .firma-linea {{
            width: 100%;
            border-top: 1px solid #333;
            margin: 60px 0 5px 0;
        }}

        .firma-texto {{
            font-size: 12px;
            font-weight: bold;
            margin-bottom: 5px;
        }}

        .firma-nombre {{
            font-size: 11px;
            text-align: center;
            margin-top: 8px;
        }}

        /* Botón de impresión */
        .print-btn {{
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 12px 24px;
            background: #2c3e50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-family: Arial, sans-serif;
            font-size: 14px;
            z-index: 1000;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }}

        .print-btn:hover {{
            background: #1a252f;
        }}

        /* Marca de agua */
        .watermark {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(-45deg);
            font-size: 60px;
            color: rgba(0,0,0,0.1);
            z-index: -1;
            white-space: nowrap;
            pointer-events: none;
        }}
    </style>
</head>
<body>
    <!-- Botón para imprimir -->
    <button class="print-btn no-print" onclick="window.print()">
        🖨️ Imprimir / Guardar como PDF
    </button>

    <!-- Marca de agua -->
    <div class="watermark no-print">COPIA ORIGINAL</div>

    <div class="container">
        <!-- Encabezado con información de la empresa -->
        <div class="header">
            <div class="company-name">
             <img width="120" height="90" src="{img_logo}">
             </div>
            <div class="company-info">
                Cels. 79949364 - 65070403<br>
                Av. Canal lsuto C/ Landivar Edif. Los Cedros<br>
                Santa Cruz - Bolivia
            </div>
        </div>

        <!-- Fecha (derecha) -->
        <div class="fecha">
            <span class="fecha-label">FECHA:</span>
            <span id="fecha-actual">{fecha_str}</span>
        </div>

        <!-- Destinatario -->
        <div class="destinatario">
            <span class="destinatario-label">SEÑORES:</span>
            {nota['ncliente']}
        </div>

        <!-- Título principal -->
        <div class="titulo-principal">
            Nota de Venta
        </div>

        <!-- Tabla de productos -->
        <div class="tabla-contenedor">
            <table class="tabla-productos">
                <thead>
                    <tr>
                        <th class="col-detalle">DETALLE</th>
                        <th class="col-talla">TALLA</th>
                        <th class="col-cantidad">CANTIDAD</th>
                        <th class="col-cantidad">PRECIO</th>
                        <th class="col-cantidad">SUBTOTAL</th>
                    </tr>
                </thead>
                <tbody>
            '''

    detalles = buscar_detalle_notas(valor)
    total=0
    total_precio=0
    for detalle in detalles:
        total_precio = total_precio + (float(detalle['cantidad'])*float(detalle['precio']))
        subtotal = float(detalle['cantidad'])*float(detalle['precio'])
        total=total + float(detalle['cantidad'])
        str_html += f'''
                <tr>
                 <td class="col-detalle2">{detalle['detalle']}</td>
                 <td class="col-talla2">{detalle['talla']}</td>
                 <td class="col-cantidad2">{detalle['cantidad']}</td>
                 <td class="col-cantidad2">{detalle['precio']}</td>
                 <td class="col-cantidad2">{subtotal}</td>
             </tr>     '''


    str_html += f'''            <!-- Fila de total -->
                    <tr style="background-color: #f8f9fa; font-weight: bold;">
                        <td class="col-detalle2" style="text-align: right;">TOTAL</td>
                        <td class="col-talla2">-</td>
                        <td class="col-cantidad2">{total}</td>
                        <td class="col-cantidad2">-</td>
                        <td class="col-cantidad2">{total_precio}</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Firmas -->
        <div class="firmas">
            <div class="firma-container">
                <div class="firma-col">
                    <div class="firma-texto">ENTREGADO POR:</div>
                    <div class="firma-linea"></div>
                    <div class="firma-nombre">
                        Nombre y Firma
                    </div>
                    <div class="firma-nombre" style="font-size: 10px; margin-top: 5px;">
                        Fecha: __/__/____
                    </div>
                </div>

                <div class="firma-col">
                    <div class="firma-texto">RECIBIDO POR:</div>
                    <div class="firma-linea"></div>
                    <div class="firma-nombre">
                        Nombre y Firma del Cliente
                    </div>
                    <div class="firma-nombre" style="font-size: 10px; margin-top: 5px;">
                        Fecha: __/__/____
                    </div>
                </div>
            </div>
        </div>

        <!-- Pie de página -->
        <div style="text-align: center; font-size: 9px; color: #666; margin-top: 50px; padding-top: 10px; border-top: 1px solid #ccc;">
            Documento generado electrónicamente por Guara<br>
            Código: {valor} |
            Versión: 1.0
        </div>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function() {{
            // Auto-llenar fecha actual si no hay datos
            // Configurar para impresión
            window.onbeforeprint = function() {{
                // Ocultar elementos no deseados al imprimir
                document.querySelectorAll(".no-print").forEach(el => {{
                    el.style.display = "none";
                }});
            }};

            window.onafterprint = function() {{
                // Restaurar elementos después de imprimir
                document.querySelectorAll(".no-print").forEach(el => {{
                    el.style.display = "";
                }});
            }};
        }});


    </script>
</body>
</html>
'''

    return HttpResponse(str_html)




#---------------------------------COTIZACION-----------------------------------#


def lista_cotizaciones(request):
    tareas = listar_cotizaciones()  # Obtener datos
    return JsonResponse({'tareas': tareas})


import uuid
def registra_cotizacion(request):
    if request.method == "POST":
        tipo = int(request.POST.get("tipo", 0))
        cotizacion_id = int(request.POST.get("cotizacion_id", 0))
        prospecto = request.POST.get("prospecto", "")
        entrega = request.POST.get("entrega", "")
        forma = request.POST.get("forma", "")
        validez = request.POST.get("validez", "")
        fecha = request.POST.get("fecha", "")
        usuario_registra = request.session.get("dpilogin", "Desconocido")
        fecha_registra = now().strftime("%Y-%m-%d %H:%M:%S")
        detallec = request.POST.getlist('detallec[]')
        cantidadc = request.POST.getlist('cantidadc[]')
        preciou = request.POST.getlist('preciou[]')
        total_iten = request.POST.getlist('total_iten[]')
        respaldos = request.FILES.getlist('respaldo[]')
        detalles_existentes_ids = request.POST.getlist('detalle_id[]')  # IDs de detalles existentes

        try:
            with connections['default'].cursor() as cursor:
                if tipo == 1:  # NUEVO REGISTRO
                    cursor.execute("""
                        INSERT INTO cotizaciones
                        (prospecto, fecha, entrega, forma, validez, estado, fecha_carga, usuario_carga)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """, [prospecto, fecha, entrega, forma, validez, 1, fecha_registra, usuario_registra])

                    ultimo_id = cursor.lastrowid
                    cantidad_contador = 0
                    precio_total = 0
                    detalle_lista = ''

                    for i, (detalle_, cantidad_, precio_, total_iten_) in enumerate(zip(detallec, cantidadc, preciou, total_iten)):
                        try:
                            cantidad_val = float(cantidad_) if cantidad_ else 0
                            precio_val = float(precio_) if precio_ else 0
                            total_iten_val = float(total_iten_) if total_iten_ else 0
                            cantidad_contador = cantidad_contador + cantidad_val
                            precio_total = precio_total + total_iten_val
                            detalle_lista = detalle_ + ',' + detalle_lista

                            adjuntos_portada = None

                            if i < len(respaldos) and respaldos[i]:
                                archivo = respaldos[i]
                                if archivo.name:
                                    nombre_original = archivo.name
                                    nombre_base, extension = os.path.splitext(nombre_original)
                                    nombre_unico = f"{nombre_base}_{uuid.uuid4().hex[:8]}{extension}"
                                    adjuntos_path_portada = os.path.join("biblioteca/cotizaciones32/", nombre_unico)
                                    full_path = os.path.join(settings.STATICFILES_DIRS[0], adjuntos_path_portada)
                                    os.makedirs(os.path.dirname(full_path), exist_ok=True)
                                    with open(full_path, "wb+") as destination:
                                        for chunk in archivo.chunks():
                                            destination.write(chunk)
                                    adjuntos_portada = nombre_unico

                            cursor.execute("""
                                INSERT INTO cotizaciones_detalle
                                (cotizacion, prospecto, fecha, detalle, cantidad, precio, total, imagen, estado, fecha_carga, usuario_carga)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                """, [ultimo_id, prospecto, fecha, detalle_, cantidad_val, precio_val, total_iten_val, adjuntos_portada, 1, fecha_registra, usuario_registra])

                        except Exception as e:
                            messages.warning(request, f"Error al insertar el detalle {i+1}: {str(e)}")

                    cursor.execute("""
                        UPDATE cotizaciones
                        SET cantidad = %s,
                            monto = %s,
                            detalle = %s
                        WHERE id = %s
                        """, [cantidad_contador, precio_total, detalle_lista, ultimo_id])


                elif tipo == 2 and cotizacion_id:  # EDICIÓN
                    # Primero actualizar la cabecera
                    cursor.execute("""
                        UPDATE cotizaciones
                        SET prospecto = %s,
                            fecha = %s,
                            entrega = %s,
                            forma = %s,
                            validez = %s
                        WHERE id = %s
                        """, [prospecto, fecha, entrega, forma, validez, cotizacion_id])

                    cantidad_contador = 0
                    precio_total = 0
                    detalle_lista = ''

                    # --- AQUÍ VA EL CÓDIGO PARA PROCESAR ARCHIVOS ---
                    archivos_por_detalle = {}
                    for key, file in request.FILES.items():
                        if key.startswith('respaldo_'):
                            try:
                                # Extraer el ID del nombre: respaldo_123[]
                                detalle_id_str = key.replace('respaldo_', '').replace('[]', '')
                                if detalle_id_str.isdigit():
                                    detalle_id = int(detalle_id_str)
                                    archivos_por_detalle[detalle_id] = file
                            except Exception as e:
                                print(f"Error procesando archivo {key}: {e}")
                    # --- FIN DEL PROCESAMIENTO DE ARCHIVOS ---

                    # CONTADOR PARA ARCHIVOS DE NUEVOS DETALLES (name="respaldo[]")
                    archivos_nuevos_index = 0

                    # Procesar cada detalle
                    for i in range(len(detallec)):
                        try:
                            detalle_ = detallec[i] if i < len(detallec) else ""
                            cantidad_ = cantidadc[i] if i < len(cantidadc) else "0"
                            precio_ = preciou[i] if i < len(preciou) else "0"
                            total_iten_ = total_iten[i] if i < len(total_iten) else "0"

                            cantidad_val = float(cantidad_) if cantidad_ else 0
                            precio_val = float(precio_) if precio_ else 0
                            total_iten_val = float(total_iten_) if total_iten_ else 0
                            cantidad_contador = cantidad_contador + cantidad_val
                            precio_total = precio_total + total_iten_val
                            detalle_lista = detalle_ + ',' + detalle_lista

                            # Verificar si es un detalle existente (tiene ID) o nuevo
                            if i < len(detalles_existentes_ids) and detalles_existentes_ids[i]:
                                detalle_id = int(detalles_existentes_ids[i])

                                # Obtener la imagen actual del detalle existente
                                cursor.execute("""
                                    SELECT imagen FROM cotizaciones_detalle
                                    WHERE id = %s AND cotizacion = %s
                                """, [detalle_id, cotizacion_id])
                                resultado = cursor.fetchone()
                                imagen_actual = resultado[0] if resultado else None

                                # Verificar si hay un archivo para este ID específico
                                if detalle_id in archivos_por_detalle:
                                    archivo = archivos_por_detalle[detalle_id]
                                    if archivo and archivo.name:
                                        # Eliminar archivo anterior si existe
                                        if imagen_actual:
                                            try:
                                                old_path = os.path.join(settings.STATICFILES_DIRS[0], "biblioteca/cotizaciones32/", imagen_actual)
                                                if os.path.exists(old_path):
                                                    os.remove(old_path)
                                            except Exception as e:
                                                print(f"Error al eliminar archivo anterior: {e}")

                                        # Guardar nuevo archivo
                                        nombre_original = archivo.name
                                        nombre_base, extension = os.path.splitext(nombre_original)
                                        nombre_unico = f"{nombre_base}_{uuid.uuid4().hex[:8]}{extension}"
                                        adjuntos_path_portada = os.path.join("biblioteca/cotizaciones32/", nombre_unico)
                                        full_path = os.path.join(settings.STATICFILES_DIRS[0], adjuntos_path_portada)
                                        os.makedirs(os.path.dirname(full_path), exist_ok=True)

                                        with open(full_path, "wb+") as destination:
                                            for chunk in archivo.chunks():
                                                destination.write(chunk)

                                        imagen_actual = nombre_unico

                                # Actualizar el detalle existente
                                cursor.execute("""
                                    UPDATE cotizaciones_detalle
                                    SET detalle = %s,
                                        cantidad = %s,
                                        precio = %s,
                                        total = %s,
                                        imagen = %s,
                                        fecha_carga = %s,
                                        usuario_carga = %s
                                    WHERE id = %s AND cotizacion = %s
                                """, [detalle_, cantidad_val, precio_val, total_iten_val,
                                      imagen_actual, fecha_registra, usuario_registra,
                                      detalle_id, cotizacion_id])
                            else:
                                # Es un nuevo detalle - procesar archivos normales (respaldo[])
                                adjuntos_portada = None

                                # CAMBIO CLAVE: Procesar archivos de nuevas filas con contador separado
                                # Verificar si hay archivos disponibles para nuevos detalles
                                if archivos_nuevos_index < len(respaldos):
                                    archivo = respaldos[archivos_nuevos_index]
                                    # Verificar si este archivo pertenece a esta fila nueva
                                    # (los archivos de nuevos detalles vienen en orden)
                                    if archivo and archivo.name:
                                        nombre_original = archivo.name
                                        nombre_base, extension = os.path.splitext(nombre_original)
                                        nombre_unico = f"{nombre_base}_{uuid.uuid4().hex[:8]}{extension}"
                                        adjuntos_path_portada = os.path.join("biblioteca/cotizaciones32/", nombre_unico)
                                        full_path = os.path.join(settings.STATICFILES_DIRS[0], adjuntos_path_portada)
                                        os.makedirs(os.path.dirname(full_path), exist_ok=True)

                                        with open(full_path, "wb+") as destination:
                                            for chunk in archivo.chunks():
                                                destination.write(chunk)

                                        adjuntos_portada = nombre_unico
                                        archivos_nuevos_index += 1
                                # Si no hay archivo para esta nueva fila, adjuntos_portada queda como None

                                # Insertar nuevo detalle
                                cursor.execute("""
                                    INSERT INTO cotizaciones_detalle
                                    (cotizacion, prospecto, fecha, detalle, cantidad, precio, total, imagen, estado, fecha_carga, usuario_carga)
                                    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
                                """, [cotizacion_id, prospecto, fecha, detalle_, cantidad_val,
                                      precio_val, total_iten_val, adjuntos_portada, 1,
                                      fecha_registra, usuario_registra])

                        except Exception as e:
                            messages.warning(request, f"Error al procesar el detalle {i+1}: {str(e)}")

                    # Actualizar totales en la cabecera
                    cursor.execute("""
                        UPDATE cotizaciones
                        SET cantidad = %s,
                            monto = %s,
                            detalle = %s
                        WHERE id = %s
                    """, [cantidad_contador, precio_total, detalle_lista, cotizacion_id])

                else:
                    messages.error(request, "Tipo de operación no válido")
                    return redirect("configuracion")

            messages.success(request, "Cotización guardada correctamente.")
            return redirect("configuracion")

        except Exception as e:
            messages.error(request, f"Ocurrió un error: {str(e)}")
            import traceback
            print(traceback.format_exc())
            return redirect("configuracion")

    return HttpResponse("Método no permitido", status=405)


def eliminar_cotizacion(request,valor):

    try:

        with connections['default'].cursor() as cursor:
            cursor.execute("""
                UPDATE cotizaciones
                SET estado='0'
                WHERE id=%s
            """,[valor])
        respuesta="Se realizo con exito"

    except Exception as e:
            return redirect("configuracion")
    return JsonResponse({'respuesta': respuesta})

def editar_cotizacion(request, valor):
    cotizacion = buscar_cotizacion(valor)
    detalles = buscar_detalle_cotizacion(valor)
    str_html = ""

    if cotizacion:
        str_html += f'''
            <input type="hidden" id="tipo" name="tipo" value="2">
            <input type="hidden" id="cotizacion_id" name="cotizacion_id" value="{cotizacion['id']}">

            <!-- Fecha (derecha) -->
            <div class="fecha">
                <span class="fecha-label">FECHA:</span>
                <span id="fecha-actual">
                    <input type="date" id="fecha" name="fecha" class="form-control" required style="width:30%;" value="{cotizacion['fecha']}">
                </span>
            </div>

            <!-- Destinatario -->
            <div class="destinatario">
                <span class="destinatario-label">SEÑORES:</span>
                <input type="text" id="prospecto" name="prospecto" class="form-control" style="width:50%;" value="{cotizacion['prospecto']}" required>
            </div>

            <!-- Título principal -->
            <div class="titulo-principal">
                COTIZACIÓN
            </div>

            <!-- Tabla de productos -->
            <div class="table-container">
                <table class="tabla-productos">
                    <thead>
                        <tr>
                            <th class="col-talla">CANT</th>
                            <th class="col-detalle">DETALLE</th>
                            <th class="col-cantidad">PRECIO UNI BS.</th>
                            <th class="col-cantidad">TOTAL</th>
                            <th class="col-diseno">DISEÑO</th>
                            <td class="col-anular">ANULAR</td>
                        </tr>
                    </thead>
                    <tbody id="body_cotizaciones">'''

        total_unitario = 0
        total_precio = 0
        contador_filas = 0

        if detalles:
            for detalle in detalles:
                total_item = float(detalle['cantidad']) if detalle['cantidad'] else 0
                precio_item = float(detalle['precio']) if detalle['precio'] else 0
                total_unitario = total_unitario + precio_item
                total_precio = total_precio + (total_item * precio_item)

                if detalle['imagen']:
                    img_url = static(f"biblioteca/cotizaciones32/{detalle['imagen']}")
                else:
                    img_url = static(f"biblioteca/marcas/nulo.jpg")

                # CAMBIO IMPORTANTE: Agregar campo hidden con el ID del detalle
                str_html += f'''
                    <tr>
                        <td class="col-talla2">
                            <input type="hidden" name="detalle_id[]" value="{detalle['id']}">
                            <input type="text" class="form-control cantidadc" name="cantidadc[]" value="{detalle['cantidad']}">
                        </td>
                        <td class="col-detalle2">
                            <textarea class="form-control detallec" name="detallec[]">{detalle['detalle']}</textarea>
                        </td>
                        <td class="col-cantidad2">
                            <input type="text" class="form-control preciou" name="preciou[]" value="{detalle['precio']}">
                        </td>
                        <td class="col-cantidad2">
                            <input type="text" class="form-control total_iten" name="total_iten[]" value="{detalle['total']}" readonly>
                        </td>
                        <td class="col-diseno2">
                            <img src="{img_url}" style="width:25%;height:25%;">
                             <input type="file" class="form-control respaldo" name="respaldo_{detalle['id']}[]">
                            <input type="hidden" name="imagen_actual_{detalle['id']}" value="{detalle['imagen'] or ''}">
                        </td>
                        <td align="center">
                            <button type="button" class="btn btn-danger btn-eliminarFilac btn-sm">
                                <span class="fa fa-times"></span>
                            </button>
                        </td>
                    </tr>'''
                contador_filas += 1

        str_html += f'''
                    </tbody>
                    <tfoot class="table-active text-right">
                        <tr>
                            <td align="center">
                                <button type="button" class="btn btn-sm" id="btn-addFilacotizacion">
                                    <span class="fa fa-plus"></span>
                                </button>
                            </td>
                            <td>Totales</td>
                            <td><input type="text" class="form-control-plaintext text-right" id="total_unitario" name="total_unitario" value="{total_unitario}" disabled></td>
                            <td><input type="text" class="form-control-plaintext text-right" id="total_precio" name="total_precio" value="{total_precio}" disabled></td>
                            <td>&nbsp;</td>
                            <td>&nbsp;</td>
                        </tr>
                    </tfoot>
                </table>
            </div>

            <div class="destinatario">
                <span class="destinatario-label">Forma de pago:</span>
                <input type="text" id="forma" name="forma" class="form-control" style="width:30%;" value="{cotizacion['forma']}">
            </div>

            <div class="destinatario">
                <span class="destinatario-label">Tiempo de validez:</span>
                <input type="text" id="validez" name="validez" class="form-control" style="width:30%;" value="{cotizacion['validez']}">
            </div>
            <div class="destinatario">
                <span class="destinatario-label">Tiempo de entrega:</span>
                <input type="text" id="entrega" name="entrega" class="form-control" style="width:30%;" value="{cotizacion['entrega']}">
            </div>

            <div class="modal-footer">
                <button class="btn btn-success" type="submit">GRABAR COTIZACIÓN</button>
            </div>

            <!-- Script para manejar archivos con JavaScript -->
            <script>
                // Al enviar el formulario, procesar los archivos
                document.addEventListener('DOMContentLoaded', function() {{
                    const form = document.querySelector('form');

                    form.addEventListener('submit', function(e) {{
                        // Procesar archivos antes de enviar
                        const fileInputs = document.querySelectorAll('input[type="file"].respaldo');

                        fileInputs.forEach((input, index) => {{
                            if (input.files.length > 0) {{
                                const detalleId = input.getAttribute('data-detalle-id');
                                if (detalleId) {{
                                    // Cambiar el nombre para incluir el ID
                                    input.name = 'respaldo[' + detalleId + ']';
                                }}
                            }} else {{
                                // Si no hay archivo, cambiar a campo oculto vacío
                                // para no interferir con el orden
                                const hiddenInput = document.createElement('input');
                                hiddenInput.type = 'hidden';
                                hiddenInput.name = 'respaldo[]';
                                hiddenInput.value = '';
                                input.parentNode.insertBefore(hiddenInput, input);
                                input.remove();
                            }}
                        }});
                    }});


                }});
            </script>'''

    return JsonResponse({'resultado': str_html})



def ver_cotizacion(request, valor):
    dato = int(base64.b64decode(valor).decode("utf-8"))
    cotizacion = buscar_cotizacion(dato)
    if not cotizacion:
        return HttpResponse("No se encontró", status=404)

    # Formatear fecha en español
    fecha_str = formatear_fecha_espanol(cotizacion['fecha'])
    img_url = static(f"biblioteca/logo/IMG-20251216-WA0012.ico")
    img_logo = static(f"biblioteca/logo/IMG-20251216-WA0012.jpg")

    str_html = f'''
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guara - Nota de Venta</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
        <link rel="icon" href="{img_url}">
    <style>
        /* Estilos para impresión */
        @page {{
            size: A4;
            margin: 2cm;
        }}

        @media print {{
            body {{
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }}

            .no-print {{
                display: none;
            }}

            .print-btn {{
                display: none;
            }}
        }}

        /* Estilos generales */
        body {{
            font-family: "Arial", sans-serif;
            margin: 0;
            padding: 0;
            color: #000;
            background-color: #fff;
            line-height: 1.4;
        }}

        .container {{
            max-width: 21cm;
            margin: 0 auto;
            padding: 0;
            position: relative;
        }}

        /* Encabezado */
        .header {{
            text-align: left;
            margin-bottom: 30px;
            padding-bottom: 15px;

        }}

        .company-name {{
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 8px;
            letter-spacing: 1px;
        }}

        .company-info {{
            font-size: 14px;
            line-height: 1.6;
        }}

        /* Fecha */
        .fecha {{
            text-align: right;
            margin: 25px 0;
            font-size: 14px;
            font-weight: bold;
        }}

        .fecha-label {{
            color: #F7634D;
        }}

        /* Destinatario */
        .destinatario {{
            margin: 25px 0 40px 0;
            font-size: 14px;
            font-weight: bold;
        }}

        .destinatario-label {{
            color: #F7634D;
        }}

        /* Título principal */
        .titulo-principal {{
            text-align: center;
            margin: 40px 0;
            font-size: 28px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}

        /* Tabla */
        .tabla-contenedor {{
            margin: 30px 0 50px 0;
            width: 100%;
        }}

        .tabla-productos {{
            width: 100%;
            border-collapse: collapse;
            border: 2px solid #333;
        }}

        .tabla-productos th {{
            background-color: #f0f0f0;
            border: 2px solid #333;
            padding: 12px 8px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
        }}

        .tabla-productos td {{
            border: 1px solid #333;
            padding: 10px 8px;
            text-align: center;
            font-size: 13px;
        }}

     .tabla-productos .col-detalle {{
            text-align: center;
            width: 33%;
            background-color: #575351;
            color:#FFFFFF;
        }}

         .tabla-productos .col-diseno {{
            text-align: center;
            width: 33%;
            background-color: #B0DFF7;
            color:#F7634D;
        }}

        .tabla-productos .col-diseno2 {{
            text-align: center;
            width: 33%;
            background-color: #B0DFF7;
            color:#F7634D;
        }}


        .tabla-productos .col-detalle2 {{
            text-align: left;
            width: 33%;
            background-color: #F2E6DF;
            color:#292626;
        }}
        .tabla-productos .col-talla {{
            width: 10%;
            background-color: #575351;
            color:#FFFFFF;
        }}

        .tabla-productos .col-talla2 {{
            width: 10%;
            background-color: #F2E6DF;
            color:#292626;
        }}
        .tabla-productos .col-cantidad {{
            width: 10%;
            background-color: #575351;
            color:#FFFFFF;
        }}

        .tabla-productos .col-cantidad2 {{
            width: 10%;
            background-color: #EBE9E6;
            color:#292626;
        }}

        /* Firmas */
        .firmas {{
            margin-top: 100px;
            padding-top: 30px;
            border-top: 1px solid #333;
        }}

        .firma-container {{
            display: flex;
            justify-content: space-between;
        }}

        .firma-col {{
            width: 45%;
        }}

        .firma-linea {{
            width: 100%;
            border-top: 1px solid #333;
            margin: 60px 0 5px 0;
        }}

        .firma-texto {{
            font-size: 12px;
            font-weight: bold;
            margin-bottom: 5px;
        }}

        .firma-nombre {{
            font-size: 11px;
            text-align: center;
            margin-top: 8px;
        }}

        /* Botón de impresión */
        .print-btn {{
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 12px 24px;
            background: #2c3e50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-family: Arial, sans-serif;
            font-size: 14px;
            z-index: 1000;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }}

        .print-btn:hover {{
            background: #1a252f;
        }}

        /* Marca de agua */
        .watermark {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(-45deg);
            font-size: 60px;
            color: rgba(0,0,0,0.1);
            z-index: -1;
            white-space: nowrap;
            pointer-events: none;
        }}
    </style>
</head>
<body>
    <!-- Botón para imprimir -->
    <button class="print-btn no-print" onclick="window.print()">
        🖨️ Imprimir / Guardar como PDF
    </button>


    <!-- Marca de agua -->
    <div class="watermark no-print">COPIA ORIGINAL</div>

    <div class="container">
        <!-- Encabezado con información de la empresa -->
        <div class="header">
            <div class="company-name">
             <img width="120" height="90" src="{img_logo}">
             </div>
            <div class="company-info">
                Cels. 79949364 - 65070403<br>
                Av. Canal lsuto C/ Landivar Edif. Los Cedros<br>
                Santa Cruz - Bolivia
            </div>
        </div>

        <!-- Fecha (derecha) -->
        <div class="fecha">
            <span class="fecha-label">FECHA:</span>
            <span id="fecha-actual">{fecha_str}</span>
        </div>

        <!-- Destinatario -->
        <div class="destinatario">
            <span class="destinatario-label">SEÑORES:</span>
            {cotizacion['prospecto']}
        </div>

        <!-- Título principal -->
        <div class="titulo-principal">
            COTIZACION
        </div>

        <!-- Tabla de productos -->
        <div class="tabla-contenedor">
            <table class="tabla-productos">
                <thead>
                    <tr>
                        <th class="col-talla">CANT</th>
                        <th class="col-detalle">DETALLE</th>
                        <th class="col-cantidad">PRECIO UNI BS.</th>
                        <th class="col-cantidad">TOTAL</th>
                        <th class="col-diseno">DISEÑO</th>
                    </tr>
                </thead>
                <tbody>
            '''


    listados =buscar_detalle_cotizacion(dato)
    total_unitario=0
    total_precio=0
    if listados:
            for listado in listados:
                total_item = float(listado['cantidad']) if listado['cantidad'] else 0
                precio_item=0
                precio_item = float(listado['precio']) if listado['precio'] else 0
                total_unitario = total_unitario + precio_item
                total_precio = total_precio + (total_item*precio_item)
                if listado['imagen']:
                    img_diseno = static(f"biblioteca/cotizaciones32/{listado['imagen']}")
                else:
                    img_diseno = static(f"biblioteca/marcas/nulo.jpg")
                str_html += f'''<tr>
                                    <td class="col-talla2">{listado['cantidad']}</td>
                                    <td class="col-detalle2">{listado['detalle']}</td>
                                    <td class="col-cantidad2">{listado['precio']}</td>
                                    <td class="col-cantidad2">{listado['total']}</td>
                                    <td class="col-diseno2"><img src="{img_diseno}"style="width:100%;heigth:100%;"></td>
                                </tr>'''

    str_html += f'''            <!-- Fila de total -->
                    <tr style="background-color: #f8f9fa; font-weight: bold;">
                        <td colspan="2" style="text-align: right;">TOTAL</td>
                        <td class="col-cantidad2">{total_unitario}</td>
                        <td class="col-cantidad2">{total_precio}</td>
                        <td class="col-diseno2"></td>
                    </tr>
                </tbody>
            </table>
        </div>
        <div class="destinatario">
            <span class="destinatario-label">FORMA DE PAGO:</span>
           {cotizacion['forma']}<br>
            <span class="destinatario-label">TIEMPO DE VALIDEZ DE LA COTIZACION:</span>
            {cotizacion['validez']}<br>
            <span class="destinatario-label">TIEMPO DE ENTREGA:</span>
            {cotizacion['entrega']}
        </div>


        <!-- Pie de página -->
        <div style="font-size: 9px; color: #666; margin-top: 50px; padding-top: 10px; border-top: 1px solid #ccc;">
            Av. Canal Isuto C/landivar Edif. Los cedros Santa cruz - Bolivia Cel.: 79949364 - 65070403 Mail: guara.corp@gmail.com
        </div>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function() {{
            // Auto-llenar fecha actual si no hay datos
            // Configurar para impresión
            window.onbeforeprint = function() {{
                // Ocultar elementos no deseados al imprimir
                document.querySelectorAll(".no-print").forEach(el => {{
                    el.style.display = "none";
                }});
            }};

            window.onafterprint = function() {{
                // Restaurar elementos después de imprimir
                document.querySelectorAll(".no-print").forEach(el => {{
                    el.style.display = "";
                }});
            }};
        }});

    </script>
</body>
</html>
'''


    return HttpResponse(str_html)


 #---------------------------------RECIBOS-----------------------------------#

def lista_recibos(request):
    tareas = listar_recibos()  # Obtener datos
    return JsonResponse({'tareas': tareas})


def registra_recibo(request):
    if request.method == "POST":
        tipo = int(request.POST.get("tiporecibo", 0))
        recibo_id = int(request.POST.get("recibo_id",0))
        cliente = request.POST.get("clienter", "")
        cotizacionr = request.POST.get("cotizacionr", "")
        metodo = request.POST.get("metodo", "")
        porcentaje = request.POST.get("porcentaje", "100%")
        cuenta = request.POST.get("cuenta",0)
        saldo = request.POST.get("saldo", 0)
        fecha = request.POST.get("fechai", "")
        usuario_registra = request.session.get("dpilogin", "Desconocido")
        fecha_registra = now().strftime("%Y-%m-%d %H:%M:%S")
        detalles = request.POST.getlist('detallei[]')
        cantidades = request.POST.getlist('cantidadi[]')
        precios = request.POST.getlist('precioi[]')
        try:
            with connections['default'].cursor() as cursor:
                if tipo == 1:
                    cursor.execute("""
                        INSERT INTO recibos
                        (cliente,fecha,metodo,estado,porcentaje,cuenta,saldo,fecha_carga, usuario_carga,cotizacion)
                        VALUES (%s, %s,%s,%s, %s, %s,%s,%s,%s,%s)
                        """, [cliente,fecha,metodo,1,porcentaje,cuenta,saldo, fecha_registra, usuario_registra,cotizacionr])

                     # OBTENER EL ÚLTIMO ID INSERTADO
                    ultimo_id = cursor.lastrowid
                    cantidad_contador=0
                    precio_total = 0
                    detalle_lista = ''
                    for detalle_,cantidad_,precio_ in zip(detalles, cantidades,precios):
                        try:
                            cantidad_val = float(cantidad_) if cantidad_ else 0
                            precio_val = float(precio_) if precio_ else 0
                            cantidad_contador = cantidad_contador + cantidad_val
                            precio_total = precio_total + (cantidad_val*precio_val)
                            detalle_lista = detalle_ + ',' + detalle_lista
                            cursor.execute("""
                            INSERT INTO recibos_detalle
                            (recibo,cliente,fecha,detalle,cantidad,total,estado,fecha_carga, usuario_carga)
                            VALUES (%s, %s, %s, %s, %s,%s,%s,%s,%s)
                            """, [ultimo_id,cliente,fecha,detalle_,cantidad_val,precio_val,1,fecha_registra,usuario_registra])
                        except Exception as e:
                            messages.warning(request, f"Error al insertar el detalle: {str(e)}")

                    cursor.execute("""
                                UPDATE recibos
                                SET cantidad = %s,
                                total = %s,
                                detalle=%s
                                WHERE id = %s
                                """, [cantidad_contador,precio_total,detalle_lista, ultimo_id])
                else:
                    if tipo == 2 and recibo_id:
                        cursor.execute("""
                            UPDATE recibos
                            SET cliente = %s,
                            fecha = %s,
                            metodo=%s,
                            porcentaje=%s,
                            cuenta=%s,
                            cotizacion=%s,
                            saldo=%s
                            WHERE id = %s
                            """, [cliente,fecha,metodo,porcentaje,cuenta,cotizacionr,saldo,recibo_id])

                        cursor.execute("""
                                UPDATE recibos_detalle
                                SET estado ='0'
                                WHERE recibo=%s
                            """, [recibo_id])
                        cantidad_contador=0
                        precio_total = 0
                        detalle_lista = ''

                        for detalle_,cantidad_,precio_ in zip(detalles, cantidades,precios):
                            try:
                                cantidad_val = float(cantidad_) if cantidad_ else 0
                                precio_val = float(precio_) if precio_ else 0
                                cantidad_contador = cantidad_contador + cantidad_val
                                precio_total = precio_total + (cantidad_val*precio_val)
                                detalle_lista = detalle_ + ',' + detalle_lista
                                cursor.execute("""
                                INSERT INTO recibos_detalle
                                (recibo,cliente,fecha,detalle,cantidad,total,estado,fecha_carga, usuario_carga)
                                VALUES (%s, %s, %s, %s, %s, %s,%s,%s,%s)
                                """, [recibo_id,cliente,fecha,detalle_,cantidad_val,precio_val,1,fecha_registra,usuario_registra])
                            except Exception as e:
                                messages.warning(request, f"Error al insertar el detalle: {str(e)}")

                        cursor.execute("""
                                    UPDATE recibos
                                    SET cantidad = %s,
                                    total = %s,
                                    detalle=%s
                                    WHERE id = %s
                                    """, [cantidad_contador,precio_total,detalle_lista, recibo_id])

            messages.success(request, "Recibo guardado correctamente.")
            return redirect("configuracion")
        except Exception as e:
            messages.error(request, f"Ocurrió un error: {e}")
            return redirect("configuracion")

    return HttpResponse("Método no permitido", status=405)


def eliminar_recibo(request,valor):

    try:

        with connections['default'].cursor() as cursor:
            cursor.execute("""
                UPDATE recibos
                SET estado='0'
                WHERE id=%s
            """,[valor])
        respuesta="Se realizo con exito"

    except Exception as e:
            return redirect("configuracion")
    return JsonResponse({'respuesta': respuesta})


def editar_recibo(request,valor):
    recibo= buscar_recibo(valor)
    clientes = listar_clientes()
    str_html = ""
    if recibo:
        str_html += f'''
                    <input type="hidden" id="tiporecibo" name="tiporecibo" value="2">
                     <input type="hidden" id="recibo_id" name="recibo_id" value="{recibo['id']}">
                         <div class="form-group">
                        <label for="serviceTitle">Cliente *</label>
                        <select id="clienter" name="clienter" class="form-control" required>'''
        for cliente in clientes:
            if int(cliente['id']) == int(recibo['cliente']):
                str_html += f'''<option value="{cliente['id']}" selected>{cliente['nombre']}</option>'''
            else:
                str_html += f'''<option value="{cliente['id']}">{cliente['nombre']}</option>'''

        str_html += f'''</select>
                    </div>
                     <div class="form-group">
                        <label for="serviceTitle">Cotizacion *</label>
                        <select id="cotizacionr" name="cotizacionr" class="form-control" required>'''

        lista_cotizacion = revisar_cotizaciones(recibo['cliente'])
        if lista_cotizacion:
            for cotizacion in lista_cotizacion:
                if cotizacion['id'] == recibo['cotizacion']:
                    str_html += f'''<option value="{cotizacion['id']}" selected>{cotizacion['detalle']}</option>'''
                else:
                    str_html += f'''<option value="{cotizacion['id']}">{cotizacion['detalle']}</option>'''
        else:
            str_html += f'''<option value="" disabled selected>No se encontro una cotizacion</option>'''
        str_html += f'''</select>
                    </div>

                    <a href="#" id="revicion_deuda" name="revicion_deuda" title="verificar historial de pagos"><i class="fas fa-coins"></i> Revisar pagos</a>


                        <div id="alerta_recibo" name="alerta_recibo">

                        </div>
                     <div class="form-group">
                        <label for="serviceTitle">Fecha *</label>
                        <input type="date" id="fechai" name="fechai" class="form-control" required value="{recibo['fecha']}">
                    </div>

                      <div class="form-group">
                        <label for="serviceTitle">Metodo de pago</label>
                            <select id="metodo" name="metodo" class="form-control">
                            <option value="Efectivo">Efectivo</option>
                            <option value="Qr">Qr</option>
                             <option value="Transferencia">Transferencia</option>
                            </select>
                        </div>


                     <div class="table-responsive">
                    <table class="table table-bordered">
                                <thead>
                                    <tr>
                                            <td width="4%" height="31">#</td>
                                            <td width="65%">DETALLE</td>
                                            <td>CANTIDAD</td>
                                            <td>PRECIO</td>
                                            <td width="5%">ANULAR</td>
                                    </tr>
                                </thead>
                                <tbody id="tbody-ingresos" >'''
        valor_ = recibo['id']
        listados =buscar_detalle_recibos(valor_)
        total=0
        total_precio=0
        if listados:
            contador=0
            for listado in listados:
                contador=contador + 1
                total_item=0
                total_item = float(listado['cantidad']) if listado['cantidad'] else 0
                precio_item=0
                precio_item = float(listado['total']) if listado['total'] else 0
                total = total + total_item
                total_precio = total_precio + (total_item*precio_item)
                str_html += f''' <tr>
                                <td width="4%" align="center">{contador}</td>
                                <td width="65%">
                                    <input type="text" class="form-control detallei" name="detallei[]" value="{listado['detalle']}">
                                </td>
                                <td><input type="text" class="form-control cantidadi" name="cantidadi[]" value="{listado['cantidad']}"></td>
                                <td><input type="text" class="form-control precioi" name="precioi[]" value="{listado['total']}"></td>
                                <td align="center">
                                    <button type="button" class="btn btn-danger btn-eliminarFilai btn-sm">
                                        <span class="fa fa-times"></span>
                                    </button>
                                </td>
                            </tr>'''


        str_html += f'''    </tbody>
                                <tfoot class="table-active text-right" >
                                  <tr>
                                        <td align="center"> <button type="button" class="btn btn-sm" id="btn-addFilai"> <span class="fa fa-plus"></span> </button></td>
                                        <td colspan="2">Totales</td>
                                        <td><input type="text" class="form-control-plaintext text-right" id="total_generali" name="total_generali"  value="{float(total):.2f}" disabled></td>
                                        <td><input type="text" class="form-control-plaintext text-right" id="total_precioi" name="total_precioi"  value="{float(total_precio):.2f}" disabled></td>
                                        <td>&nbsp;</td>

                                  </tr>

                              </tfoot>
                            </table>

                             <div class="form-group">
                        <label for="serviceTitle">Porcentaje </label>
                        <input type="text" id="porcentaje" name="porcentaje" class="form-control" value="{recibo['porcentaje']}">
                    </div>
                    <div class="form-group">
                        <label for="serviceTitle">A cuenta </label>
                        <input type="text" id="cuenta" name="cuenta" class="form-control" value="{recibo['cuenta']}">
                    </div>
                    <div class="form-group">
                        <label for="serviceTitle">Saldo </label>
                        <input type="text" id="saldo" name="saldo" class="form-control" value="{recibo['saldo']}">
                    </div>
                             </div>
                     '''

    return JsonResponse({'resultado': str_html})





def revisar_saldo(request,valor):
    str_html2 = ""
    lista_cotizacion = revisar_cotizaciones(valor)
    if lista_cotizacion:
        for cotizacion in lista_cotizacion:
            str_html2 += f'''<option value="{cotizacion['id']}">{cotizacion['detalle']}</option>'''
    else:
        str_html2 += f'''<option value="" disabled selected>No se encontraron cotizaciones</option>'''

    return JsonResponse({'opciones':str_html2})



def revisar_saldo_cotizacion(request,valor):
    cliente,cotizacion = valor.split("+")
    str_html = ""
    str_html += f'''<h3 style="margin: 20px 0 10px 0;">Historial de Pagos</h3>
                <div class="payment-details">'''

    pagos = revisar_pagos(cliente,cotizacion)
    coti = buscar_cotizacion(cotizacion)
    if pagos:
        str_html += f'''<h4 style="margin: 20px 0 10px 0;">Monto total {coti['monto']}</h4>'''
        for pago in pagos:
            str_html += f'''<div class="payment-item">
                        <div class="payment-info">
                            <span class="payment-date">{pago['fecha']}</span>
                            <span class="payment-amount">{pago['cuenta']}</span>
                            <span>{pago['metodo']}</span>
                        </div>
                    </div>'''
    else:
        str_html += f'''<p>No hay pagos registrados</p>'''

    return JsonResponse({'resultado':str_html})


def ver_recibo(request, valor):
    nota = buscar_recibo(valor)
    if not nota:
        return HttpResponse("No se encontró", status=404)

    # Formatear fecha en español
    fecha_emision = formatear_fecha_espanol(nota['fecha_carga'])
    fecha_pago = formatear_fecha_espanol(nota['fecha'])
    año = obtener_año(nota['fecha'])

    img_url = static(f"biblioteca/logo/IMG-20251216-WA0012.ico")
    img_logo = static(f"biblioteca/logo/IMG-20251216-WA0012.jpg")

    str_html = f'''
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guara - Recibo de pago</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
        <link rel="icon" href="{img_url}">
    <style>
        /* Estilos para impresión */
        @page {{
            size: A4;
            margin: 2cm;
        }}

        @media print {{
            body {{
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }}

            .no-print {{
                display: none;
            }}

            .print-btn {{
                display: none;
            }}
        }}

        /* Estilos generales */
        body {{
            font-family: "Arial", sans-serif;
            margin: 0;
            padding: 0;
            color: #000;
            background-color: #fff;
            line-height: 1.4;
        }}

        .container {{
            max-width: 21cm;
            margin: 0 auto;
            padding: 0;
            position: relative;
        }}

        /* Encabezado */
        .header {{
            text-align: left;
            margin-bottom: 30px;
            padding-bottom: 15px;

        }}

        .company-name {{
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 8px;
            letter-spacing: 1px;
        }}

        .company-info {{
            font-size: 10px;
            line-height: 1.6;
        }}

        /* Fecha */
        .fecha {{
            text-align: right;
            margin: 25px 0;
            font-size: 14px;
            font-weight: bold;
        }}

        .fecha-label {{
            color: #000;
        }}

        /* Destinatario */
        .destinatario {{
            margin: 25px 0 40px 0;
            font-size: 14px;
            font-weight: bold;
            text-align: left;
        }}

        .destinatario-label {{
            color: #000;
        }}

        /* Título principal */
        .titulo-principal {{
            text-align: center;
            margin: 40px 0;
            font-size: 28px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}


  .receipt-title .receipt-number {{
            font-size: 1.1rem;
            color: #7f8c8d;
        }}

        .receipt-body {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 30px;
        }}

   .receipt-title {{
            text-align: right;
        }}

        .receipt-title h3 {{
            color: #3498db;
            font-size: 2.2rem;
            margin-bottom: 5px;
        }}


        /* Tabla */
        .tabla-contenedor {{
            margin: 30px 0 50px 0;
            width: 100%;
        }}

        .tabla-productos {{
            width: 100%;
            border-collapse: collapse;
            border: 2px solid #333;
        }}

        .tabla-productos th {{
            background-color: #f0f0f0;
            border: 2px solid #333;
            padding: 12px 8px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
        }}

        .tabla-productos td {{
            border: 1px solid #333;
            padding: 10px 8px;
            text-align: center;
            font-size: 13px;
        }}

        .tabla-productos .col-detalle {{
            text-align: center;
            width: 70%;
            background-color: #918787;
            color:#FFFFFF;
        }}

        .tabla-productos .col-detalle2 {{
            text-align: left;
            width: 70%;
            background-color: #FFFFFF;
            color:#292626;
        }}
        .tabla-productos .col-talla {{
            width: 15%;
            background-color: #918787;
            color:#FFFFFF;
        }}

        .tabla-productos .col-talla2 {{
            width: 15%;
            background-color: #FFFFFF;
            color:#292626;
        }}
        .tabla-productos .col-cantidad {{
            width: 15%;
            background-color: #918787;
            color:#FFFFFF;
        }}

        .tabla-productos .col-cantidad2 {{
            width: 15%;
            background-color: #FFFFFF;
            color:#292626;
        }}
        /* Firmas */
        .firmas {{
            margin-top: 100px;
            padding-top: 30px;
            border-top: 1px solid #333;
        }}

        .firma-container {{
            display: flex;
            justify-content: space-between;
        }}

        .firma-col {{
            width: 45%;
        }}

        .firma-linea {{
            width: 100%;
            border-top: 1px solid #333;
            margin: 60px 0 5px 0;
        }}

        .firma-texto {{
            font-size: 12px;
            font-weight: bold;
            margin-bottom: 5px;
        }}

        .firma-nombre {{
            font-size: 11px;
            text-align: center;
            margin-top: 8px;
        }}

        /* Botón de impresión */
        .print-btn {{
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 12px 24px;
            background: #2c3e50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-family: Arial, sans-serif;
            font-size: 14px;
            z-index: 1000;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }}

        .print-btn:hover {{
            background: #1a252f;
        }}

        /* Marca de agua */
        .watermark {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(-45deg);
            font-size: 60px;
            color: rgba(0,0,0,0.1);
            z-index: -1;
            white-space: nowrap;
            pointer-events: none;
        }}

        .receipt-title {{
            text-align: right;
        }}

          .section-title {{
            font-size: 1.2rem;
            color: #2c3e50;
            margin-bottom: 15px;
            padding-bottom: 5px;
            border-bottom: 1px solid #eee;
            font-weight: 600;
        }}

            .info-row {{
            display: flex;
            margin-bottom: 10px;
        }}

        .info-label {{
            flex: 0 0 40%;
            font-weight: 600;
            color: #555;
        }}

        .info-value {{
            flex: 1;
            color: #333;
        }}


  .receipt-container {{
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
            padding: 30px;
            position: relative;
            overflow: hidden;
        }}

        .receipt-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-bottom: 20px;
            border-bottom: 2px solid #eee;
            margin-bottom: 25px;
        }}
    </style>
</head>
<body>
    <!-- Botón para imprimir -->
    <button class="print-btn no-print" onclick="window.print()">
        🖨️ Imprimir / Guardar como PDF
    </button>

    <!-- Marca de agua -->
    <div class="watermark no-print">COPIA ORIGINAL</div>

    <div class="container">
        <!-- Encabezado con información de la empresa -->


        <div class="receipt-header">
            <div class="company-name">
             <img width="120" height="90" src="{img_logo}">
                 <div class="company-info">
               Cels. 79949364 - 65070403<br>
                Av. Canal lsuto C/ Landivar Edif. Los Cedros<br>
                Santa Cruz - Bolivia
            </div>
             </div>

             <div class="receipt-title">

               <h3>RECIBO DE INGRESO</h3>
                    <div class="receipt-number">Nº <strong>R-{año}-00{valor}</strong></div>
                    <div class="info-label">Fecha de Emisión:</div>{fecha_emision}
            </div>

        </div>






           <div class="receipt-body">
                <div class="section">
                    <h4 class="section-title">Información del Cliente</h4>
                    <div class="info-row">
                        <div class="info-label">Señores:</div>
                        <div class="info-value">{nota['ncliente']}</div>
                    </div>
                    <div class="info-row">
                        <div class="info-label">Cel:</div>
                        <div class="info-value">{nota['celular']}</div>
                    </div>
                </div>

                <div class="section">
                    <h4 class="section-title">Detalles del Pago</h4>
                    <div class="info-row">
                        <div class="info-label">Método:</div>
                        <div class="info-value"> {nota['metodo']}</div>
                    </div>

                    <div class="info-row">
                        <div class="info-label">Fecha de pago:</div>
                        <div class="info-value">{fecha_pago}</div>
                    </div>

                </div>
            </div>


        <!-- Tabla de productos -->
        <div class="tabla-contenedor">
            <table class="tabla-productos">
                <thead>
                    <tr>
                        <th class="col-detalle">DETALLE</th>
                        <th class="col-cantidad">CANTIDAD</th>
                        <th class="col-cantidad">PRECIO</th>
                        <th class="col-cantidad">SUBTOTAL</th>
                    </tr>
                </thead>
                <tbody>
            '''

    detalles = buscar_detalle_recibos(valor)
    total=0
    total_precio=0
    for detalle in detalles:
        total_precio = total_precio + (float(detalle['cantidad'])*float(detalle['total']))
        subtotal = float(detalle['cantidad'])*float(detalle['total'])
        total=total + float(detalle['cantidad'])
        str_html += f'''
                <tr>
                 <td class="col-detalle2">{detalle['detalle']}</td>
                 <td class="col-cantidad2">{detalle['cantidad']}</td>
                 <td class="col-cantidad2">{detalle['total']}</td>
                 <td class="col-cantidad2">{subtotal}</td>
             </tr>     '''


    str_html += f'''            <!-- Fila de total -->
                    <tr style="background-color: #f8f9fa; font-weight: bold;">
                        <td rowspan="4" class="col-detalle2" style="text-align: right;"></td>
                        <td colspan="2" class="col-cantidad2">Total Cantidad:</td>
                        <td class="col-cantidad2">{total}</td>

                    </tr>
                     <tr style="background-color: #f8f9fa; font-weight: bold;">

                    <td colspan="2" class="col-cantidad2">Saldo total:</td>
                     <td class="col-cantidad2">{total_precio}</td>
                    </tr>
                    <tr style="background-color: #f8f9fa; font-weight: bold;">

                    <td colspan="2" class="col-cantidad2">A cuenta {nota['porcentaje']}:</td>
                     <td class="col-cantidad2">{nota['cuenta']}</td>
                    </tr>
                    <tr style="background-color: #f8f9fa; font-weight: bold;">

                    <td colspan="2" class="col-cantidad2">Saldo a pagar:</td>
                     <td class="col-cantidad2">{nota['saldo']}</td>
                    </tr>
                </tbody>
            </table>
        </div>

        <!-- Firmas -->
        <div class="firmas">
            <div class="firma-container">
                <div class="firma-col">
                    <div class="firma-texto">ENTREGADO POR:</div>
                    <div class="firma-linea"></div>
                    <div class="firma-nombre">
                        Nombre y Firma
                    </div>
                    <div class="firma-nombre" style="font-size: 10px; margin-top: 5px;">
                        Fecha: __/__/____
                    </div>
                </div>

                <div class="firma-col">
                    <div class="firma-texto">RECIBIDO POR:</div>
                    <div class="firma-linea"></div>
                    <div class="firma-nombre">
                        Nombre y Firma del Cliente
                    </div>
                    <div class="firma-nombre" style="font-size: 10px; margin-top: 5px;">
                        Fecha: __/__/____
                    </div>
                </div>
            </div>
        </div>

        <!-- Pie de página -->
        <div style="text-align: center; font-size: 9px; color: #666; margin-top: 50px; padding-top: 10px; border-top: 1px solid #ccc;">
            Documento generado electrónicamente por Guara<br>
            Código: {valor} |
            Versión: 1.0
        </div>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function() {{
            // Auto-llenar fecha actual si no hay datos
            // Configurar para impresión
            window.onbeforeprint = function() {{
                // Ocultar elementos no deseados al imprimir
                document.querySelectorAll(".no-print").forEach(el => {{
                    el.style.display = "none";
                }});
            }};

            window.onafterprint = function() {{
                // Restaurar elementos después de imprimir
                document.querySelectorAll(".no-print").forEach(el => {{
                    el.style.display = "";
                }});
            }};
        }});


    </script>
</body>
</html>
'''

    return HttpResponse(str_html)



#---------------------------------PAGOS-----------------------------------#


def lista_pagos(request):
    tareas = listar_pagos()  # Obtener datos
    return JsonResponse({'tareas': tareas})

def registra_pago(request):
    if request.method == "POST":
        tipo = int(request.POST.get("tipopago", 0))
        egreso_id = int(request.POST.get("egreso_id",2))
        cotizacion_id = int(request.POST.get("cotizacion_id",0))
        titular = request.POST.get("titular", "")
        detalle = request.POST.get("detalle", "")
        monto = request.POST.get("monto",0)
        fecha = request.POST.get("fechap", "")
        usuario_registra = request.session.get("dpilogin", "Desconocido")
        fecha_registra = now().strftime("%Y-%m-%d %H:%M:%S")
        respaldos = request.FILES.get('respaldo')
        # Obtener listas de campos regulares
        titulares = request.POST.getlist('titulae[]')
        detalles = request.POST.getlist('detallee[]')
        montos = request.POST.getlist('montoe[]')
        respaldoe = request.POST.getlist('respaldoe[]')

        try:
            with connections['default'].cursor() as cursor:
                if tipo == 1:  # INSERTAR MÚLTIPLES REGISTROS
                    # Determinar el número máximo de filas basado en la lista más larga
                    max_filas = max(len(titulares), len(detalles), len(montos))

                    registros_insertados = 0

                    # Procesar cada posible fila
                    for i in range(max_filas):
                        # Obtener valores con manejo de índices fuera de rango
                        titular = titulares[i] if i < len(titulares) else ""
                        detalle = detalles[i] if i < len(detalles) else ""
                        monto = montos[i] if i < len(montos) else 0
                        # Solo insertar si al menos el titular tiene contenido
                        # (puedes ajustar esta condición según tus necesidades)
                        if titular and titular.strip():

                            adjuntos_portada = None

                            if i < len(respaldoe) and respaldoe[i]:
                                archivo = respaldoe[i]
                                if archivo.name:
                                    nombre_original = archivo.name
                                    nombre_base, extension = os.path.splitext(nombre_original)
                                    nombre_unico = f"{nombre_base}_{uuid.uuid4().hex[:8]}{extension}"
                                    adjuntos_path_portada = os.path.join("biblioteca/pagos/", nombre_unico)
                                    full_path = os.path.join(settings.STATICFILES_DIRS[0], adjuntos_path_portada)
                                    os.makedirs(os.path.dirname(full_path), exist_ok=True)
                                    with open(full_path, "wb+") as destination:
                                        for chunk in archivo.chunks():
                                            destination.write(chunk)
                                    adjuntos_portada = nombre_unico


                            # Insertar el registro en la base de datos
                            cursor.execute("""
                                INSERT INTO egresos
                                (titular, fecha, detalle, monto, estado, fecha_carga, usuario_carga, respaldo,cotizacion)
                                VALUES (%s, %s, %s, %s, %s, %s, %s, %s,%s)
                                """, [
                                    titular,
                                    fecha,
                                    detalle if detalle else '',  # Si está vacío, guardar NULL
                                    monto if monto else 0,  # Si está vacío, guardar 0
                                    1,
                                    fecha_registra,
                                    usuario_registra,
                                    adjuntos_portada,
                                    cotizacion_id
                                ])

                            registros_insertados += 1

                    if registros_insertados > 0:
                        messages.success(request, f"{registros_insertados} pago(s) guardado(s) correctamente.")
                    else:
                        messages.warning(request, "No se insertaron registros. Verifica que hayas completado los campos.")

                elif tipo == 2 and egreso_id:  # EDITAR UN REGISTRO EXISTENTE
                    adjuntos_portada = None
                        # Manejar archivo si existe para esta fila
                    if respaldos:
                        if respaldos.name:  # Verificar que tenga nombre
                            # Generar nombre único para evitar conflictos
                            nombre_original = respaldos.name
                            nombre_base, extension = os.path.splitext(nombre_original)
                            nombre_unico = f"{nombre_base}_{uuid.uuid4().hex[:8]}{extension}"

                                # Ruta relativa y absoluta
                            adjuntos_path_portada = os.path.join("biblioteca/pagos/", nombre_unico)
                            full_path = os.path.join(settings.STATICFILES_DIRS[0], adjuntos_path_portada)

                                    # Crear directorio si no existe
                            os.makedirs(os.path.dirname(full_path), exist_ok=True)
                                # Guardar archivo
                            with open(full_path, "wb+") as destination:
                                for chunk in respaldos.chunks():
                                    destination.write(chunk)

                            adjuntos_portada = nombre_unico
                        cursor.execute("""
                            UPDATE egresos
                            SET titular = %s,
                            fecha = %s,
                            detalle=%s,
                            monto=%s,
                            respaldo=%s,
                            cotizacion =%s
                            WHERE id = %s
                            """, [titular,fecha,detalle,monto,adjuntos_portada,cotizacion_id,egreso_id])
                    else:
                        cursor.execute("""
                            UPDATE egresos
                            SET titular = %s,
                            fecha = %s,
                            detalle=%s,
                            monto=%s,
                            cotizacion =%s
                            WHERE id = %s
                            """, [titular,fecha,detalle,monto,cotizacion_id,egreso_id])
                    messages.success(request, "Pago actualizado correctamente.")

            return redirect("configuracion")

        except Exception as e:
            messages.error(request, f"Ocurrió un error: {e}")
            return redirect("configuracion")

    return HttpResponse("Método no permitido", status=405)



def registra_pago_anterior(request):
    if request.method == "POST":
        tipo = int(request.POST.get("tipopago", 0))
        egreso_id = int(request.POST.get("egreso_id",0))
        titular = request.POST.get("titular", "")
        detalle = request.POST.get("detalle", "")
        monto = request.POST.get("monto",0)
        fecha = request.POST.get("fechap", "")
        usuario_registra = request.session.get("dpilogin", "Desconocido")
        fecha_registra = now().strftime("%Y-%m-%d %H:%M:%S")
        respaldos = request.FILES.get('respaldo')
        try:
            with connections['default'].cursor() as cursor:
                if tipo == 1:
                    adjuntos_portada = None
                    # Manejar archivo si existe para esta fila
                    if respaldos:
                        if respaldos.name:  # Verificar que tenga nombre
                            # Generar nombre único para evitar conflictos
                            nombre_original = respaldos.name
                            nombre_base, extension = os.path.splitext(nombre_original)
                            nombre_unico = f"{nombre_base}_{uuid.uuid4().hex[:8]}{extension}"

                            # Ruta relativa y absoluta
                            adjuntos_path_portada = os.path.join("biblioteca/pagos/", nombre_unico)
                            full_path = os.path.join(settings.STATICFILES_DIRS[0], adjuntos_path_portada)

                                # Crear directorio si no existe
                            os.makedirs(os.path.dirname(full_path), exist_ok=True)
                            # Guardar archivo
                            with open(full_path, "wb+") as destination:
                                for chunk in respaldos.chunks():
                                    destination.write(chunk)

                            adjuntos_portada = nombre_unico

                    cursor.execute("""
                        INSERT INTO egresos
                        (titular,fecha,detalle,monto,estado,fecha_carga, usuario_carga,respaldo)
                        VALUES (%s, %s,%s,%s, %s, %s,%s,%s)
                        """, [titular,fecha,detalle,monto,1,fecha_registra, usuario_registra,adjuntos_portada])

                else:
                    if tipo == 2 and egreso_id:
                        adjuntos_portada = None
                        # Manejar archivo si existe para esta fila
                        if respaldos:
                            if respaldos.name:  # Verificar que tenga nombre
                            # Generar nombre único para evitar conflictos
                                nombre_original = respaldos.name
                                nombre_base, extension = os.path.splitext(nombre_original)
                                nombre_unico = f"{nombre_base}_{uuid.uuid4().hex[:8]}{extension}"

                                # Ruta relativa y absoluta
                                adjuntos_path_portada = os.path.join("biblioteca/pagos/", nombre_unico)
                                full_path = os.path.join(settings.STATICFILES_DIRS[0], adjuntos_path_portada)

                                    # Crear directorio si no existe
                                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                                # Guardar archivo
                                with open(full_path, "wb+") as destination:
                                    for chunk in respaldos.chunks():
                                        destination.write(chunk)

                                adjuntos_portada = nombre_unico
                        cursor.execute("""
                            UPDATE egresos
                            SET titular = %s,
                            fecha = %s,
                            detalle=%s,
                            monto=%s,
                            respaldo=%s
                            WHERE id = %s
                            """, [titular,fecha,detalle,monto,adjuntos_portada,egreso_id])



            messages.success(request, "Pago guardado correctamente.")
            return redirect("configuracion")
        except Exception as e:
            messages.error(request, f"Ocurrió un error: {e}")
            return redirect("configuracion")

    return HttpResponse("Método no permitido", status=405)


def eliminar_pago(request,valor):

    try:

        with connections['default'].cursor() as cursor:
            cursor.execute("""
                UPDATE egresos
                SET estado='0'
                WHERE id=%s
            """,[valor])
        respuesta="Se realizo con exito"

    except Exception as e:
            return redirect("configuracion")
    return JsonResponse({'respuesta': respuesta})


def editar_pago(request,valor):
    pago= buscar_pago(valor)
    str_html = ""
    if pago:
        if pago['respaldo']:
            img_url = static(f"biblioteca/pagos/{pago['respaldo']}")
        else:
            img_url = static(f"biblioteca/marcas/nulo.jpg")
        str_html += f'''
                    <input type="hidden" id="tipopago" name="tipopago" value="2">
                     <input type="hidden" id="egreso_id" name="egreso_id" value="{pago['id']}">
                     <input type="hidden" id="cotizacion_id" name="cotizacion_id" value="{pago['cotizacion']}">
                        <div class="form-group">
                        <label for="serviceTitle">Razon *</label>
                        <input type="text" id="titular" name="titular" class="form-control" required value="{pago['titular']}">

                        </div>

                     <div class="form-group">
                        <label for="serviceTitle">Fecha *</label>
                        <input type="date" id="fechap" name="fechap" class="form-control" required value="{pago['fecha']}">
                    </div>

                       <div class="form-group">
                        <label for="serviceTitle">Detalle del pago</label>
                            <textarea id="detalle" name="detalle" class="form-control">{pago['detalle']}</textarea>
                        </div>

                        <div class="form-group">
                        <label for="serviceTitle">Monto *</label>
                        <input type="text" id="monto" name="monto" class="form-control" required value="{pago['monto']}">
                        </div>

                        <div class="form-group">
                        <label for="brandLogo">Respaldo</label>
                        <input type="file"  id="respaldo" name="respaldo" class="form-control">

                        </div>

                    <div class="form-group">
                        <label for="brandLogo">Respaldo Actual</label>
                        <img src="{img_url}" alt="Producto"  style="width:25%;heigth:25%;" >

                    </div>

                     '''

    return JsonResponse({'resultado': str_html})





def ver_pago(request, valor):
    pago = buscar_pago(valor)
    if not pago:
        return HttpResponse("No se encontró", status=404)

    # Formatear fecha en español
    fecha_emision = formatear_fecha_espanol(pago['fecha_carga'])
    fecha_pago = formatear_fecha_espanol(pago['fecha'])
    año = obtener_año(pago['fecha'])

    img_url = static(f"biblioteca/logo/IMG-20251216-WA0012.ico")
    img_logo = static(f"biblioteca/logo/IMG-20251216-WA0012.jpg")

    str_html = f'''
    <!DOCTYPE html>
    <html lang="es">
    <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guara - Pagos realizados</title>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js"></script>
        <link rel="icon" href="{img_url}">
    <style>
        /* Estilos para impresión */
        @page {{
            size: A4;
            margin: 2cm;
        }}

        @media print {{
            body {{
                -webkit-print-color-adjust: exact;
                print-color-adjust: exact;
            }}

            .no-print {{
                display: none;
            }}

            .print-btn {{
                display: none;
            }}
        }}

        /* Estilos generales */
        body {{
            font-family: "Arial", sans-serif;
            margin: 0;
            padding: 0;
            color: #000;
            background-color: #fff;
            line-height: 1.4;
        }}

        .container {{
            max-width: 21cm;
            margin: 0 auto;
            padding: 0;
            position: relative;
        }}

        /* Encabezado */
        .header {{
            text-align: left;
            margin-bottom: 30px;
            padding-bottom: 15px;

        }}

        .company-name {{
            font-size: 24px;
            font-weight: bold;
            margin-bottom: 8px;
            letter-spacing: 1px;
        }}

        .company-info {{
            font-size: 10px;
            line-height: 1.6;
        }}

        /* Fecha */
        .fecha {{
            text-align: right;
            margin: 25px 0;
            font-size: 14px;
            font-weight: bold;
        }}

        .fecha-label {{
            color: #000;
        }}

        /* Destinatario */
        .destinatario {{
            margin: 25px 0 40px 0;
            font-size: 14px;
            font-weight: bold;
            text-align: left;
        }}

        .destinatario-label {{
            color: #000;
        }}

        /* Título principal */
        .titulo-principal {{
            text-align: center;
            margin: 40px 0;
            font-size: 28px;
            font-weight: bold;
            text-transform: uppercase;
            letter-spacing: 1px;
        }}


  .receipt-title .receipt-number {{
            font-size: 1.1rem;
            color: #7f8c8d;
        }}

        .receipt-body {{
            display: grid;
            grid-template-columns: 1fr 1fr;
            gap: 30px;
            margin-bottom: 30px;
        }}

   .receipt-title {{
            text-align: right;
        }}

        .receipt-title h3 {{
            color: #3498db;
            font-size: 2.2rem;
            margin-bottom: 5px;
        }}


        /* Tabla */
        .tabla-contenedor {{
            margin: 30px 0 50px 0;
            width: 100%;
        }}

        .tabla-productos {{
            width: 100%;
            border-collapse: collapse;
            border: 2px solid #333;
        }}

        .tabla-productos th {{
            background-color: #f0f0f0;
            border: 2px solid #333;
            padding: 12px 8px;
            text-align: center;
            font-size: 14px;
            font-weight: bold;
        }}

        .tabla-productos td {{
            border: 1px solid #333;
            padding: 10px 8px;
            text-align: center;
            font-size: 13px;
        }}

        .tabla-productos .col-detalle {{
            text-align: center;
            width: 70%;
            background-color: #918787;
            color:#FFFFFF;
        }}

        .tabla-productos .col-detalle2 {{
            text-align: left;
            width: 70%;
            background-color: #FFFFFF;
            color:#292626;
        }}
        .tabla-productos .col-talla {{
            width: 15%;
            background-color: #918787;
            color:#FFFFFF;
        }}

        .tabla-productos .col-talla2 {{
            width: 15%;
            background-color: #FFFFFF;
            color:#292626;
        }}
        .tabla-productos .col-cantidad {{
            width: 15%;
            background-color: #918787;
            color:#FFFFFF;
        }}

        .tabla-productos .col-cantidad2 {{
            width: 15%;
            background-color: #FFFFFF;
            color:#292626;
        }}
        /* Firmas */
        .firmas {{
            margin-top: 100px;
            padding-top: 30px;
            border-top: 1px solid #333;
        }}

        .firma-container {{
            display: flex;
            justify-content: space-between;
        }}

        .firma-col {{
            width: 45%;
        }}

        .firma-linea {{
            width: 100%;
            border-top: 1px solid #333;
            margin: 60px 0 5px 0;
        }}

        .firma-texto {{
            font-size: 12px;
            font-weight: bold;
            margin-bottom: 5px;
        }}

        .firma-nombre {{
            font-size: 11px;
            text-align: center;
            margin-top: 8px;
        }}

        /* Botón de impresión */
        .print-btn {{
            position: fixed;
            top: 20px;
            right: 20px;
            padding: 12px 24px;
            background: #2c3e50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            font-family: Arial, sans-serif;
            font-size: 14px;
            z-index: 1000;
            box-shadow: 0 2px 5px rgba(0,0,0,0.2);
        }}

        .print-btn:hover {{
            background: #1a252f;
        }}

        /* Marca de agua */
        .watermark {{
            position: fixed;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(-45deg);
            font-size: 60px;
            color: rgba(0,0,0,0.1);
            z-index: -1;
            white-space: nowrap;
            pointer-events: none;
        }}

        .receipt-title {{
            text-align: right;
        }}

          .section-title {{
            font-size: 1.2rem;
            color: #2c3e50;
            margin-bottom: 15px;
            padding-bottom: 5px;
            border-bottom: 1px solid #eee;
            font-weight: 600;
        }}

            .info-row {{
            display: flex;
            margin-bottom: 10px;
        }}

        .info-label {{
            flex: 0 0 40%;
            font-weight: 600;
            color: #555;
        }}

        .info-value {{
            flex: 1;
            color: #333;
        }}


  .receipt-container {{
            background-color: white;
            border-radius: 10px;
            box-shadow: 0 5px 20px rgba(0, 0, 0, 0.1);
            padding: 30px;
            position: relative;
            overflow: hidden;
        }}

        .receipt-header {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            padding-bottom: 20px;
            border-bottom: 2px solid #eee;
            margin-bottom: 25px;
        }}
    </style>
</head>
<body>
    <!-- Botón para imprimir -->
    <button class="print-btn no-print" onclick="window.print()">
        🖨️ Imprimir / Guardar como PDF
    </button>

    <!-- Marca de agua -->
    <div class="watermark no-print">COPIA ORIGINAL</div>

    <div class="container">
        <!-- Encabezado con información de la empresa -->


        <div class="receipt-header">
            <div class="company-name">
             <img width="120" height="90" src="{img_logo}">
                 <div class="company-info">
               Cels. 79949364 - 65070403<br>
                Av. Canal lsuto C/ Landivar Edif. Los Cedros<br>
                Santa Cruz - Bolivia
            </div>
             </div>

             <div class="receipt-title">

               <h3>BOLETA DE PAGO</h3>
                    <div class="receipt-number">Nº <strong>P-{año}-00{valor}</strong></div>
                    <div class="info-label">Fecha de Emisión:</div>{fecha_emision}
            </div>

        </div>






           <div class="receipt-body">
                <div class="section">
                    <h4 class="section-title">Detalles del pago </h4>
                    <div class="info-row">
                        <div class="info-label">Recibe:</div>
                        <div class="info-value">{pago['titular']}</div>
                    </div>

                    <div class="info-row">
                        <div class="info-label">Fecha de pago:</div>
                        <div class="info-value">{fecha_pago}</div>
                    </div>

                </div>
            </div>


        <!-- Tabla de productos -->
        <div class="tabla-contenedor">
            <table class="tabla-productos">
                <thead>
                    <tr>
                        <th class="col-detalle">DETALLE</th>
                        <th class="col-cantidad">MONTO</th>
                    </tr>
                </thead>
                <tbody>
                <tr>
                 <td class="col-detalle2">{pago['detalle']}</td>
                 <td class="col-cantidad2">{pago['monto']}</td>
                 </tr>
                </tbody>
            </table>
        </div>

        <!-- Firmas -->
        <div class="firmas">
            <div class="firma-container">
                <div class="firma-col">
                    <div class="firma-texto">ENTREGADO POR:</div>
                    <div class="firma-linea"></div>
                    <div class="firma-nombre">
                        Nombre y Firma
                    </div>
                    <div class="firma-nombre" style="font-size: 10px; margin-top: 5px;">
                        Fecha: __/__/____
                    </div>
                </div>

                <div class="firma-col">
                    <div class="firma-texto">RECIBIDO POR:</div>
                    <div class="firma-linea"></div>
                    <div class="firma-nombre">
                        Nombre y Firma del Cliente
                    </div>
                    <div class="firma-nombre" style="font-size: 10px; margin-top: 5px;">
                        Fecha: __/__/____
                    </div>
                </div>
            </div>
        </div>

        <!-- Pie de página -->
        <div style="text-align: center; font-size: 9px; color: #666; margin-top: 50px; padding-top: 10px; border-top: 1px solid #ccc;">
            Documento generado electrónicamente por Guara<br>
            Código: {valor} |
            Versión: 1.0
        </div>
    </div>

    <script>
        document.addEventListener("DOMContentLoaded", function() {{
            // Auto-llenar fecha actual si no hay datos
            // Configurar para impresión
            window.onbeforeprint = function() {{
                // Ocultar elementos no deseados al imprimir
                document.querySelectorAll(".no-print").forEach(el => {{
                    el.style.display = "none";
                }});
            }};

            window.onafterprint = function() {{
                // Restaurar elementos después de imprimir
                document.querySelectorAll(".no-print").forEach(el => {{
                    el.style.display = "";
                }});
            }};
        }});


    </script>
</body>
</html>
'''

    return HttpResponse(str_html)




#---------------------------------CATEGORIAS-----------------------------------#

def lista_categorias(request):
    tareas = listar_categorias()  # Obtener datos
    return JsonResponse({'tareas': tareas})


def ver_todas_categorias(request):
    from django.db import connections
    from django.http import JsonResponse
    
    with connections['default'].cursor() as cursor:
        cursor.execute("SELECT * FROM categorias ORDER BY id DESC LIMIT 10")
        columns = [col[0] for col in cursor.description]
        categorias = [dict(zip(columns, row)) for row in cursor.fetchall()]
    
    return JsonResponse({'categorias': categorias})

def registra_categoria(request):
    if request.method == "POST":
        tipo = int(request.POST.get("tipocategoria", 1))
        categoria_id = int(request.POST.get("categoria_id",0))
        categoriaName = request.POST.get("categoriaName", "")
        categoria_descripcion = request.POST.get("categoria_descripcion", "")
        imagen = request.FILES.get("categoria_imagen", None)
        usuario_registra = request.session.get("dpilogin", "Desconocido")
        fecha = now().strftime("%Y-%m-%d %H:%M:%S")

        adjuntos_portada = None

        if imagen:
            adjuntos_path_portada = os.path.join("biblioteca/productos", imagen.name)
            full_path = os.path.join(settings.STATICFILES_DIRS[0], adjuntos_path_portada)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "wb+") as destination:
                for chunk in imagen.chunks():
                    destination.write(chunk)
            adjuntos_portada = imagen.name

        try:
            with connections['default'].cursor() as cursor:
                if tipo == 1:
                    cursor.execute("""
                        INSERT INTO categorias
                        (nombre,detalle, imagen,estado,fecha_carga, usuario_carga)
                        VALUES (%s, %s,%s, %s, %s, %s)
                        """, [categoriaName,categoria_descripcion, adjuntos_portada,'1', fecha, usuario_registra])


                else:
                    if tipo == 2 and categoria_id:
                        if not adjuntos_portada:
                            cursor.execute("SELECT imagen FROM categorias WHERE id = %s", [categoria_id])
                            result = cursor.fetchone()
                            adjuntos_portada = result[0] if result else None

                        # ACTUALIZAR PRODUCTO EXISTENTE
                        cursor.execute("""
                        UPDATE categorias
                        SET nombre=%s,detalle=%s, imagen=%s
                        WHERE id=%s
                        """, [categoriaName,categoria_descripcion,adjuntos_portada,categoria_id])
                    else:
                        messages.error(request, "ocurrio un error al modificar")
                        return redirect("configuracion")
            messages.success(request, "Categoria guardado correctamente.")
            return redirect("configuracion")
        except Exception as e:
            messages.error(request, f"Ocurrió un error: {e}")
            return redirect("configuracion")

    return HttpResponse("Método no permitido", status=405)


def eliminar_categoria(request,valor):
 
    try:

        with connections['default'].cursor() as cursor:
            cursor.execute("""
                UPDATE categorias
                SET estado='0'
                WHERE id=%s
            """,[valor])
        respuesta="Se realizo con exito"

    except Exception as e:
            return redirect("configuracion")
    return JsonResponse({'respuesta': respuesta})

 
def editar_categoria(request,valor):
   
    categoria= buscar_categoria(valor)
    str_html = ""
    if categoria:
        if categoria['imagen']:
            img_url = static(f"biblioteca/productos/{categoria['imagen']}")
        else:
            img_url = static(f"biblioteca/marcas/nulo.jpg")

        str_html += f'''
                    <input type="hidden" id="tipocategoria" name="tipocategoria" value="2">
                     <input type="hidden" id="categoria_id" name="categoria_id" value="{categoria['id']}">


                    <div class="form-group">
                        <label for="brandName">Nombre de la Categoria *</label>
                        <input type="text"  id="categoriaName" name="categoriaName"  class="form-control" required value="{categoria['nombre']}">
                    </div>

                        <div class="form-group">
                        <label for="serviceDescription">Descripción *</label>
                        <textarea id="categoria_descripcion" name="categoria_descripcion" class="form-control" required>{categoria['detalle']}</textarea>
                    </div>
                    <div class="form-group">
                        <label for="brandLogo">Imagen</label>
                        <input type="file"  id="categoria_imagen" name="categoria_imagen" class="form-control" accept=".jpg,.jpeg,.png,image/jpeg,image/png">

                    </div>

                    <div class="form-group">
                        <label for="brandLogo">Imagen Actual</label>
                        <img src="{img_url}" alt="Producto"  style="width:25%;heigth:25%;" >

                    </div>'''

    return JsonResponse({'resultado': str_html})




 #---------------------------------PROVEEDORES-----------------------------------#

def lista_proveedor(request):
    tareas = listar_proveedores()  # Obtener datos
    return JsonResponse({'tareas': tareas})


def registra_proveedor(request):
    if request.method == "POST":
        tipo = int(request.POST.get("tipop", 0))
        proveedor_id = int(request.POST.get("proveedor_id",0))
        nombre = request.POST.get("nombrep", "")
        contacto = request.POST.get("contacto", "")
        detalle = request.POST.get("detalleP", "")
        correo = request.POST.get("correoP", "")
        celular = request.POST.get("celularP", "")
        usuario_registra = request.session.get("dpilogin", "Desconocido")
        fecha = now().strftime("%Y-%m-%d %H:%M:%S")

        try:
            with connections['default'].cursor() as cursor:
                if tipo == 1:
                    cursor.execute("""
                        INSERT INTO proveedor
                        (nombre, contacto,detalle,correo,celular,estado,fecha_carga, usuario_carga)
                        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
                        """, [nombre, contacto,detalle,correo,celular,1, fecha, usuario_registra])
                else:
                    if tipo == 2 and proveedor_id:
                        cursor.execute("""
                            UPDATE proveedor
                            SET nombre=%s,
                            contacto=%s,
                            detalle=%s,
                            correo=%s,
                            celular=%s
                            WHERE id=%s
                            """, [nombre, contacto,detalle,correo,celular,proveedor_id])
                    else:
                        messages.error(request, "ocurrio un error al modificar")
                        return redirect("configuracion")
            messages.success(request, "Proveedor guardado correctamente.")
            return redirect("configuracion")
        except Exception as e:
            messages.error(request, f"Ocurrió un error: {e}")
            return redirect("configuracion")

    return HttpResponse("Método no permitido", status=405)


def eliminar_proveedor(request,valor):

    try:

        with connections['default'].cursor() as cursor:
            cursor.execute("""
                UPDATE proveedor
                SET estado='0'
                WHERE id=%s
            """,[valor])
        respuesta="Se realizo con exito"

    except Exception as e:
            return redirect("configuracion")
    return JsonResponse({'respuesta': respuesta})


def editar_proveedor(request,valor):
    proveedor= buscar_proveedor(valor)
    str_html = ""
    if proveedor:
        str_html += f'''
                    <input type="hidden" id="tipop" name="tipop" value="2">
                     <input type="hidden" id="proveedor_id" name="proveedor_id" value="{proveedor['id']}">

                      <div class="form-group">
                        <label for="brandName">Nombre *</label>
                        <input type="text" id="nombre" name="nombre" class="form-control" required value="{proveedor['nombre']}">
                    </div>

                     <div class="form-group">
                        <label for="brandName">Contacto</label>
                        <input type="text" id="contacto" name="contacto" class="form-control" value="{proveedor['contacto']}">
                    </div>

                    <div class="form-group">
                        <label for="brandName">Detalle</label>
                        <textarea id="detalle" name="detalle" class="form-control" placeholder="Descripcion del proveedor">{proveedor['detalle']}</textarea>
                    </div>


                    <div class="form-group">
                        <label for="brandName">correo</label>
                        <input type="email" id="correo" name="correo" class="form-control" required placeholder="Ejemplo: pilandina@gmail.com" value="{proveedor['correo']}">
                    </div>


                    <div class="form-group">
                        <label for="brandName">Celular</label>
                        <input type="text" id="celular" name="celular" class="form-control" required placeholder="71325456" value="{proveedor['celular']}">
                    </div>
                    '''

    return JsonResponse({'resultado': str_html})



 #---------------------------------PRODUCTOS-----------------------------------#

def lista_productos(request):
    tareas = listar_productos()  # Obtener datos
    return JsonResponse({'tareas': tareas})


def registra_producto(request):
    if request.method == "POST":
        tipo = int(request.POST.get("tipoc", 0))
        producto_id = int(request.POST.get("producto_id",0))
        productName = request.POST.get("productName", "")
        productDescription = request.POST.get("productDescription", "")
        imagen = request.FILES.get("productIcon", None)
        usuario_registra = request.session.get("dpilogin", "Desconocido")
        fecha = now().strftime("%Y-%m-%d %H:%M:%S")

        adjuntos_portada = None

        if imagen:
            adjuntos_path_portada = os.path.join("biblioteca/productos", imagen.name)
            full_path = os.path.join(settings.STATICFILES_DIRS[0], adjuntos_path_portada)
            os.makedirs(os.path.dirname(full_path), exist_ok=True)
            with open(full_path, "wb+") as destination:
                for chunk in imagen.chunks():
                    destination.write(chunk)
            adjuntos_portada = imagen.name

        try:
            with connections['default'].cursor() as cursor:
                if tipo == 1:
                    cursor.execute("""
                        INSERT INTO productos
                        (nombre,detalle, imagen,estado,fecha_carga, usuario_carga)
                        VALUES (%s, %s,%s, %s, %s, %s)
                        """, [productName,productDescription, adjuntos_portada,1, fecha, usuario_registra])


                else:
                    if tipo == 2 and producto_id:
                        if not adjuntos_portada:
                            cursor.execute("SELECT imagen FROM productos WHERE id = %s", [producto_id])
                            result = cursor.fetchone()
                            adjuntos_portada = result[0] if result else None

                        # ACTUALIZAR PRODUCTO EXISTENTE
                        cursor.execute("""
                        UPDATE productos
                        SET nombre=%s,detalle=%s, imagen=%s
                        WHERE id=%s
                        """, [productName,productDescription,adjuntos_portada,producto_id])
                    else:
                        messages.error(request, "ocurrio un error al modificar")
                        return redirect("configuracion")
            messages.success(request, "Servicio guardado correctamente.")
            return redirect("configuracion")
        except Exception as e:
            messages.error(request, f"Ocurrió un error: {e}")
            return redirect("configuracion")

    return HttpResponse("Método no permitido", status=405)


def eliminar_producto(request,valor):

    try:

        with connections['default'].cursor() as cursor:
            cursor.execute("""
                UPDATE productos
                SET estado='0'
                WHERE id=%s
            """,[valor])
        respuesta="Se realizo con exito"

    except Exception as e:
            return redirect("configuracion")
    return JsonResponse({'respuesta': respuesta})


def editar_producto(request,valor):
    producto= buscar_producto(valor)
    str_html = ""
    if producto:
        if producto['imagen']:
            img_url = static(f"biblioteca/productos/{producto['imagen']}")
        else:
            img_url = static(f"biblioteca/marcas/nulo.jpg")

        str_html += f'''
                    <input type="hidden" id="tipoc" name="tipoc" value="2">
                     <input type="hidden" id="producto_id" name="producto_id" value="{producto['id']}">


                    <div class="form-group">
                        <label for="brandName">Nombre del Producto *</label>
                        <input type="text"  id="productName" name="productName"  class="form-control" required value="{producto['nombre']}">
                    </div>

                        <div class="form-group">
                        <label for="serviceDescription">Descripción *</label>
                        <textarea id="productDescription" name="productDescription" class="form-control" required>{producto['detalle']}</textarea>
                    </div>
                    <div class="form-group">
                        <label for="brandLogo">Imagen</label>
                        <input type="file"  id="productIcon" name="productIcon" class="form-control" accept=".jpg,.jpeg,.png,image/jpeg,image/png">

                    </div>

                    <div class="form-group">
                        <label for="brandLogo">Imagen Actual</label>
                        <img src="{img_url}" alt="Producto"  style="width:25%;heigth:25%;" >

                    </div>'''

    return JsonResponse({'resultado': str_html})


# Función auxiliar para formatear fecha en español
def formatear_fecha_espanol(fecha):
    """Formatea fecha en formato '2 DE SEPTIEMBRE DEL 2025'"""
    if not fecha:
        return ""

    # Si es string datetime de la base de datos
    if isinstance(fecha, str):
        try:
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
        except:
            return fecha

    # Diccionario de meses en español
    meses = {
        1: "ENERO", 2: "FEBRERO", 3: "MARZO", 4: "ABRIL",
        5: "MAYO", 6: "JUNIO", 7: "JULIO", 8: "AGOSTO",
        9: "SEPTIEMBRE", 10: "OCTUBRE", 11: "NOVIEMBRE", 12: "DICIEMBRE"
    }

    try:
        dia = fecha.day
        mes = meses.get(fecha.month, "")
        año = fecha.year
        return f"{dia} DE {mes} DEL {año}"
    except:
        return str(fecha)


def obtener_año(fecha):
    """Formatea fecha en formato '2 DE SEPTIEMBRE DEL 2025'"""
    if not fecha:
        return ""

    # Si es string datetime de la base de datos
    if isinstance(fecha, str):
        try:
            fecha = datetime.strptime(fecha, "%Y-%m-%d")
        except:
            return fecha

    try:
        año = fecha.year
        return año
    except:
        return str(fecha)

def tienda(request):
    return render(request, "home/tienda.html")

#---------------------------------- DETALLES ---------------------------------------------#

def detalle_cotizacion(request,valor):
    dato = int(base64.b64decode(valor).decode("utf-8"))
    context = {
        'id_auto':dato
        }

    html_template = loader.get_template('home/detalle.html')
    return HttpResponse(html_template.render(context, request))





def mostrar_detalle(request,valor):
    str_html = ""
    cotizacion = buscar_cotizacion(valor)
    str_html += f'''

    <!-- Timeline -->
    <div class="timeline-container fade-in-up" style="animation-delay: 0.2s">
            <div class="timeline-header">

                        <div class="card">
            <div class="card-header">
                <h2>📊 Detalles de Cotización  CTG{valor}</h2>
                <span class="badge" id="selectedQuoteStatus"></span>
                </div>
                <div>
                <p><strong>Prospecto:</strong> {cotizacion['prospecto']}</p>
                <p><strong>Fecha:</strong> {cotizacion['fecha']}</p>
                <p><strong>Detalles:</strong> {cotizacion['detalle']}</p>
                <p><strong>Cantidad:</strong> {cotizacion['cantidad']}</p>
                <p><strong>Monto Total:</strong>{cotizacion['monto']}</p>
                <p><strong>Entrega:</strong> {cotizacion['entrega']}</p>
                <p><strong>Cliente:</strong> {cotizacion['ncliente']}</p>

                <h3 style="margin: 20px 0 10px 0;">Historial de Pagos</h3>
                <div class="payment-details">'''
    cliente = cotizacion['cliente']
    pagos = revisar_pagos(cliente,valor)
    if pagos:
        for pago in pagos:
            str_html += f'''<div class="payment-item">
                        <div class="payment-info">
                            <span class="payment-date">{pago['fecha']}</span>
                            <span class="payment-amount">{pago['cuenta']}</span>
                            <span>{pago['metodo']}</span>
                        </div>
                    </div>'''
    else:
        str_html += f'''<p>No hay pagos registrados</p>'''

    str_html += f'''</div>

                </div>
                </div>
                </br>
                </br>
        <h2><i class="fas fa-stream"></i> Historial de la cotización</h2>
                        <div class="timeline-controls">
                            <a data="{valor}" class="control-btn" id="agrega_comentario" name="agrega_comentario">
                                <i class="fa-solid fa-comment-dots" style="color:blue;"></i> Notas
                            </a>
                            <a class="control-btn"  data="{valor}" id="agrega_material" name="agrega_material">
                                <i class="fa-solid fa-cloud-arrow-up" style="color:blue;"></i> Adjuntos
                            </a>

                            <a class="control-btn"  data="{valor}" id="firmar_contrato" name="firmar_contrato">
                                <i class="fas fa-handshake" style="color:green;"></i> Concretar
                            </a>

                              <a class="control-btn"  data="{valor}" id="gastos_cotizacion" name="gastos_cotizacion">
                                <i class="fas fa-cart-shopping" style="color:red;"></i> Registrar gastos
                            </a>
                        </div>
            </div>

        <div class="timeline-content">

            '''
    detalles = revisar_detalles_cotizacion(valor)
    if detalles:
        for detalle in detalles:
            clase=""
            if detalle['tipo'] == 1:
                clase+= f'''<div class="timeline-item en-proceso" >
                                    <div class="timeline-marker">
                                        <div class="timeline-dot"></div>
                                        <div class="timeline-date">
                                            <div>{detalle['fecha_carga']}</div>

                                        </div>
                                    </div>
                                    <div class="timeline-content-card">
                                        <div class="timeline-title">
                                            <span>Nota</span>

                                        </div>
                                        <div class="timeline-description">
                                            <textarea class="vercomentarea">{detalle['detalle']}</textarea>
                                        </div>
                                        <div class="timeline-meta">
                                            <div class="meta-item">
                                                <i class="fas fa-user-tie"></i>
                                                <span>{detalle['nombre']}</span>
                                                <a  data="{detalle['id']}" href="#" id="eliminar_adjuntos" title="Eliminar">
                                                <i class="fas fa-trash" style="color:red;"></i>
                                                </a>
                                            </div>

                                        </div>
                                    </div>
                                </div>'''
            else:
                if detalle['tipo'] == 2:
                    clase+= f'''<div class="timeline-item pendiente">
                                        <div class="timeline-marker">
                                            <div class="timeline-dot"></div>
                                            <div class="timeline-date">

                                                <div class="timeline-time">{detalle['fecha_carga']}</div>
                                            </div>
                                        </div>
                                        <div class="timeline-content-card">
                                            <div class="timeline-title">
                                                <span>Material Adjunto</span>

                                            </div>
                                            <div class="timeline-description">
                                             <a href="https://www.guara.com.bo/static/biblioteca/adjuntos/{detalle['adjunto']}" target="_blank"  title="Archivo adjunto">{detalle['adjunto']}</a>
                                            </div>
                                            <div class="timeline-meta">
                                                <div class="meta-item">
                                                    <i class="fas fa-signature"></i>
                                                    <span> {detalle['nombre']}</span>
                                                     <a  data="{detalle['id']}" href="#" id="eliminar_adjuntos" title="Eliminar">
                                                <i class="fas fa-trash" style="color:red;"></i>
                                                </a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>'''

            str_html += f''' {clase}'''


    gastos = revisar_pagos_cotizacion(valor)
    if gastos:
        for gasto in gastos:
            str_html += f'''<div class="timeline-item pendiente">
                                        <div class="timeline-marker">
                                            <div class="timeline-dot"></div>
                                            <div class="timeline-date">

                                                <div class="timeline-time">{gasto['fecha_carga']}</div>
                                            </div>
                                        </div>
                                        <div class="timeline-content-card">
                                            <div class="timeline-title">
                                                <span>{gasto['titular']}</span>

                                            </div>
                                            <div class="timeline-description">
                                             <a href="https://www.guara.com.bo/static/biblioteca/pagos/{gasto['respaldo']}" target="_blank"  title="Archivo adjunto">{gasto['respaldo']}</a>
                                              <textarea class="vercomentarea">{gasto['detalle']}</textarea>
                                              <hr>
                                              Gastos: {gasto['monto']} Bs.
                                            </div>
                                            <div class="timeline-meta">
                                                <div class="meta-item">
                                                    <i class="fas fa-signature"></i>
                                                    <span> {gasto['nombre']}</span>
                                                     <a  data="{gasto['id']}" href="#" id="eliminar_gastos" name="eliminar_gastos" title="Eliminar">
                                                <i class="fas fa-trash" style="color:red;"></i>
                                                </a>
                                                </div>
                                            </div>
                                        </div>
                                    </div>'''
    str_html += f'''</div>
    </div>
        </div>'''

    return JsonResponse({'respuesta': str_html})



def comentarios_cotizacion(request,valor):
    str_html = ""
    str_html += f'''
             <div class="contenido">
                        <input type="hidden" id="id_auto" name="id_auto" value="{valor}">
                        <input type="hidden" id="modalidad" name="modalidad" value="1">
                           <section class="users-section">
                                <div class="section-header">
                                  <h4 style="color:#1A0600;"> <i class="fa-solid fa-envelopes-bulk"></i> AÑADIR COMENTARIOS</h4>
                                </div>
                                <div>
                                <textarea id="comentarea" name="comentarea"></textarea>
                                </div>

            </div>

                                <center>
                                    <button type="submit" class="btn btn-info">Grabar</button>
                                    <button type="button" class="btn btn-success" id="cancel-btn-comentarios">Cerrar</button>
                                    </center>
                        '''

    return JsonResponse({'respuesta': str_html})



def adjuntos_cotizacion(request,valor):
    str_html = ""
    str_html += f'''
             <div class="contenido">
                        <input type="hidden" id="id_auto" name="id_auto" value="{valor}">
                        <input type="hidden" id="modalidad" name="modalidad" value="2">
                           <section class="users-section">
                                <div class="section-header">
                                  <h4 style="color:#1A0600;"> <i class="fa-solid fa-envelopes-bulk"></i> AÑADIR ADJUNTOS</h4>
                                </div>
                                <center>
                                <div class="custom-file-upload">
                                <input type="file" id="fileInput" name="fileInput" class="file-input" hidden>
                                <label for="fileInput" class="upload-label">
                                    <i class="fas fa-cloud-upload-alt"></i>
                                    <span>Subir archivo</span>
                                </label>
                               <span class="file-name" id="fileName">No se ha seleccionado ningún archivo</span>
                            </div>
                            </center>

            </div>

                                <center>
                                    <button type="submit" class="btn btn-info">Grabar</button>
                                    <button type="button" class="btn btn-success" id="cancel-btn-comentarios">Cerrar</button>
                                    </center>
                        '''

    return JsonResponse({'respuesta': str_html})


def revertir_contrato(request,valor):

    try:

        with connections['default'].cursor() as cursor:
            cursor.execute("""
                UPDATE cotizaciones
                SET cliente="", ncliente="",
                estado = '1'
                WHERE id=%s
            """,[valor])
        respuesta="Se realizo con exito"

    except Exception as e:
            return redirect("configuracion")
    return JsonResponse({'respuesta': respuesta})


def firmar_contrato(request,valor):
    str_html = ""
    str_html += f'''
             <div class="contenido">
                        <input type="hidden" id="id_auto" name="id_auto" value="{valor}">
                        <input type="hidden" id="modalidad" name="modalidad" value="3">
                           <section class="users-section">
                                <div class="section-header">
                                  <h4 style="color:#1A0600;"> <i class="fa-solid fa-envelopes-bulk"></i> CONCRETAR CONTRATO</h4>
                                </div>
                                <center>
                                 <div class="form-group">
                                 <label for="serviceTitle">Cliente</label>
                                <select id="clientecontrato" name="clientecontrato" class="form-control" required>'''
    clientes = listar_clientes()
    for cliente in clientes:
        str_html += f'''<option value="{cliente['id']}+{cliente['nombre']}">{cliente['nombre']}</option>'''

    str_html += f'''</select>
                    </div>
                            </center>

            </div>

                                <center>
                                    <button type="submit" class="btn btn-info">Grabar</button>
                                    <a class="btn btn-success" id="cancel-btn-comentarios">Cerrar</a>
                                    <a class="btn btn-info" data="{valor}" id="revertir_contrato" name="revertir_contrato">Revertir</a>
                                    </center>
                        '''

    return JsonResponse({'respuesta': str_html})


def eliminar_adjuntos(request,valor):

    try:

        with connections['default'].cursor() as cursor:
            cursor.execute("""
                UPDATE detalle_cotizaciones
                SET estado='0'
                WHERE id=%s
            """,[valor])
        respuesta="Se realizo con exito"

    except Exception as e:
            return redirect("configuracion")
    return JsonResponse({'respuesta': respuesta})

def codificar_id(id_numero):
    """Convierte un ID numérico a string base64"""
    id_str = str(id_numero)
    id_bytes = id_str.encode('utf-8')
    id_base64 = base64.b64encode(id_bytes).decode('utf-8')
    return id_base64

def agregar_interaccion(request):
    if request.method == "POST":
        usuario_registra = request.session.get("dpilogin", "Desconocido")
        fecha = now().strftime("%Y-%m-%d %H:%M:%S")
        id_auto = request.POST.get("id_auto", 0)
        comentarea = request.POST.get("comentarea", "")
        modalidad = int(request.POST.get('modalidad'))
        clientecontrato = request.POST.get('clientecontrato')
        fileInput = request.FILES.get("fileInput", None)

        adjuntos_portada = None
                        # Manejar archivo si existe para esta fila
        if fileInput:
            if fileInput.name:  # Verificar que tenga nombre
                # Generar nombre único para evitar conflictos
                nombre_original = fileInput.name
                nombre_base, extension = os.path.splitext(nombre_original)
                nombre_unico = f"{nombre_base}_{uuid.uuid4().hex[:8]}{extension}"

                # Ruta relativa y absoluta
                adjuntos_path_portada = os.path.join("biblioteca/adjuntos/", nombre_unico)
                full_path = os.path.join(settings.STATICFILES_DIRS[0], adjuntos_path_portada)

                # Crear directorio si no existe
                os.makedirs(os.path.dirname(full_path), exist_ok=True)
                # Guardar archivo
                with open(full_path, "wb+") as destination:
                    for chunk in fileInput.chunks():
                        destination.write(chunk)

                adjuntos_portada = nombre_unico

        try:
            # Conectar con la BD e insertar datos
           with connections['default'].cursor() as cursor:
                if modalidad == 1:
                    cursor.execute("""
                        INSERT INTO detalle_cotizaciones
                        (cotizacion,usuario_carga,fecha_carga,estado,detalle,tipo)
                        VALUES (%s,%s, %s, %s, %s,%s)
                        """, [id_auto,usuario_registra,fecha,1,comentarea,modalidad])
                else:
                    if modalidad == 2:
                        cursor.execute("""
                            INSERT INTO detalle_cotizaciones
                            (cotizacion,usuario_carga,fecha_carga,estado,adjunto,tipo)
                            VALUES (%s,%s, %s, %s, %s,%s)
                            """, [id_auto,usuario_registra,fecha,1,adjuntos_portada,modalidad])
                    else:
                        id_cliente,ncliente = clientecontrato.split("+")
                        cursor.execute("""
                            UPDATE cotizaciones
                            SET cliente=%s, ncliente=%s,
                            estado = '2'
                            WHERE id=%s
                            """, [id_cliente,ncliente,id_auto])
                messages.success(request, "Realizado con Exito.")

                id_codificado = codificar_id(id_auto)

                url_detalle = f"https://www.guara.com.bo/configuracion/detalle_cotizacion/{id_codificado}/"

                return HttpResponseRedirect(url_detalle)


        except Exception as e:
            messages.error(request, f"Error al guardar: {str(e)}")
            return redirect("configuracion")
    return HttpResponse("Método no permitido", status=405)



#---------------------------------- DASHBOARD ---------------------------------------------#



from django.db import connections
from datetime import datetime, timedelta
from django.http import JsonResponse

def grafico(request):
    # Definir período (últimos 360 días)
    fecha_inicio = datetime.now() - timedelta(days=360)
    
    with connections['default'].cursor() as cursor:
        # Obtener ingresos agrupados por mes (SQLite)
        cursor.execute("""
            SELECT 
                strftime('%Y-%m', fecha) as mes,
                SUM(cuenta) as total_ingresos
            FROM recibos
            WHERE fecha >= ? AND estado = '1'
            GROUP BY strftime('%Y-%m', fecha)
            ORDER BY mes
        """, [fecha_inicio.strftime('%Y-%m-%d %H:%M:%S')])
        
        ingresos = cursor.fetchall()
        ingresos_dict = {row[0]: float(row[1]) for row in ingresos}
        
        # Obtener egresos agrupados por mes (SQLite)
        cursor.execute("""
            SELECT 
                strftime('%Y-%m', fecha) as mes,
                SUM(monto) as total_egresos
            FROM egresos
            WHERE fecha >= ? AND estado = '1'
            GROUP BY strftime('%Y-%m', fecha)
            ORDER BY mes
        """, [fecha_inicio.strftime('%Y-%m-%d %H:%M:%S')])
        
        egresos = cursor.fetchall()
        egresos_dict = {row[0]: float(row[1]) for row in egresos}
        
        # Combinar todos los meses únicos
        todos_meses = sorted(set(list(ingresos_dict.keys()) + list(egresos_dict.keys())))
        
        # Preparar datos para el gráfico
        datos_grafico = {
            'meses': todos_meses,
            'ingresos': [ingresos_dict.get(mes, 0) for mes in todos_meses],
            'egresos': [egresos_dict.get(mes, 0) for mes in todos_meses]
        }
        
        return JsonResponse(datos_grafico)


def grafico_reporte(request,valor):
    inicio,fin = valor.split("+")
    with connection.cursor() as cursor:
        # Obtener ingresos agrupados por mes
        cursor.execute("""
            SELECT
                DATE_FORMAT(fecha, '%%Y-%%m') as mes,
                SUM(cuenta) as total_ingresos
            FROM recibos
            WHERE fecha BETWEEN %s AND %s
            and estado='1'
            GROUP BY DATE_FORMAT(fecha, '%%Y-%%m')
            ORDER BY mes
        """, [inicio,fin])

        ingresos = cursor.fetchall()
        ingresos_dict = {row[0]: float(row[1]) for row in ingresos}

        # Obtener egresos agrupados por mes
        cursor.execute("""
            SELECT
                DATE_FORMAT(fecha, '%%Y-%%m') as mes,
                SUM(monto) as total_egresos
            FROM egresos
            WHERE fecha BETWEEN %s AND %s
            and estado='1'
            GROUP BY DATE_FORMAT(fecha, '%%Y-%%m')
            ORDER BY mes
        """, [inicio,fin])

        egresos = cursor.fetchall()
        egresos_dict = {row[0]: float(row[1]) for row in egresos}

        # Combinar todos los meses únicos
        todos_meses = sorted(set(list(ingresos_dict.keys()) + list(egresos_dict.keys())))

        # Preparar datos para el gráfico
        datos_grafico = {
            'meses': todos_meses,
            'ingresos': [ingresos_dict.get(mes, 0) for mes in todos_meses],
            'egresos': [egresos_dict.get(mes, 0) for mes in todos_meses]
        }

        return JsonResponse(datos_grafico)


def grafico2(request):
    fecha_inicio = datetime.now() - timedelta(days=360)
    with connections['default'].cursor() as cursor:
        cursor.execute("""SELECT
                        p.nombre as clientes,
                        (SELECT SUM(o.cuenta) FROM recibos o
                        WHERE o.estado='1' and o.fecha >= %s and o.cliente=p.id) AS ventasm
                    FROM clientes p
                    WHERE p.estado = '1'
                    GROUP BY p.nombre;
        """,[fecha_inicio])
        results = cursor.fetchall()

    #Convertir a listas para Chart.js
    labels = []
    ventas = []

    for row in results:
        clientes, ventasm = row
        labels.append(clientes)
        ventas.append(float(ventasm) if ventasm is not None else 0)


    return JsonResponse({
        'labels': labels,
        'ventas': ventas
    })

def grafico2_reporte(request, valor):
    inicio,fin = valor.split("+")
    with connections['default'].cursor() as cursor:
        cursor.execute("""SELECT
                        p.nombre as clientes,
                        (SELECT SUM(o.cuenta) FROM recibos o
                        WHERE o.estado='1' and o.fecha  BETWEEN %s AND %s and o.cliente=p.id) AS ventasm
                    FROM clientes p
                    WHERE p.estado = '1'
                    GROUP BY p.nombre;
        """,[inicio,fin])
        results = cursor.fetchall()

    #Convertir a listas para Chart.js
    labels = []
    ventas = []

    for row in results:
        clientes, ventasm = row
        labels.append(clientes)
        ventas.append(float(ventasm) if ventasm is not None else 0)


    return JsonResponse({
        'labels': labels,
        'ventas': ventas
    })
