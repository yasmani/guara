
from django.urls import path, re_path
from app import views





urlpatterns = [

    path('configuracion', views.configuracion, name="configuracion"),

     #---------------------------------MARCAS-----------------------------------#
    path('configuracion/lista_marcas/', views.lista_marcas, name="lista_marcas"),
    path('registra_marca/', views.registra_marca, name='registra_marca'),
    path('configuracion/editar_marca/<int:valor>/', views.editar_marca, name='editar_marca'),
    path('configuracion/eliminar_marca/<int:valor>/', views.eliminar_marca, name='eliminar_marca'),

     #---------------------------------SERVICIOS-----------------------------------#
    path('configuracion/lista_servicios/', views.lista_servicios, name="lista_servicios"),
    path('registra_servicio/', views.registra_servicio, name='registra_servicio'),
    path('configuracion/editar_servicio/<int:valor>/', views.editar_servicio, name='editar_servicio'),
    path('configuracion/eliminar_servicio/<int:valor>/', views.eliminar_servicio, name='eliminar_servicio'),

      #---------------------------------CLIENTES-----------------------------------#
    path('configuracion/lista_clientes/', views.lista_clientes, name="lista_clientes"),
    path('registra_cliente/', views.registra_cliente, name='registra_cliente'),
    path('configuracion/editar_cliente/<int:valor>/', views.editar_cliente, name='editar_cliente'),
    path('configuracion/eliminar_cliente/<int:valor>/', views.eliminar_cliente, name='eliminar_cliente'),

     #---------------------------------USUARIOS-----------------------------------#
    path('configuracion/lista_usuarios/', views.lista_usuarios, name="lista_usuarios"),
    path('registra_usuarios/', views.registra_usuarios, name='registra_usuarios'),
    path('configuracion/editar_usuario/<int:valor>/', views.editar_usuario, name='editar_usuario'),
    path('configuracion/eliminar_usuario/<int:valor>/', views.eliminar_usuario, name='eliminar_usuario'),

    #---------------------------------NOTAS-----------------------------------#
    path('configuracion/lista_notas/', views.lista_notas, name="lista_notas"),
    path('registra_nota/', views.registra_nota, name='registra_nota'),
    path('configuracion/ver_nota/<int:valor>/', views.ver_nota, name='ver_nota'),
    path('configuracion/editar_nota/<int:valor>/', views.editar_nota, name='editar_nota'),
    path('configuracion/eliminar_nota/<int:valor>/', views.eliminar_nota, name='eliminar_nota'),

    #---------------------------------RECIBOS-----------------------------------#
    path('configuracion/lista_recibos/', views.lista_recibos, name="lista_recibos"),
    path('registra_recibo/', views.registra_recibo, name='registra_recibo'),
    path('configuracion/ver_recibo/<int:valor>/', views.ver_recibo, name='ver_recibo'),
    path('configuracion/editar_recibo/<int:valor>/', views.editar_recibo, name='editar_recibo'),
    path('configuracion/revisar_saldo/<int:valor>/', views.revisar_saldo, name='revisar_saldo'),
    path('configuracion/revisar_saldo_cotizacion/<str:valor>/', views.revisar_saldo_cotizacion, name='revisar_saldo_cotizacion'),
    path('configuracion/eliminar_recibo/<int:valor>/', views.eliminar_recibo, name='eliminar_recibo'),


    #---------------------------------PAGOS-----------------------------------#
    path('configuracion/lista_pagos/', views.lista_pagos, name="lista_pagos"),
    path('registra_pago/', views.registra_pago, name='registra_pago'),
    path('configuracion/ver_pago/<int:valor>/', views.ver_pago, name='ver_pago'),
    path('configuracion/editar_pago/<int:valor>/', views.editar_pago, name='editar_pago'),
    path('configuracion/eliminar_pago/<int:valor>/', views.eliminar_pago, name='eliminar_pago'),


    #---------------------------------COTIZACION-----------------------------------#
    path('configuracion/lista_cotizaciones/', views.lista_cotizaciones, name="lista_cotizaciones"),
    path('registra_cotizacion/', views.registra_cotizacion, name='registra_cotizacion'),
    path('configuracion/ver_cotizacion/<str:valor>/', views.ver_cotizacion, name='ver_cotizacion'),
    path('configuracion/editar_cotizacion/<int:valor>/', views.editar_cotizacion, name='editar_cotizacion'),
    path('configuracion/eliminar_cotizacion/<int:valor>/', views.eliminar_cotizacion, name='eliminar_cotizacion'),


     #---------------------------------CATEGORIAS-----------------------------------#
    path('configuracion/lista_categorias/', views.lista_categorias, name="lista_categorias"),
    path('configuracion/ver_todas_categorias/', views.ver_todas_categorias, name="ver_todas_categorias"),
    path('registra_categoria/', views.registra_categoria, name='registra_categoria'),
    path('configuracion/editar_categoria/<int:valor>/', views.editar_categoria, name='editar_categoria'),
    path('configuracion/eliminar_categoria/<int:valor>/', views.eliminar_categoria, name='eliminar_categoria'),

    #---------------------------------PRODUCTOS-----------------------------------#
    path('configuracion/lista_productos/', views.lista_productos, name="lista_productos"),
    path('registra_producto/', views.registra_producto, name='registra_producto'),
    path('configuracion/editar_producto/<int:valor>/', views.editar_producto, name='editar_producto'),
    path('configuracion/eliminar_producto/<int:valor>/', views.eliminar_producto, name='eliminar_producto'),


    #---------------------------------PROVEEDOR-----------------------------------#
    path('configuracion/lista_proveedor/', views.lista_proveedor, name="lista_proveedor"),
    path('registra_proveedor/', views.registra_proveedor, name='registra_proveedor'),
    path('configuracion/editar_proveedor/<int:valor>/', views.editar_proveedor, name='editar_proveedor'),
    path('configuracion/eliminar_proveedor/<int:valor>/', views.eliminar_proveedor, name='eliminar_proveedor'),


    #------------------------------ DETALLE -----------------------------------------#
    path('configuracion/detalle_cotizacion/<str:valor>/', views.detalle_cotizacion, name='detalle_cotizacion'),
    path('configuracion/mostrar_detalle/<int:valor>/', views.mostrar_detalle, name='mostrar_detalle'),
    path('agregar_interaccion/', views.agregar_interaccion, name='agregar_interaccion'),
    path('configuracion/detalle_cotizacion/comentarios_cotizacion/<int:valor>/', views.comentarios_cotizacion, name='comentarios_cotizacion'),
    path('configuracion/detalle_cotizacion/adjuntos_cotizacion/<int:valor>/', views.adjuntos_cotizacion, name='adjuntos_cotizacion'),
    path('configuracion/detalle_cotizacion/firmar_contrato/<int:valor>/', views.firmar_contrato, name='firmar_contrato'),
    path('configuracion/detalle_cotizacion/revertir_contrato/<int:valor>/', views.revertir_contrato, name='revertir_contrato'),
    path('configuracion/detalle_cotizacion/eliminar_adjuntos/<int:valor>/', views.eliminar_adjuntos, name='eliminar_adjuntos'),


    #------------------------------ DASHBOARD -----------------------------------------#
    path('configuracion/grafico/', views.grafico, name="grafico"),
    path('configuracion/grafico_reporte/<str:valor>/', views.grafico_reporte, name='grafico_reporte'),
    path('configuracion/grafico2/', views.grafico2, name="grafico2"),
    path('configuracion/grafico2_reporte/<str:valor>/', views.grafico2_reporte, name='grafico2_reporte'),

    #------------------------------ TIENDA -----------------------------------------#
    path('tienda', views.tienda, name="tienda"),


    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
