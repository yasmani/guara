
from django.shortcuts import render, redirect
from django.db import connections
from .models import  listar_marcas,listar_servicios,listar_categorias,primer_categoria,buscar_categoria
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.http import require_POST
from urllib.parse import quote
from datetime import datetime
from django.utils.timezone import now
import json


def inicio_view(request):
    #marcas=listar_marcas()
    #servicios = listar_servicios()
    #categorias = listar_categorias()
    #primeras = primer_categoria()
    #return render(request, "accounts/login.html",{'marcas':marcas,'servicios':servicios,'categorias':categorias,'primeras':primeras})
    return render(request, "accounts/login.html")

def login_view(request):
    return render(request, "accounts/sesion.html")


def ingresar_guara(request):
    msg = None
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")


        with connections["default"].cursor() as cursor:
           cursor.execute("""
              SELECT u.id as dpilogin,
                    u.nombre as nombre,
                    u.username as username,
                    u.cargo as cargo
                   FROM home_usuarios u
                WHERE u.username = %s AND u.password = %s
                and u.estado=1
            """, [username, password])
           user = cursor.fetchone()  # Obtiene el primer resultado


        if user:
            # Guardar datos en la sesión
            request.session["dpilogin"] = user[0]
            request.session["nombre"] = user[1]
            request.session["username"] = user[2]
            request.session["cargo"] = user[3]



            return redirect("configuracion")
            # Lista de cargos permitidos
         #   cargos_permitidos = {63, 67, 82, 90, 112}  # Usamos un conjunto para mejor rendimiento

          #  if user[5] in cargos_permitidos:
           #     return redirect("home")  # Redirige si el cargo es válido
          #  else:
           #     msg = "Acceso no autorizado"
        else:
            msg = "Usuario o contraseña incorrectos"
            

    return render(request, "accounts/sesion.html", {"msg": msg})


@require_POST
@csrf_exempt
def ver_categoria(request):
    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            categoria_id = data.get('categoria_id')
            categoria = buscar_categoria(categoria_id)
            response_data = {
                        'success': True,
                        'nombre': categoria['nombre'],
                        'detalle': categoria['detalle'],
                        'imagen_url': f"/static/biblioteca/productos/{categoria['imagen']}",
            }

            return JsonResponse(response_data)
        except Exception as e:
                return JsonResponse({
                    'success': False,
                    'error': f'Error procesando la solicitud: {str(e)}'
                })

    return JsonResponse({'success': False, 'error': 'Método no permitido'})


@csrf_exempt
def enviar_whatsapp_directo(request):

    if request.method == 'POST':
        try:
            # Obtener datos (compatible con FormData y JSON)
            if request.content_type == 'application/json':
                data = json.loads(request.body)
                nombre = data.get('nombre', '').strip()
                correo = data.get('correo', '').strip()
                asunto = data.get('asunto', '').strip()
                telefono_cliente = data.get('telefono', '').strip()
                detalle = data.get('detalle', '').strip()
            else:
                nombre = request.POST.get('nombre', '').strip()
                correo = request.POST.get('correo', '').strip()
                asunto = request.POST.get('asunto', '').strip()
                telefono_cliente = request.POST.get('telefono', '').strip()
                detalle = request.POST.get('detalle', '').strip()

            # Validar
            if not all([nombre, correo, telefono_cliente, detalle]):
                return JsonResponse({
                    'success': False,
                    'error': 'Por favor complete todos los campos marcados con *'
                })


            tu_numero = "59179949364"

            # Crear mensaje profesional
            fecha_hora = now().strftime('%d/%m/%Y %H:%M')
            referencia = f"SOL-{datetime.now().strftime('%Y%m%d%H%M%S')}"

            mensaje = f"""📋 *NUEVA SOLICITUD - GUARA*

*INFORMACIÓN DEL CLIENTE*
👤 *Nombre:* {nombre}
📧 *Correo:* {correo}
📞 *Teléfono:* {telefono_cliente}
🏷️ *Asunto:* {asunto}

*DETALLE DEL REQUERIMIENTO*
{detalle}

*DATOS DE LA SOLICITUD*
📅 *Fecha y hora:* {fecha_hora}
🔢 *Referencia:* {referencia}
📊 *Tipo:* Cotización
👔 *Producto:* {asunto}

*ACCIONES SUGERIDAS*
1. Contactar al cliente en 24h
2. Enviar catálogo de productos
3. Cotizar según requerimientos

────────────────────
🏭 *Guara*
📞 79949364 - 65070403
🌐 https://www.guara.com.bo/
✉️ guara.corp@gmail.com"""

            # Codificar para URL
            mensaje_codificado = quote(mensaje)

            # Crear enlace de WhatsApp
            enlace_whatsapp = f"https://wa.me/{tu_numero}?text={mensaje_codificado}"

            # También crear confirmación para el cliente (opcional)
            confirmacion_cliente = f"""¡Hola {nombre}! 👋

✅ *Solicitud recibida correctamente*
🔢 *Referencia:* {referencia}
📋 *Asunto:* {asunto}
⏰ *Fecha:* {fecha_hora}

Nuestro equipo de ventas se contactará contigo en las próximas 24 horas hábiles.

Gracias por preferir *Guara* 🏭

Para consultas inmediatas:
📧 guara.corp@gmail.com
📞 (+591) 79949364 - (+591) 65070403"""

            enlace_confirmacion = f"https://wa.me/{telefono_cliente}?text={quote(confirmacion_cliente)}"

            return JsonResponse({
                'success': True,
                'whatsapp_link': enlace_whatsapp,
                'client_confirm_link': enlace_confirmacion,
                'reference': referencia,
                'message': 'El mensaje está listo para enviar por WhatsApp',
                'instructions': 'Haz clic en "Abrir WhatsApp" para enviar la solicitud'
            })

        except Exception as e:
            return JsonResponse({
                'success': False,
                'error': f'Error procesando la solicitud: {str(e)}'
            })

    return JsonResponse({'success': False, 'error': 'Método no permitido'})



def logout_view(request):
    request.session.flush()  # Elimina todas las variables de sesión
    return redirect("inicio")  # Redirige al login después de cerrar sesión

