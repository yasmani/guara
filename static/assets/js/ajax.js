
let host = "https://www.guara.com.bo";



$(document).ready(function () {




$(document).on("click", "#btn_captura_reportes", function () {
    downloadCanvas('graficas_guara.png');
});


/***************************** MARCAS **************************************************/
   $(document).on("click", "#brands", function () {

          $(".admin-section").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria
 $(".botones").removeClass("active");
    // Luego agrega la clase 'active' solo al botón clickeado
    $("#brands_tabla").addClass("active");
     $("#brands").addClass("active");



        listar_marcas();

    });




   $(document).on("click", "#closeBrandModal", function () {

          $("#brandModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });


   $(document).on("click", "#cancelBrandBtn", function () {

           $("#brandModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });




        function listar_marcas(){


            var contador=1;
              return $.ajax({
                url: host + "/configuracion/lista_marcas/",
                method: "GET",
                dataType: "json",
                success: function (response) {
                    let content = "";

                    response.tareas.forEach((tarea) => {

                         content += `
                         <tr>
                            <td>${contador}</td>
                    <td><strong>${tarea.nombre}</strong></td>
                    <td>
                        <div style="width: 150px; height: 60px; display: flex; align-items: center; justify-content: center; background-color: #f8f9fa; border-radius: 4px;">
                            <img src="https://www.guara.com.bo/static/biblioteca/marcas/${tarea.imagen}" title="${tarea.nombre}" style="max-width: 120px; max-height: 40px;">
                        </div>
                    </td>
                    <td>
                        <div class="actions">
                            <a class="action-btn edit-btn edit-brand" data="${tarea.id}" id="editar_marca">
                                <i class="fas fa-edit"></i> Editar
                            </a>
                            <a class="action-btn delete-btn delete-brand" data="${tarea.id}" id="eliminar_marca">
                                <i class="fas fa-trash"></i> Eliminar
                            </a>
                        </div>
                    </td>
                    </tr>
                `;
                 contador++;


                    });

                    $("#brandsTableBody").html(content);


                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });



        }



  $(document).on("click", "#addBrandBtn", function () {



                 $("#brandModalTitle").html("Agregar Nueva Marca");
                $("#brandModal").addClass("active");


    });




      $(document).on("click", "#editar_marca", function () {

            let valor = $(this).attr("data");

        return $.ajax({
                url: host + "/configuracion/editar_marca/"+valor + "/",
                method: "GET",
                dataType: "json",
                success: function (response) {

                     $("#brandModalTitle").text("Editar Marca");
                     $("#body_marca").html(response.resultado);
                     $("#brandModal").addClass("active");

                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });




    });







$(document).on("click", "#eliminar_marca", function () {

        let valor = $(this).attr("data");


        Swal.fire({
            title: "¿Estás seguro de eliminar la marca?",
            text: "Esta acción no se puede deshacer.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#d33",
            cancelButtonColor: "#3085d6",
            confirmButtonText: "Sí, eliminar",
            cancelButtonText: "Cancelar"
        }).then((result) => {
            if (result.isConfirmed) {

               return $.ajax({
                    url: host + "/configuracion/eliminar_marca/" + valor + "/",
                    method: "GET",
                    dataType: "json",
                    success: function (response) {
                        Swal.fire({
                            title: "Eliminado",
                            text: "La marca ha sido eliminada correctamente.",
                            icon: "success",
                            confirmButtonColor: "#3085d6",
                            confirmButtonText: "OK"
                        }).then(() => {
                            location.reload(); // Recargar la página o actualizar la tabla
                        });
                    },
                    error: function (xhr, status, error) {
                        Swal.fire({
                            title: "Error",
                            text: "Hubo un problema al eliminar la marca.",
                            icon: "error",
                            confirmButtonColor: "#d33",
                            confirmButtonText: "Cerrar"
                        });
                    }
                });
            }
        });


        });



/***************************************** SERVICIOS *********************************************/



 $(document).on("click", "#addServiceBtn", function () {



                 $("#serviceModalTitle").html("Agregar Nueva Marca");
                $("#serviceModal").addClass("active");


    });

   $(document).on("click", "#services", function () {

          $(".admin-section").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria
 $(".botones").removeClass("active");
    // Luego agrega la clase 'active' solo al botón clickeado
    $("#services_tabla").addClass("active");
     $("#services").addClass("active");



        listar_servicios();

    });

   $(document).on("click", "#editar_servicio", function () {

            let valor = $(this).attr("data");

        return $.ajax({
                url: host + "/configuracion/editar_servicio/"+valor + "/",
                method: "GET",
                dataType: "json",
                success: function (response) {

                     $("#serviceModalTitle").text("Editar Servicio");
                     $("#body_servicios").html(response.resultado);
                     $("#serviceModal").addClass("active");

                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });




    });



        function listar_servicios(){


            var contador=1;
              return $.ajax({
                url: host + "/configuracion/lista_servicios/",
                method: "GET",
                dataType: "json",
                success: function (response) {
                    let content = "";

                    response.tareas.forEach((tarea) => {

                         content += `
                         <tr>

                          <td>${contador}</td>
                    <td><strong>${tarea.titulo}</strong></td>
                    <td>${tarea.detalle.substring(0, 100)}${tarea.detalle.length > 100 ? '...' : ''}</td>
                    <td>
                        <div style="width: 80px; height: 50px; overflow: hidden; border-radius: 4px;">
                            <img src="https://www.guara.com.bo/static/biblioteca/servicios/${tarea.imagen}" alt="${tarea.titulo}" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                    </td>
                    <td>
                        <div class="actions">
                            <a class="action-btn edit-btn edit-service" id="editar_servicio" data="${tarea.id}">
                                <i class="fas fa-edit"></i> Editar
                            </a>
                            <a class="action-btn delete-btn delete-service" id="eliminar_servicio" data="${tarea.id}">
                                <i class="fas fa-trash"></i> Eliminar
                            </a>
                        </div>
                    </td>
                    </tr>
                `;
                 contador++;


                    });

                    $("#servicesTableBody").html(content);


                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });



        }



$(document).on("click", "#eliminar_servicio", function () {

        let valor = $(this).attr("data");


        Swal.fire({
            title: "¿Estás seguro de eliminar el servicio?",
            text: "Esta acción no se puede deshacer.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#d33",
            cancelButtonColor: "#3085d6",
            confirmButtonText: "Sí, eliminar",
            cancelButtonText: "Cancelar"
        }).then((result) => {
            if (result.isConfirmed) {

               return $.ajax({
                    url: host + "/configuracion/eliminar_servicio/" + valor + "/",
                    method: "GET",
                    dataType: "json",
                    success: function (response) {
                        Swal.fire({
                            title: "Eliminado",
                            text: "el servicio ha sido eliminada correctamente.",
                            icon: "success",
                            confirmButtonColor: "#3085d6",
                            confirmButtonText: "OK"
                        }).then(() => {
                            location.reload(); // Recargar la página o actualizar la tabla
                        });
                    },
                    error: function (xhr, status, error) {
                        Swal.fire({
                            title: "Error",
                            text: "Hubo un problema al eliminar el servicio.",
                            icon: "error",
                            confirmButtonColor: "#d33",
                            confirmButtonText: "Cerrar"
                        });
                    }
                });
            }
        });


        });




   $(document).on("click", "#cancelServiceBtn", function () {

          $("#serviceModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });


   $(document).on("click", "#closeServiceModal", function () {

           $("#serviceModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });





/***************************************** CATEGORIAS *********************************************/



 $(document).on("click", "#addcategoriaBtn", function () {



                 $("#CategoriaModalTitle").html("Agregar Nueva Categoria");
                  $("#body_categoria").html(`<input type="hidden" id="tipocategoria" name="tipocategoria" value="1">
                     <input type="hidden" id="categoria_id" name="categoria_id" value="0">

                    <div class="form-group">
                        <label for="productName">Nombre de la Categoria *</label>
                        <input type="text" id="categoriaName" name="categoriaName" class="form-control" required>
                    </div>

                    <div class="form-group">
                        <label for="productDescription">Descripción *</label>
                        <textarea id="categoria_descripcion" name="categoria_descripcion" class="form-control" required></textarea>
                    </div>

                    <div class="form-group">
                        <label for="productIcon">Imagen</label>
                        <input type="file" id="categoria_imagen" name="categoria_imagen" class="form-control" accept=".jpg,.jpeg,.png,image/jpeg,image/png">
                    </div>`);


                $("#CategoriaModal").addClass("active");



    });

   $(document).on("click", "#categorias", function () {

          $(".admin-section").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria
 $(".botones").removeClass("active");
    // Luego agrega la clase 'active' solo al botón clickeado
    $("#categoria_tabla").addClass("active");
     $("#categorias").addClass("active");



        listar_categorias();

    });

   $(document).on("click", "#editar_categoria", function () {

            let valor = $(this).attr("data");

        return $.ajax({
                url: host + "/configuracion/editar_categoria/"+valor + "/",
                method: "GET",
                dataType: "json",
                success: function (response) {

                     $("#CategoriaModalTitle").text("Editar Categoria");
                     $("#body_categoria").html(response.resultado);
                     $("#CategoriaModal").addClass("active");

                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });




    });



        function listar_categorias(){


            var contador=1;
              return $.ajax({
                url: host + "/configuracion/lista_categorias/",
                method: "GET",
                dataType: "json",
                success: function (response) {
                    let content = "";

                    response.tareas.forEach((tarea) => {

                         content += `
                         <tr>
                          <td>${contador}</td>
                    <td><strong>${tarea.nombre}</strong></td>
                    <td>${tarea.detalle.substring(0, 100)}${tarea.detalle.length > 100 ? '...' : ''}</td>
                    <td>
                        <div style="width: 80px; height: 50px; overflow: hidden; border-radius: 4px;">
                            <img src="https://www.guara.com.bo/static/biblioteca/productos/${tarea.imagen}" alt="${tarea.nombre}" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                    </td>
                    <td>
                        <div class="actions">
                            <a class="action-btn edit-btn edit-service" id="editar_categoria" data="${tarea.id}">
                                <i class="fas fa-edit"></i> Editar
                            </a>
                            <a class="action-btn delete-btn delete-service" id="eliminar_categoria" data="${tarea.id}">
                                <i class="fas fa-trash"></i> Eliminar
                            </a>
                        </div>
                    </td>
                    </tr>
                `;
                 contador++;


                    });

                    $("#categoriaTableBody").html(content);


                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });



        }



$(document).on("click", "#eliminar_categoria", function () {

        let valor = $(this).attr("data");


        Swal.fire({
            title: "¿Estás seguro de eliminar la categoria?",
            text: "Esta acción no se puede deshacer.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#d33",
            cancelButtonColor: "#3085d6",
            confirmButtonText: "Sí, eliminar",
            cancelButtonText: "Cancelar"
        }).then((result) => {
            if (result.isConfirmed) {

               return $.ajax({
                    url: host + "/configuracion/eliminar_categoria/" + valor + "/",
                    method: "GET",
                    dataType: "json",
                    success: function (response) {
                        Swal.fire({
                            title: "Eliminado",
                            text: "La categoria ha sido eliminada correctamente.",
                            icon: "success",
                            confirmButtonColor: "#3085d6",
                            confirmButtonText: "OK"
                        }).then(() => {
                            location.reload(); // Recargar la página o actualizar la tabla
                        });
                    },
                    error: function (xhr, status, error) {
                        Swal.fire({
                            title: "Error",
                            text: "Hubo un problema al eliminar la categoria.",
                            icon: "error",
                            confirmButtonColor: "#d33",
                            confirmButtonText: "Cerrar"
                        });
                    }
                });
            }
        });


        });




   $(document).on("click", "#cancelCategoria", function () {

          $("#CategoriaModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });


   $(document).on("click", "#closeCategoriaModal", function () {

           $("#CategoriaModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });




/***************************************** PRODUCTOS *********************************************/



 $(document).on("click", "#addProductBtn", function () {



                 $("#ItemModalTitle").html("Agregar Nuevo Producto");
                $("#ItemModal").addClass("active");


    });

   $(document).on("click", "#products", function () {

          $(".admin-section").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria
 $(".botones").removeClass("active");
    // Luego agrega la clase 'active' solo al botón clickeado
    $("#products_tabla").addClass("active");
     $("#products").addClass("active");



      //  listar_items();

    });

   $(document).on("click", "#editar_producto", function () {

            let valor = $(this).attr("data");

        return $.ajax({
                url: host + "/configuracion/editar_producto/"+valor + "/",
                method: "GET",
                dataType: "json",
                success: function (response) {

                     $("#ItemModalTitle").text("Editar Producto");
                     $("#body_producto").html(response.resultado);
                     $("#ItemModal").addClass("active");

                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });




    });



        function listar_items(){


            var contador=1;
              return $.ajax({
                url: host + "/configuracion/lista_productos/",
                method: "GET",
                dataType: "json",
                success: function (response) {
                    let content = "";

                    response.tareas.forEach((tarea) => {

                         content += `
                         <tr>
                          <td>${contador}</td>
                    <td><strong>${tarea.nombre}</strong></td>
                    <td>${tarea.detalle.substring(0, 100)}${tarea.detalle.length > 100 ? '...' : ''}</td>
                    <td>
                        <div style="width: 80px; height: 50px; overflow: hidden; border-radius: 4px;">
                            <img src="https://www.guara.com.bo/static/biblioteca/productos/${tarea.imagen}" alt="${tarea.nombre}" style="width: 100%; height: 100%; object-fit: cover;">
                        </div>
                    </td>
                    <td>
                        <div class="actions">
                            <a class="action-btn edit-btn edit-service" id="editar_producto" data="${tarea.id}">
                                <i class="fas fa-edit"></i> Editar
                            </a>
                            <a class="action-btn delete-btn delete-service" id="eliminar_producto" data="${tarea.id}">
                                <i class="fas fa-trash"></i> Eliminar
                            </a>
                        </div>
                    </td>
                    </tr>
                `;
                 contador++;


                    });

                    $("#productsTableBody").html(content);


                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });



        }



$(document).on("click", "#eliminar_producto", function () {

        let valor = $(this).attr("data");


        Swal.fire({
            title: "¿Estás seguro de eliminar el producto?",
            text: "Esta acción no se puede deshacer.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#d33",
            cancelButtonColor: "#3085d6",
            confirmButtonText: "Sí, eliminar",
            cancelButtonText: "Cancelar"
        }).then((result) => {
            if (result.isConfirmed) {

               return $.ajax({
                    url: host + "/configuracion/eliminar_producto/" + valor + "/",
                    method: "GET",
                    dataType: "json",
                    success: function (response) {
                        Swal.fire({
                            title: "Eliminado",
                            text: "el producto ha sido eliminada correctamente.",
                            icon: "success",
                            confirmButtonColor: "#3085d6",
                            confirmButtonText: "OK"
                        }).then(() => {
                            location.reload(); // Recargar la página o actualizar la tabla
                        });
                    },
                    error: function (xhr, status, error) {
                        Swal.fire({
                            title: "Error",
                            text: "Hubo un problema al eliminar el producto.",
                            icon: "error",
                            confirmButtonColor: "#d33",
                            confirmButtonText: "Cerrar"
                        });
                    }
                });
            }
        });


        });




   $(document).on("click", "#closItemModal", function () {

          $("#ItemModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });


   $(document).on("click", "#cancelItemBtn", function () {

           $("#ItemModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });




/***************************************** CLIENTES *********************************************/



 $(document).on("click", "#addclienteBtn", function () {



                 $("#clienteModalTitle").html("Agregar Nuevo Cliente");
                $("#clienteModal").addClass("active");


    });

   $(document).on("click", "#clientes", function () {

          $(".admin-section").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria
 $(".botones").removeClass("active");
    // Luego agrega la clase 'active' solo al botón clickeado
    $("#clientes_tabla").addClass("active");
     $("#clientes").addClass("active");



        listar_clientes();

    });

   $(document).on("click", "#editar_cliente", function () {

            let valor = $(this).attr("data");

        return $.ajax({
                url: host + "/configuracion/editar_cliente/"+valor + "/",
                method: "GET",
                dataType: "json",
                success: function (response) {

                     $("#clienteModalTitle").text("Editar Cliente");
                     $("#body_clientes").html(response.resultado);
                     $("#clienteModal").addClass("active");

                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });




    });


let dataTable_clientes;
let dataTableinicializado_clientes = false;


        function listar_clientes(){


            var contador=1;
              return $.ajax({
                url: host + "/configuracion/lista_clientes/",
                method: "GET",
                dataType: "json",
                success: function (response) {
                    let content = "";

                    response.tareas.forEach((tarea) => {

                         content += `
                         <tr>

                          <td>${contador}</td>
                    <td><strong>${tarea.nombre}</strong></td>
                    <td><strong>${tarea.titular}</strong></td>
                    <td>${tarea.detalle.substring(0, 100)}${tarea.detalle.length > 100 ? '...' : ''}</td>
                    <td>${tarea.correo}</td>
                    <td>${tarea.celular}</td>

                    <td>
                        <div class="actions">
                            <a class="action-btn edit-btn edit-service" id="editar_cliente" data="${tarea.id}">
                                <i class="fas fa-edit"></i> Editar
                            </a>
                            <a class="action-btn delete-btn delete-service" id="eliminar_cliente" data="${tarea.id}">
                                <i class="fas fa-trash"></i> Eliminar
                            </a>
                        </div>
                    </td>
                    </tr>
                `;
                 contador++;


                    });

                    $("#clientesTableBody").html(content);

                    Iniciar_tabla_clientes();





                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });



        }

const dataTableOptions_clientes = {

        dom: 'Bfrtip',
        buttons: [
                                    {
                                      extend: 'excelHtml5',
                                      text: '📊 Excel' ,
                                      title: 'Listado de Clientes',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5]
                                      }
                                    },
                                    {
                                      extend: 'csvHtml5',
                                      text: '📄 CSV',
                                      title: 'Listado de Clientes',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5]
                                      }
                                    },
                                    {
                                      extend: 'pdfHtml5',
                                      text: '📕 PDF' ,
                                      title: 'Listado de Clientes',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5]
                                      }
                                    },

                                    {
                                      extend: 'print',
                                      text: '🖨️ Imprimir' ,
                                      title: 'Listado de Clientes',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5]
                                      }
                                    }
                                  ],
        language: {
                          url: "https://cdn.datatables.net/plug-ins/1.13.8/i18n/es-ES.json"
                        }
};
const Iniciar_tabla_clientes = () => {
    if (dataTableinicializado_clientes) {
        dataTable_clientes.destroy();
    }


        dataTable_clientes = $('#clienteTable').DataTable(dataTableOptions_clientes);
        dataTableinicializado_clientes = true;

};

$(document).on("click", "#eliminar_cliente", function () {

        let valor = $(this).attr("data");


        Swal.fire({
            title: "¿Estás seguro de eliminar el cliente?",
            text: "Esta acción no se puede deshacer.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#d33",
            cancelButtonColor: "#3085d6",
            confirmButtonText: "Sí, eliminar",
            cancelButtonText: "Cancelar"
        }).then((result) => {
            if (result.isConfirmed) {

               return $.ajax({
                    url: host + "/configuracion/eliminar_cliente/" + valor + "/",
                    method: "GET",
                    dataType: "json",
                    success: function (response) {
                        Swal.fire({
                            title: "Eliminado",
                            text: "el cliente ha sido eliminada correctamente.",
                            icon: "success",
                            confirmButtonColor: "#3085d6",
                            confirmButtonText: "OK"
                        }).then(() => {
                            location.reload(); // Recargar la página o actualizar la tabla
                        });
                    },
                    error: function (xhr, status, error) {
                        Swal.fire({
                            title: "Error",
                            text: "Hubo un problema al eliminar el cliente.",
                            icon: "error",
                            confirmButtonColor: "#d33",
                            confirmButtonText: "Cerrar"
                        });
                    }
                });
            }
        });


        });




   $(document).on("click", "#cancelclienteBtn", function () {

          $("#clienteModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });


   $(document).on("click", "#closeclienteModal", function () {

           $("#clienteModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });




/***************************************** NOTAS DE ENTREGAS *********************************************/



 $(document).on("click", "#addnotaBtn", function () {



                 $("#notaModalTitle").html("Agregar Nueva Nota");
                $("#notaModal").addClass("active");



    });

   $(document).on("click", "#notas", function () {

        $(".admin-section").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria
        $(".botones").removeClass("active");
    // Luego agrega la clase 'active' solo al botón clickeado
        $("#notas_tabla").addClass("active");
        $("#notas").addClass("active");



        listar_notas();

    });

   $(document).on("click", "#editar_nota", function () {

            let valor = $(this).attr("data");

        return $.ajax({
                url: host + "/configuracion/editar_nota/"+valor + "/",
                method: "GET",
                dataType: "json",
                success: function (response) {

                     $("#notaModalTitle").text("Editar Nota");
                     $("#body_notas").html(response.resultado);
                     $("#notaModal").addClass("active");

                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });




    });


let dataTable_notas;
let dataTableinicializado_notas = false;

        function listar_notas(){


            var contador=1;
              return $.ajax({
                url: host + "/configuracion/lista_notas/",
                method: "GET",
                dataType: "json",
                success: function (response) {
                    let content = "";

                    response.tareas.forEach((tarea) => {

                         content += `
                         <tr>

                          <td>${contador}</td>
                    <td><strong>${tarea.ncliente}</strong></td>
                    <td><strong>${tarea.fecha}</strong></td>
                    <td>${tarea.detalle.substring(0, 100)}${tarea.detalle.length > 100 ? '...' : ''}</td>
                    <td>${tarea.talla}</td>
                    <td>${tarea.cantidad}</td>
                    <td>${tarea.precio}</td>

                    <td>
                        <div class="actions">

                         <a class="action-btn info-btn edit-service" id="ver_nota" href="${host}/configuracion/ver_nota/${tarea.id}/" target="_blank">
                                <i class="fas fa-note-sticky"></i> Revisar
                            </a>


                            <a class="action-btn edit-btn edit-service" id="editar_nota" data="${tarea.id}">
                                <i class="fas fa-edit"></i> Editar
                            </a>
                            <a class="action-btn delete-btn delete-service" id="eliminar_nota" data="${tarea.id}">
                                <i class="fas fa-trash"></i> Eliminar
                            </a>
                        </div>
                    </td>
                    </tr>
                `;
                 contador++;


                    });

                    $("#notaTableBody").html(content);


                    Iniciar_tabla_notas();


                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });



        }



const dataTableOptions_notas = {

            dom: 'Bfrtip',
            buttons: [
                                    {
                                      extend: 'excelHtml5',
                                      text: '📊 Excel' ,
                                      title: 'Reporte de Notas de Ventas',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5,6]
                                      }
                                    },
                                    {
                                      extend: 'csvHtml5',
                                      text: '📄 CSV',
                                      title: 'Reporte de Notas de Ventas',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5,6]
                                      }
                                    },
                                    {
                                      extend: 'pdfHtml5',
                                      text: '📕 PDF' ,
                                      title: 'Reporte de Notas de Ventas',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5,6]
                                      }
                                    },

                                    {
                                      extend: 'print',
                                      text: '🖨️ Imprimir' ,
                                      title: 'Reporte de Notas de Ventas',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5,6]
                                      }
                                    }
                                  ],
            language: {
                          url: "https://cdn.datatables.net/plug-ins/1.13.8/i18n/es-ES.json"
                        }
};

;


const Iniciar_tabla_notas = () => {
    if (dataTableinicializado_notas) {
        dataTable_notas.destroy();
    }


        dataTable_notas = $('#notaTable').DataTable(dataTableOptions_notas);
        dataTableinicializado_notas = true;

};

$(document).on("click", "#eliminar_nota", function () {

        let valor = $(this).attr("data");


        Swal.fire({
            title: "¿Estás seguro de eliminar la nota?",
            text: "Esta acción no se puede deshacer.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#d33",
            cancelButtonColor: "#3085d6",
            confirmButtonText: "Sí, eliminar",
            cancelButtonText: "Cancelar"
        }).then((result) => {
            if (result.isConfirmed) {

               return $.ajax({
                    url: host + "/configuracion/eliminar_nota/" + valor + "/",
                    method: "GET",
                    dataType: "json",
                    success: function (response) {
                        Swal.fire({
                            title: "Eliminado",
                            text: "La nota ha sido eliminada correctamente.",
                            icon: "success",
                            confirmButtonColor: "#3085d6",
                            confirmButtonText: "OK"
                        }).then(() => {
                            location.reload(); // Recargar la página o actualizar la tabla
                        });
                    },
                    error: function (xhr, status, error) {
                        Swal.fire({
                            title: "Error",
                            text: "Hubo un problema al eliminar la nota.",
                            icon: "error",
                            confirmButtonColor: "#d33",
                            confirmButtonText: "Cerrar"
                        });
                    }
                });
            }
        });


        });




   $(document).on("click", "#cancelnotaBtn", function () {

          $("#notaModal").removeClass("active");

           $("#form_notas")[0].reset();


    });


   $(document).on("click", "#closenotaModal", function () {

        $("#notaModal").removeClass("active");
        $("#form_notas")[0].reset();

    });



/************************************* tabla nota de venta *******************************************/

let contador = 1;

       $(document).on("click", "#btn-addFila", function () {

           let cliente = $("#cliente").val();

            if (cliente=='') {
            toastr.info("Por favor, seleccione un cliente primeramente.", "ALERTA", {
            timeOut: 5000,
            closeButton: true,
            progressBar: true
            });
        return;
        }
    let nuevaFila = `
        <tr>
            <td width="4%" align="center">${contador}</td>
            <td width="65%">
                <input type="text" class="form-control detalle" name="detalle[]">
            </td>
            <td><input type="text" class="form-control talla" name="talla[]"></td>
            <td><input type="text" class="form-control cantidad" name="cantidad[]"></td>
            <td><input type="text" class="form-control precio" name="precio[]"></td>
            <td align="center">
                <button type="button" class="btn btn-danger btn-eliminarFila btn-sm">
                    <span class="fa fa-times"></span>
                </button>
            </td>
        </tr>
    `;

    let $nuevaFila = $(nuevaFila);
    $("#tbody-registro").append($nuevaFila);



    contador++;
});


    $(document).on("click", ".btn-eliminarFila", function() {
        $(this).closest("tr").remove();
        actualizarNumeracion();
        calcularTotales();
    });




      // Función para actualizar la numeración de las filas
    function actualizarNumeracion() {
        contador=1;
        $("#tbody-registro tr").each(function(index) {
            $(this).find("td:first").text(index + 1);
            contador++;
        });

    }


      function calcularTotales() {

            let totalcantidad = 0;
            let totalprecio = 0;
            $("#tbody-registro tr").each(function () {
                let cantidad = parseFloat($(this).find(".cantidad").val()) || 0;
                let precio = parseFloat($(this).find(".precio").val()) || 0;
                totalprecio = totalprecio + (cantidad * precio);
                totalcantidad += cantidad;
            });



            $("#total_general").val(totalcantidad.toFixed(2));
            $("#total_precion").val(totalprecio.toFixed(2));





    }





     $(document).on("input", ".cantidad , .precio", function () {

          let valor = parseFloat($(this).val());

            if (valor < 0) {
                $(this).val(0);
                alert("No se permiten valores negativos.");
            }else{
                calcularTotales();
            }

        });




/***************************************************** COTIZACION *******************************************/

   $(document).on("click", "#cotizaciones", function () {

          $(".admin-section").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria
        $(".botones").removeClass("active");
    // Luego agrega la clase 'active' solo al botón clickeado
    $("#cotizaciones_tabla").addClass("active");
     $("#cotizaciones").addClass("active");

        $(".tab-btn").removeClass("active");
    // Luego agrega la clase 'active' solo al botón clickeado
    $("#pestana_total").addClass("active");

    listar_cotizaciones(0);

    });


   $(document).on("click", "#pestana_total", function () {


        $(".tab-btn").removeClass("active");
    // Luego agrega la clase 'active' solo al botón clickeado
    $("#pestana_total").addClass("active");

    listar_cotizaciones(0);

    });

$(document).on("click", "#pestana_pendiente", function () {


        $(".tab-btn").removeClass("active");
    // Luego agrega la clase 'active' solo al botón clickeado
    $("#pestana_pendiente").addClass("active");

    listar_cotizaciones(1);

    });

    $(document).on("click", "#pestana_concretado", function () {


        $(".tab-btn").removeClass("active");
    // Luego agrega la clase 'active' solo al botón clickeado
    $("#pestana_concretado").addClass("active");

    listar_cotizaciones(2);

    });


 $(document).on("click", "#agregar_cotizacion", function () {


                $("#cotizaciones_formulario").addClass("active");



    });



   $(document).on("click", "#editar_cotizacion", function () {

            let valor = $(this).attr("data");

        return $.ajax({
                url: host + "/configuracion/editar_cotizacion/"+valor + "/",
                method: "GET",
                dataType: "json",
                success: function (response) {

                     $("#contenido_cotizacion").html(response.resultado);
                     $("#cotizaciones_formulario").addClass("active");

                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });




    });



let dataTable_cotizacion;
let dataTableinicializado_cotizacion = false;


function listar_cotizaciones(valor){
    var contador=1;
    var ctotal=0;
    var cpendientes=0;
    var cconcretados=0;

    return $.ajax({
        url: host + "/configuracion/lista_cotizaciones/",
        method: "GET",
        dataType: "json",
        success: function (response) {
            // Primero asegurar que DataTable está inicializado
            if (!dataTableinicializado_cotizacion) {
                Iniciar_tabla_cotizacion();
            }

            // Limpiar la tabla
            dataTable_cotizacion.clear();

            let estado="Pendiente";
            let newData = [];

            response.tareas.forEach((tarea) => {
                cpendientes = tarea.total_pendientes;
                cconcretados = tarea.total_concretados;
                ctotal = tarea.total_contador;

                if(valor === 0){
                    if(tarea.estado === 1 ){
                        estado="Pendiente";
                    }else{
                        estado="Concretado";
                    }
                    let idEncriptado = encodeBase64(tarea.id.toString());
                    newData.push([
                        contador,
                         `<strong>CTG${tarea.id}</strong>`,
                        `<strong>${tarea.prospecto}</strong>`,
                        `<strong>${tarea.fecha}</strong>`,
                        `${tarea.detalle.substring(0, 100)}${tarea.detalle.length > 100 ? '...' : ''}`,
                        tarea.cantidad,
                        tarea.monto,
                        tarea.entrega,
                        estado,
                        `<div class="actions">
                            <a class="action-btn info-btn edit-service" id="ver_recibo" href="${host}/configuracion/ver_cotizacion/${idEncriptado}/" target="_blank">
                                <i class="fas fa-coins"></i> Imprimir
                            </a>
                            <a class="action-btn info-btn edit-service" id="detalle_recibo" data="${tarea.id}">
                                <i class="fas fa-cloud-arrow-up"></i>
                                <span class="badge">${tarea.total_detalles_activos}</span>
                                Historial
                            </a>
                            <a class="action-btn edit-btn edit-service" id="editar_cotizacion" data="${tarea.id}">
                                <i class="fas fa-edit"></i> Editar
                            </a>
                            <a class="action-btn delete-btn delete-service" id="eliminar_cotizacion" data="${tarea.id}">
                                <i class="fas fa-trash"></i> Eliminar
                            </a>
                        </div>`
                    ]);
                    contador++;
                } else {
                    if(parseInt(tarea.estado) === parseInt(valor)) {
                        if(tarea.estado === 1 ){
                            estado="Pendiente";
                        }else{
                            estado="Concretado";
                        }
                        let idEncriptado = encodeBase64(tarea.id.toString());
                        newData.push([
                            contador,
                            `<strong>CTG${tarea.id}</strong>`,
                            `<strong>${tarea.prospecto}</strong>`,
                            `<strong>${tarea.fecha}</strong>`,
                            `${tarea.detalle.substring(0, 100)}${tarea.detalle.length > 100 ? '...' : ''}`,
                            tarea.cantidad,
                            tarea.monto,
                            tarea.entrega,
                            estado,
                            `<div class="actions">
                                <a class="action-btn info-btn edit-service" id="ver_recibo" href="${host}/configuracion/ver_cotizacion/${idEncriptado}/" target="_blank">
                                    <i class="fas fa-coins"></i> Imprimir
                                </a>
                                <a class="action-btn info-btn edit-service" id="detalle_recibo" data="${tarea.id}">
                                    <i class="fas fa-cloud-arrow-up"></i>
                                    <span class="badge">${tarea.total_detalles_activos}</span>
                                    Historial
                                </a>
                                <a class="action-btn edit-btn edit-service" id="editar_cotizacion" data="${tarea.id}">
                                    <i class="fas fa-edit"></i> Editar
                                </a>
                                <a class="action-btn delete-btn delete-service" id="eliminar_cotizacion" data="${tarea.id}">
                                    <i class="fas fa-trash"></i> Eliminar
                                </a>
                            </div>`
                        ]);
                        contador++;
                    }
                }
            });

            // Agregar los nuevos datos
            if (newData.length > 0) {
                dataTable_cotizacion.rows.add(newData);
            }

            // Redibujar la tabla
            dataTable_cotizacion.draw();

            // Actualizar contadores
            $("#conta_total").html(ctotal);
            $("#conta_pendiente").html(cpendientes);
            $("#conta_concretado").html(cconcretados);
        },
        error: function (xhr, status, error) {
            alert("Error al obtener los datos: " + error);
        }
    });
}

const encodeBase64 = (str) => {
    return btoa(str); // Convierte a Base64
};

const decodeBase64 = (str) => {
    return atob(str); // Convierte de Base64 a texto original
};

$(document).on("click", "#detalle_recibo", function () {

    let id_auto = $(this).attr("data");

      let idEncriptado = encodeBase64(id_auto.toString());
    // O si quieres abrir en nueva pestaña:
     window.open(host + "/configuracion/detalle_cotizacion/" + idEncriptado + "/", '_blank');


});




const dataTableOptions_cotizacion = {

            dom: 'Bfrtip',
            buttons: [
                                    {
                                      extend: 'excelHtml5',
                                      text: '📊 Excel' ,
                                      title: 'Reporte de Cotizaciones',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5,6,7,8]
                                      }
                                    },
                                    {
                                      extend: 'csvHtml5',
                                      text: '📄 CSV',
                                      title: 'Reporte de Cotizaciones',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5,6,7,8]
                                      }
                                    },
                                    {
                                      extend: 'pdfHtml5',
                                      text: '📕 PDF' ,
                                      title: 'Reporte de Cotizaciones',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5,6,7,8]
                                      }
                                    },

                                    {
                                      extend: 'print',
                                      text: '🖨️ Imprimir' ,
                                      title: 'Reporte de Cotizaciones',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5,6,7,8]
                                      }
                                    }
                                  ],
            language: {
                          url: "https://cdn.datatables.net/plug-ins/1.13.8/i18n/es-ES.json"
                        },
            destroy: true
};

;


const Iniciar_tabla_cotizacion = () => {
    if (dataTableinicializado_cotizacion) {
        dataTable_cotizacion.destroy();
    }


        dataTable_cotizacion = $('#cotizacionTable').DataTable(dataTableOptions_cotizacion);
        dataTableinicializado_cotizacion = true;

};



$(document).on("click", "#eliminar_cotizacion", function () {

        let valor = $(this).attr("data");


        Swal.fire({
            title: "¿Estás seguro de eliminar la cotización?",
            text: "Esta acción no se puede deshacer.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#d33",
            cancelButtonColor: "#3085d6",
            confirmButtonText: "Sí, eliminar",
            cancelButtonText: "Cancelar"
        }).then((result) => {
            if (result.isConfirmed) {

               return $.ajax({
                    url: host + "/configuracion/eliminar_cotizacion/" + valor + "/",
                    method: "GET",
                    dataType: "json",
                    success: function (response) {
                        Swal.fire({
                            title: "Eliminado",
                            text: "La cotización se ha sido eliminada correctamente.",
                            icon: "success",
                            confirmButtonColor: "#3085d6",
                            confirmButtonText: "OK"
                        }).then(() => {
                            location.reload(); // Recargar la página o actualizar la tabla
                        });
                    },
                    error: function (xhr, status, error) {
                        Swal.fire({
                            title: "Error",
                            text: "Hubo un problema al eliminar la cotización.",
                            icon: "error",
                            confirmButtonColor: "#d33",
                            confirmButtonText: "Cerrar"
                        });
                    }
                });
            }
        });


        });






   $(document).on("click", "#cerrar_formulario_cotizacion", function () {

           $("#cotizaciones_formulario").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });




/************************************* tabla cotizacion *******************************************/


$(document).on("click", "#btn-addFilacotizacion", function () {
    let nuevaFilacotizacion = `
        <tr>
            <td class="col-talla2">
                <input type="hidden" name="detalle_id[]" value="">
                <input type="text" class="form-control cantidadc" name="cantidadc[]">
            </td>
            <td class="col-detalle2"><textarea class="form-control detallec" name="detallec[]"></textarea></td>
            <td class="col-cantidad2"><input type="text" class="form-control preciou" name="preciou[]"></td>
            <td class="col-cantidad2"><input type="text" class="form-control total_iten" name="total_iten[]" readonly></td>
            <td class="col-diseno2"><input type="file" class="form-control respaldo" name="respaldo[]"></td>
            <td align="center">
                <button type="button" class="btn btn-danger btn-eliminarFilac btn-sm">
                    <span class="fa fa-times"></span>
                </button>
            </td>
        </tr>
    `;

    let $nuevaFilai = $(nuevaFilacotizacion);
    $("#body_cotizaciones").append($nuevaFilai);
});



    $(document).on("click", ".btn-eliminarFilac", function() {
        $(this).closest("tr").remove();
        calcularTotalesc();
    });





      function calcularTotalesc() {

            let totalunitario = 0;
            let totalprecio = 0;
            $("#body_cotizaciones tr").each(function () {
                let cantidad = parseFloat($(this).find(".cantidadc").val()) || 0;
                let preciou = parseFloat($(this).find(".preciou").val()) || 0;
                totalprecio = totalprecio + (cantidad * preciou);
                totalunitario += preciou;
                let total = cantidad * preciou;

                 $(this).find(".total_iten").val(total.toFixed(2));
            });



            $("#total_unitario").val(totalunitario.toFixed(2));
            $("#total_precio").val(totalprecio.toFixed(2));





    }





     $(document).on("input", ".cantidadc , .preciou", function () {

          let valor = parseFloat($(this).val());

            if (valor < 0) {
                $(this).val(0);
                alert("No se permiten valores negativos.");
            }else{
                calcularTotalesc();
            }

        });




 /***************************************************** PROVEEDOR *******************************************/

   $(document).on("click", "#proveedores", function () {

          $(".admin-section").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria
        $(".botones").removeClass("active");
    // Luego agrega la clase 'active' solo al botón clickeado
    $("#proveedores_tabla").addClass("active");
     $("#proveedores").addClass("active");

     listar_proveedores();

    });


 $(document).on("click", "#addproveedorBtn", function () {



                 $("#proveedorModalTitle").html("Agregar Nuevo Proveedor");
                $("#proveedorModal").addClass("active");



    });



   $(document).on("click", "#editar_proveedor", function () {

            let valor = $(this).attr("data");

        return $.ajax({
                url: host + "/configuracion/editar_proveedor/"+valor + "/",
                method: "GET",
                dataType: "json",
                success: function (response) {

                     $("#proveedorModalTitle").text("Editar Proveedor");
                     $("#body_proveedor").html(response.resultado);
                     $("#proveedorModal").addClass("active");

                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });




    });


let dataTable_proveedor;
let dataTableinicializado_proveedor = false;

        function listar_proveedores(){


            var contador=1;
              return $.ajax({
                url: host + "/configuracion/lista_proveedor/",
                method: "GET",
                dataType: "json",
                success: function (response) {
                    let content = "";

                    response.tareas.forEach((tarea) => {

                         content += `
                         <tr>

                          <td>${contador}</td>
                    <td><strong>${tarea.nombre}</strong></td>
                    <td><strong>${tarea.contacto}</strong></td>
                    <td>${tarea.detalle.substring(0, 100)}${tarea.detalle.length > 100 ? '...' : ''}</td>
                     <td>${tarea.correo}</td>
                    <td>${tarea.celular}</td>
                    <td>
                        <div class="actions">

                            <a class="action-btn edit-btn edit-service" id="editar_proveedor" data="${tarea.id}">
                                <i class="fas fa-edit"></i> Editar
                            </a>
                            <a class="action-btn delete-btn delete-service" id="eliminar_proveedor" data="${tarea.id}">
                                <i class="fas fa-trash"></i> Eliminar
                            </a>
                        </div>
                    </td>
                    </tr>
                `;
                 contador++;


                    });

                    $("#proveedorTableBody").html(content);


                    Iniciar_tabla_proveedor();


                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });



        }



const dataTableOptions_proveedor = {

            dom: 'Bfrtip',
            buttons: [
                                    {
                                      extend: 'excelHtml5',
                                      text: '📊 Excel' ,
                                      title: 'Reporte de Proveedores',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5]
                                      }
                                    },
                                    {
                                      extend: 'csvHtml5',
                                      text: '📄 CSV',
                                      title: 'Reporte de Proveedores',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5]
                                      }
                                    },
                                    {
                                      extend: 'pdfHtml5',
                                      text: '📕 PDF' ,
                                      title: 'Reporte de Proveedores',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5]
                                      }
                                    },

                                    {
                                      extend: 'print',
                                      text: '🖨️ Imprimir' ,
                                      title: 'Reporte de Proveedores',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5]
                                      }
                                    }
                                  ],
            language: {
                          url: "https://cdn.datatables.net/plug-ins/1.13.8/i18n/es-ES.json"
                        }
};

;


const Iniciar_tabla_proveedor = () => {
    if (dataTableinicializado_proveedor) {
        dataTable_proveedor.destroy();
    }


        dataTable_proveedor = $('#proveedorTable').DataTable(dataTableOptions_proveedor);
        dataTableinicializado_proveedor = true;

};

$(document).on("click", "#eliminar_proveedor", function () {

        let valor = $(this).attr("data");


        Swal.fire({
            title: "¿Estás seguro de eliminar el proveedor?",
            text: "Esta acción no se puede deshacer.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#d33",
            cancelButtonColor: "#3085d6",
            confirmButtonText: "Sí, eliminar",
            cancelButtonText: "Cancelar"
        }).then((result) => {
            if (result.isConfirmed) {

               return $.ajax({
                    url: host + "/configuracion/eliminar_proveedor/" + valor + "/",
                    method: "GET",
                    dataType: "json",
                    success: function (response) {
                        Swal.fire({
                            title: "Eliminado",
                            text: "El proveedor se ha sido eliminado correctamente.",
                            icon: "success",
                            confirmButtonColor: "#3085d6",
                            confirmButtonText: "OK"
                        }).then(() => {
                            location.reload(); // Recargar la página o actualizar la tabla
                        });
                    },
                    error: function (xhr, status, error) {
                        Swal.fire({
                            title: "Error",
                            text: "Hubo un problema al eliminar el proveedor.",
                            icon: "error",
                            confirmButtonColor: "#d33",
                            confirmButtonText: "Cerrar"
                        });
                    }
                });
            }
        });


        });




   $(document).on("click", "#cancelproveedorBtn", function () {

          $("#proveedorModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });


   $(document).on("click", "#closeproveedorModal", function () {

           $("#proveedorModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });







/***************************************************** DASHBOARD *******************************************/

   $(document).on("click", "#dashboard", function () {

          $(".admin-section").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria
        $(".botones").removeClass("active");
    // Luego agrega la clase 'active' solo al botón clickeado
    $("#dashboard_tabla").addClass("active");
     $("#dashboard").addClass("active");

    });



/***************************************************** INGRESOS *******************************************/

   $(document).on("click", "#ingresos", function () {

          $(".admin-section").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria
        $(".botones").removeClass("active");
    // Luego agrega la clase 'active' solo al botón clickeado
    $("#ingresos_tabla").addClass("active");
     $("#ingresos").addClass("active");

     listar_recibos();

    });


 $(document).on("click", "#addingresoBtn", function () {




                 $("#ingresoModalTitle").html("Agregar Nuevo Recibo");
                $("#ingresoModal").addClass("active");
                 $("#tiporecibo").val(1);
                  $("#recibo_id").val(0);
                  $("#fechai").val("");
                   $("#clienter").val("");
                    $("#metodo").val("");
                    $("#tbody-ingresos").html("");
                    $("#porcentaje").val("");
                    $("#cuenta").val(0);
                     $("#total_generali").val(0);
                      $("#total_precioi").val(0);





    });

 $(document).on("change", "#clienter", function () {
      let valor = $(this).val();

       return $.ajax({
                url: host + "/configuracion/revisar_saldo/"+valor+ "/",
                method: "GET",
                dataType: "json",
                success: function (response) {



                    $("#cotizacionr").html(response.opciones);

                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });
 });




 $(document).on("click", "#revicion_deuda", function () {
      let cotizacion = $("#cotizacionr").val();
      let cliente =  $("#clienter").val();



       return $.ajax({
                url: host + "/configuracion/revisar_saldo_cotizacion/"+cliente +"+"+cotizacion+"/",
                method: "GET",
                dataType: "json",
                success: function (response) {

                    $("#alerta_recibo").html(response.resultado);

                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });

 });


   $(document).on("click", "#editar_recibo", function () {

            let valor = $(this).attr("data");

        return $.ajax({
                url: host + "/configuracion/editar_recibo/"+valor + "/",
                method: "GET",
                dataType: "json",
                success: function (response) {

                     $("#ingresoModalTitle").text("Editar Recibo");
                     $("#body_ingresos").html(response.resultado);
                     $("#ingresoModal").addClass("active");

                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });




    });


let dataTable_ingresos;
let dataTableinicializado_ingresos = false;

        function listar_recibos(){


            var contador=1;
              return $.ajax({
                url: host + "/configuracion/lista_recibos/",
                method: "GET",
                dataType: "json",
                success: function (response) {
                    let content = "";

                    response.tareas.forEach((tarea) => {

                        const cotizacion = tarea.cotizacion ? "CTG" + tarea.cotizacion : "";

                         content += `
                         <tr>

                          <td>${contador}</td>
                    <td><strong>${tarea.ncliente}</strong></td>
                     <td><strong>${cotizacion}</strong></td>
                    <td><strong>${tarea.fecha}</strong></td>
                    <td>${tarea.detalle.substring(0, 100)}${tarea.detalle.length > 100 ? '...' : ''}</td>
                     <td>${tarea.metodo}</td>
                    <td>${tarea.cantidad}</td>
                    <td>${tarea.total}</td>
                    <td>${tarea.cuenta}</td>
                    <td>${tarea.saldo}</td>

                    <td>
                        <div class="actions">

                         <a class="action-btn info-btn edit-service" id="ver_recibo" href="${host}/configuracion/ver_recibo/${tarea.id}/" target="_blank">
                                <i class="fas fa-coins"></i> Imprimir
                            </a>


                            <a class="action-btn edit-btn edit-service" id="editar_recibo" data="${tarea.id}">
                                <i class="fas fa-edit"></i> Editar
                            </a>
                            <a class="action-btn delete-btn delete-service" id="eliminar_recibo" data="${tarea.id}">
                                <i class="fas fa-trash"></i> Eliminar
                            </a>
                        </div>
                    </td>
                    </tr>
                `;
                 contador++;


                    });

                    $("#ingresoTableBody").html(content);


                    Iniciar_tabla_ingresos();


                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });



        }



const dataTableOptions_ingresos = {

            dom: 'Bfrtip',
            buttons: [
                                    {
                                      extend: 'excelHtml5',
                                      text: '📊 Excel' ,
                                      title: 'Reporte de Ingresos',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5,6,7,8,9]
                                      }
                                    },
                                    {
                                      extend: 'csvHtml5',
                                      text: '📄 CSV',
                                      title: 'Reporte de Ingresos',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5,6,7,8,9]
                                      }
                                    },
                                    {
                                      extend: 'pdfHtml5',
                                      text: '📕 PDF' ,
                                      title: 'Reporte de Ingresos',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5,6,7,8,9]
                                      }
                                    },

                                    {
                                      extend: 'print',
                                      text: '🖨️ Imprimir' ,
                                      title: 'Reporte de Ingresos',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5,6,7,8,9]
                                      }
                                    }
                                  ],
            language: {
                          url: "https://cdn.datatables.net/plug-ins/1.13.8/i18n/es-ES.json"
                        }
};

;


const Iniciar_tabla_ingresos = () => {
    if (dataTableinicializado_ingresos) {
        dataTable_ingresos.destroy();
    }


        dataTable_ingresos = $('#ingresoTable').DataTable(dataTableOptions_ingresos);
        dataTableinicializado_ingresos = true;

};

$(document).on("click", "#eliminar_recibo", function () {

        let valor = $(this).attr("data");


        Swal.fire({
            title: "¿Estás seguro de eliminar el recibo?",
            text: "Esta acción no se puede deshacer.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#d33",
            cancelButtonColor: "#3085d6",
            confirmButtonText: "Sí, eliminar",
            cancelButtonText: "Cancelar"
        }).then((result) => {
            if (result.isConfirmed) {

               return $.ajax({
                    url: host + "/configuracion/eliminar_recibo/" + valor + "/",
                    method: "GET",
                    dataType: "json",
                    success: function (response) {
                        Swal.fire({
                            title: "Eliminado",
                            text: "El recibo se ha sido eliminado correctamente.",
                            icon: "success",
                            confirmButtonColor: "#3085d6",
                            confirmButtonText: "OK"
                        }).then(() => {
                            location.reload(); // Recargar la página o actualizar la tabla
                        });
                    },
                    error: function (xhr, status, error) {
                        Swal.fire({
                            title: "Error",
                            text: "Hubo un problema al eliminar el recibo.",
                            icon: "error",
                            confirmButtonColor: "#d33",
                            confirmButtonText: "Cerrar"
                        });
                    }
                });
            }
        });


        });




   $(document).on("click", "#cancelingresoBtn", function () {

          $("#ingresoModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });


   $(document).on("click", "#closeingresoModal", function () {

           $("#ingresoModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });



/************************************* tabla ingreso *******************************************/

let contadori = 1;

       $(document).on("click", "#btn-addFilai", function () {

           let cliente = $("#cliente").val();

            if (cliente=='') {
            toastr.info("Por favor, Ingrese un cliente primeramente.", "ALERTA", {
            timeOut: 5000,
            closeButton: true,
            progressBar: true
            });
        return;
        }
    let nuevaFilai = `
        <tr>
            <td width="4%" align="center">${contadori}</td>
            <td width="65%">
                <input type="text" class="form-control detallei" name="detallei[]">
            </td>
            <td><input type="text" class="form-control cantidadi" name="cantidadi[]"></td>
            <td><input type="text" class="form-control precioi" name="precioi[]"></td>
            <td align="center">
                <button type="button" class="btn btn-danger btn-eliminarFilai btn-sm">
                    <span class="fa fa-times"></span>
                </button>
            </td>
        </tr>
    `;

    let $nuevaFilai = $(nuevaFilai);
    $("#tbody-ingresos").append($nuevaFilai);



    contadori++;
});


    $(document).on("click", ".btn-eliminarFilai", function() {
        $(this).closest("tr").remove();
        actualizarNumeracioni();
        calcularTotalesi();
    });




      // Función para actualizar la numeración de las filas
    function actualizarNumeracioni() {
        contadori=1;
        $("#tbody-ingresos tr").each(function(index) {
            $(this).find("td:first").text(index + 1);
            contadori++;
        });

    }


      function calcularTotalesi() {

            let totalcantidadi = 0;
            let totalprecioi = 0;
            $("#tbody-ingresos tr").each(function () {
                let cantidadi = parseFloat($(this).find(".cantidadi").val()) || 0;
                let precioi = parseFloat($(this).find(".precioi").val()) || 0;
                totalprecioi = totalprecioi + (cantidadi * precioi);
                totalcantidadi += cantidadi;
            });



            $("#total_generali").val(totalcantidadi.toFixed(2));
            $("#total_precioi").val(totalprecioi.toFixed(2));





    }





     $(document).on("input", ".cantidadi , .precioi", function () {

          let valor = parseFloat($(this).val());

            if (valor < 0) {
                $(this).val(0);
                alert("No se permiten valores negativos.");
            }else{
                calcularTotalesi();
            }

        });



/***************************************************** EGRESOS *******************************************/

   $(document).on("click", "#egresos", function () {

          $(".admin-section").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria
        $(".botones").removeClass("active");
    // Luego agrega la clase 'active' solo al botón clickeado
    $("#egresos_tabla").addClass("active");
     $("#egresos").addClass("active");

    listar_pagos();

    });


 $(document).on("click", "#addegresoBtn", function () {



                 $("#egresoModalTitle").html("Agregar Nuevo Pago");
                $("#egresoModal").addClass("active");
                $("#body_egresos").html(`
                   <input type="hidden" id="tipopago" name="tipopago" value="1">
                     <input type="hidden" id="egreso_id" name="egreso_id" value="0">
                     <div class="form-group">
                        <label for="serviceTitle">Fecha *</label>
                        <input type="date" id="fechap" name="fechap" class="form-control" required>
                    </div>

                     <div class="table-container">
                    <table class="tabla-egresos">
                    <thead>
                    <tr>
                        <th class="col-talla">Razon</th>
                        <th class="col-detalle">Detalle</th>
                        <th class="col-cantidad">Monto</th>
                        <th class="col-detalle">Respaldo</th>
                        <th class="col-anular">Anular</th>

                    </tr>
                    </thead>
                    <tbody id="body_egresos_tabla">
                    </tbody>
                    <tfoot class="table-active text-right" >
                                  <tr>
                                        <td align="center"> <button type="button" class="btn btn-sm" id="btn-addFilaegresos"> <span class="fa fa-plus"></span> </button></td>
                                        <td>Totales</td>
                                        <td><input type="text" class="form-control-plaintext text-right" id="total_monto" name="total_monto" value="0.00" disabled></td>
                                        <td>&nbsp;</td>


                                  </tr>

                              </tfoot>
                    </table>
                </div>`);






    });



   $(document).on("click", "#editar_pago", function () {

            let valor = $(this).attr("data");

        return $.ajax({
                url: host + "/configuracion/editar_pago/"+valor + "/",
                method: "GET",
                dataType: "json",
                success: function (response) {

                     $("#egresoModalTitle").text("Editar Pago");
                     $("#body_egresos").html(response.resultado);
                     $("#egresoModal").addClass("active");

                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });




    });


$(document).on("click", "#btn-addFilaegresos", function () {

    let nuevaFilaegresos = `
        <tr>
            <td class="col-talla">
                <input type="text" class="form-control titulae" name="titulae[]">
            </td>
            <td class="col-detalle"><textarea class="form-control detallee" name="detallee[]"></textarea></td>
            <td class="col-cantidad"><input type="text" class="form-control montoe" name="montoe[]"></td>
            <td class="col-detalle"><input type="file" class="form-control respaldoe" name="respaldoe[]"></td>
            <td align="center">
                <button type="button" class="btn btn-danger btn-eliminarFilae btn-sm">
                    <span class="fa fa-times"></span>
                </button>
            </td>
        </tr>
    `;

    $("#body_egresos_tabla").append(nuevaFilaegresos);
});


    $(document).on("click", ".btn-eliminarFilae", function() {
        $(this).closest("tr").remove();
        calcularTotalese();
    });





      function calcularTotalese() {

            let totalmonto = 0;
            $("#body_egresos_tabla tr").each(function () {
                let monto = parseFloat($(this).find(".montoe").val()) || 0;
                totalmonto = totalmonto + (monto);
            });

            $("#total_monto").val(totalmonto.toFixed(2));


    }





     $(document).on("input", ".montoe", function () {

          let valor = parseFloat($(this).val());

            if (valor < 0) {
                $(this).val(0);
                alert("No se permiten valores negativos.");
            }else{
                calcularTotalese();
            }

        });





let dataTable_egresos;
let dataTableinicializado_egresos = false;

        function listar_pagos(){


            var contador=1;
              return $.ajax({
                url: host + "/configuracion/lista_pagos/",
                method: "GET",
                dataType: "json",
                success: function (response) {
                    let content = "";

                    response.tareas.forEach((tarea) => {
                         const cotizacion = tarea.cotizacion ? "CTG" + tarea.cotizacion : "";

                         content += `
                         <tr>

                          <td>${contador}</td>
                    <td><strong>${tarea.titular}</strong></td>
                     <td><strong>${cotizacion}</strong></td>
                    <td><strong>${tarea.fecha}</strong></td>
                    <td>${tarea.detalle.substring(0, 100)}${tarea.detalle.length > 100 ? '...' : ''}</td>
                     <td>${tarea.monto}</td>
                        <td>
                        <div style="width: 80px; height: 50px; overflow: hidden; border-radius: 4px;">
                            <a href="${host}/static/biblioteca/pagos/${tarea.respaldo}" target="_blank"><img src="${host}/static/biblioteca/pagos/${tarea.respaldo}" alt="${tarea.titular}" style="width: 100%; height: 100%; object-fit: cover;"></a>
                        </div>
                    </td>


                    <td>
                        <div class="actions">

                         <a class="action-btn info-btn edit-service" id="ver_pago" href="${host}/configuracion/ver_pago/${tarea.id}/" target="_blank">
                                <i class="fas fa-coins"></i> Imprimir
                            </a>


                            <a class="action-btn edit-btn edit-service" id="editar_pago" data="${tarea.id}">
                                <i class="fas fa-edit"></i> Editar
                            </a>
                            <a class="action-btn delete-btn delete-service" id="eliminar_pago" data="${tarea.id}">
                                <i class="fas fa-trash"></i> Eliminar
                            </a>
                        </div>
                    </td>
                    </tr>
                `;
                 contador++;


                    });

                    $("#egresoTableBody").html(content);


                    Iniciar_tabla_egresos();


                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });



        }



const dataTableOptions_egresos = {

            dom: 'Bfrtip',
            buttons: [
                                    {
                                      extend: 'excelHtml5',
                                      text: '📊 Excel' ,
                                      title: 'Reporte de Pagos',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5,6]
                                      }
                                    },
                                    {
                                      extend: 'csvHtml5',
                                      text: '📄 CSV',
                                      title: 'Reporte de Pagos',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5,6]
                                      }
                                    },
                                    {
                                      extend: 'pdfHtml5',
                                      text: '📕 PDF' ,
                                      title: 'Reporte de Pagos',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5,6]
                                      }
                                    },

                                    {
                                      extend: 'print',
                                      text: '🖨️ Imprimir' ,
                                      title: 'Reporte de Pagos',
                                      exportOptions: {
                                        columns: [0,1,2,3,4,5,6]
                                      }
                                    }
                                  ],
            language: {
                          url: "https://cdn.datatables.net/plug-ins/1.13.8/i18n/es-ES.json"
                        }
};

;


const Iniciar_tabla_egresos = () => {
    if (dataTableinicializado_egresos) {
        dataTable_egresos.destroy();
    }


        dataTable_egresos = $('#egresoTable').DataTable(dataTableOptions_egresos);
        dataTableinicializado_egresos = true;

};

$(document).on("click", "#eliminar_pago", function () {

        let valor = $(this).attr("data");


        Swal.fire({
            title: "¿Estás seguro de eliminar el pago?",
            text: "Esta acción no se puede deshacer.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#d33",
            cancelButtonColor: "#3085d6",
            confirmButtonText: "Sí, eliminar",
            cancelButtonText: "Cancelar"
        }).then((result) => {
            if (result.isConfirmed) {

               return $.ajax({
                    url: host + "/configuracion/eliminar_pago/" + valor + "/",
                    method: "GET",
                    dataType: "json",
                    success: function (response) {
                        Swal.fire({
                            title: "Eliminado",
                            text: "El pago se ha sido eliminado correctamente.",
                            icon: "success",
                            confirmButtonColor: "#3085d6",
                            confirmButtonText: "OK"
                        }).then(() => {
                            location.reload(); // Recargar la página o actualizar la tabla
                        });
                    },
                    error: function (xhr, status, error) {
                        Swal.fire({
                            title: "Error",
                            text: "Hubo un problema al eliminar el pago.",
                            icon: "error",
                            confirmButtonColor: "#d33",
                            confirmButtonText: "Cerrar"
                        });
                    }
                });
            }
        });


        });




   $(document).on("click", "#cancelegresoBtn", function () {

          $("#egresoModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });


   $(document).on("click", "#closeegresoModal", function () {

           $("#egresoModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });



 /***************************************************** SETTINGS *******************************************/

   $(document).on("click", "#settings", function () {

          $(".admin-section").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria
        $(".botones").removeClass("active");
    // Luego agrega la clase 'active' solo al botón clickeado
    $("#settings_tabla").addClass("active");
     $("#settings").addClass("active");

        listar_usuarios();
    });





 $(document).on("click", "#agregar_usuario", function () {



                 $("#UsuarioModalTitle").html("Agregar Nuevo Usuario");
                $("#UsuarioModal").addClass("active");



    });


   $(document).on("click", "#editar_usuario", function () {

            let valor = $(this).attr("data");

        return $.ajax({
                url: host + "/configuracion/editar_usuario/"+valor + "/",
                method: "GET",
                dataType: "json",
                success: function (response) {

                     $("#UsuarioModalTitle").text("Editar Usuario");
                     $("#modalbody_usuarios").html(response.resultado);
                     $("#UsuarioModal").addClass("active");

                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });




    });


let dataTable_usuarios;
let dataTableinicializado_usuarios = false;

        function listar_usuarios(){


            var contador=1;
              return $.ajax({
                url: host + "/configuracion/lista_usuarios/",
                method: "GET",
                dataType: "json",
                success: function (response) {
                    let content = "";
                    let cargo="";
                    response.tareas.forEach((tarea) => {
                        if(tarea.cargo == '1'){
                           cargo="Administrador";
                        }else{
                            cargo="Trabajador";
                        }
                         content += `
                         <tr>

                          <td>${contador}</td>
                    <td><strong>${tarea.nombre}</strong></td>
                    <td><strong>${tarea.correo}</strong></td>
                    <td>${tarea.username}</td>
                    <td>${tarea.password}</td>
                    <td>${cargo}</td>

                    <td>
                        <div class="actions">


                            <a class="action-btn edit-btn edit-service" id="editar_usuario" data="${tarea.id}">
                                <i class="fas fa-edit"></i> Editar
                            </a>
                            <a class="action-btn delete-btn delete-service" id="eliminar_usuario" data="${tarea.id}">
                                <i class="fas fa-trash"></i> Eliminar
                            </a>
                        </div>
                    </td>
                    </tr>
                `;
                 contador++;


                    });

                    $("#Body_usuarios").html(content);


                    Iniciar_tabla_usuarios();


                },
                error: function (xhr, status, error) {
                    alert("Error al obtener los datos: " + error);
                }
            });



        }



const dataTableOptions_usuarios = {

            dom: 'Bfrtip',
            buttons: [
                                    {
                                      extend: 'excelHtml5',
                                      text: '📊 Excel' ,
                                      title: 'Reporte de Usuarios',
                                      exportOptions: {
                                        columns: [0,1,2,3,4]
                                      }
                                    },
                                    {
                                      extend: 'csvHtml5',
                                      text: '📄 CSV',
                                      title: 'Reporte de Usuarios',
                                      exportOptions: {
                                        columns: [0,1,2,3,4]
                                      }
                                    },
                                    {
                                      extend: 'pdfHtml5',
                                      text: '📕 PDF' ,
                                      title: 'Reporte de Usuarios',
                                      exportOptions: {
                                        columns: [0,1,2,3,4]
                                      }
                                    },

                                    {
                                      extend: 'print',
                                      text: '🖨️ Imprimir' ,
                                      title: 'Reporte de Usuarios',
                                      exportOptions: {
                                        columns: [0,1,2,3,4]
                                      }
                                    }
                                  ],
            language: {
                          url: "https://cdn.datatables.net/plug-ins/1.13.8/i18n/es-ES.json"
                        }
};



const Iniciar_tabla_usuarios = () => {
    if (dataTableinicializado_usuarios) {
        dataTable_usuarios.destroy();
    }


        dataTable_usuarios = $('#tabla_usuarios').DataTable(dataTableOptions_usuarios);
        dataTableinicializado_usuarios = true;

};

$(document).on("click", "#eliminar_usuario", function () {

        let valor = $(this).attr("data");


        Swal.fire({
            title: "¿Estás seguro de eliminar el usuario?",
            text: "Esta acción no se puede deshacer.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#d33",
            cancelButtonColor: "#3085d6",
            confirmButtonText: "Sí, eliminar",
            cancelButtonText: "Cancelar"
        }).then((result) => {
            if (result.isConfirmed) {

               return $.ajax({
                    url: host + "/configuracion/eliminar_usuario/" + valor + "/",
                    method: "GET",
                    dataType: "json",
                    success: function (response) {
                        Swal.fire({
                            title: "Eliminado",
                            text: "El usuario ha sido eliminada correctamente.",
                            icon: "success",
                            confirmButtonColor: "#3085d6",
                            confirmButtonText: "OK"
                        }).then(() => {
                            location.reload(); // Recargar la página o actualizar la tabla
                        });
                    },
                    error: function (xhr, status, error) {
                        Swal.fire({
                            title: "Error",
                            text: "Hubo un problema al eliminar el usuario.",
                            icon: "error",
                            confirmButtonColor: "#d33",
                            confirmButtonText: "Cerrar"
                        });
                    }
                });
            }
        });


        });




   $(document).on("click", "#boton_cancelar_usuario", function () {

          $("#UsuarioModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });


   $(document).on("click", "#closeusuarioModal", function () {

           $("#UsuarioModal").removeClass("active"); // Asumo que todos los botones tienen la clase btn-categoria


    });



/****************************************** detalle **************************************/






$(document).on("click", "#agrega_comentario", function () {


    let id_auto = $(this).attr("data");




    return $.ajax({
        url:host+"/configuracion/detalle_cotizacion/comentarios_cotizacion/"+ id_auto + "/",
        method: "GET",
        dataType: "json",
        success: function (respuesta) {


            $("#contenido_modal_seguimientos_audiencia").html(respuesta.respuesta);

            $("#modal_detalle").addClass("active");


            $('#comentarea').summernote({
                height: 200
            });



        }
    });

});




$(document).on("click", "#agrega_material", function () {


    let id_auto = $(this).attr("data");




    return $.ajax({
        url:host+"/configuracion/detalle_cotizacion/adjuntos_cotizacion/"+ id_auto + "/",
        method: "GET",
        dataType: "json",
        success: function (respuesta) {


            $("#contenido_modal_seguimientos_audiencia").html(respuesta.respuesta);

            $("#modal_detalle").addClass("active");


        }
    });

});


$(document).on("click", "#firmar_contrato", function () {


    let id_auto = $(this).attr("data");




    return $.ajax({
        url:host+"/configuracion/detalle_cotizacion/firmar_contrato/"+ id_auto + "/",
        method: "GET",
        dataType: "json",
        success: function (respuesta) {


            $("#contenido_modal_seguimientos_audiencia").html(respuesta.respuesta);

            $("#modal_detalle").addClass("active");


        }
    });

});


$(document).on("click", "#gastos_cotizacion", function () {


    let id_auto = $(this).attr("data");

   $("#egresoModal").addClass("active");
    $("#cotizacion_id").val(id_auto);


});





$(document).on("click", "#revertir_contrato", function () {


    let id_auto = $(this).attr("data");




    return $.ajax({
        url:host+"/configuracion/detalle_cotizacion/revertir_contrato/"+ id_auto + "/",
        method: "GET",
        dataType: "json",
        success: function (respuesta) {

        toastr.success(respuesta.respuesta, "ALERTA", {
                        timeOut: 5000,
                        closeButton: true,
                        progressBar: true
                    });
        location.reload();
        }
    });

});






$(document).on("click", "#eliminar_gastos", function () {

        let valor = $(this).attr("data");


        Swal.fire({
            title: "¿Estás seguro de eliminar el pago?",
            text: "Esta acción no se puede deshacer.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#d33",
            cancelButtonColor: "#3085d6",
            confirmButtonText: "Sí, eliminar",
            cancelButtonText: "Cancelar"
        }).then((result) => {
            if (result.isConfirmed) {

               return $.ajax({
                    url: host + "/configuracion/eliminar_pago/" + valor + "/",
                    method: "GET",
                    dataType: "json",
                    success: function (response) {
                        Swal.fire({
                            title: "Eliminado",
                            text: "El pago se ha sido eliminado correctamente.",
                            icon: "success",
                            confirmButtonColor: "#3085d6",
                            confirmButtonText: "OK"
                        }).then(() => {
                            location.reload(); // Recargar la página o actualizar la tabla
                        });
                    },
                    error: function (xhr, status, error) {
                        Swal.fire({
                            title: "Error",
                            text: "Hubo un problema al eliminar el pago.",
                            icon: "error",
                            confirmButtonColor: "#d33",
                            confirmButtonText: "Cerrar"
                        });
                    }
                });
            }
        });


        });


$(document).on("click", "#eliminar_adjuntos", function () {

        let valor = $(this).attr("data");


        Swal.fire({
            title: "¿Estás seguro de eliminar?",
            text: "Esta acción no se puede deshacer.",
            icon: "warning",
            showCancelButton: true,
            confirmButtonColor: "#d33",
            cancelButtonColor: "#3085d6",
            confirmButtonText: "Sí, eliminar",
            cancelButtonText: "Cancelar"
        }).then((result) => {
            if (result.isConfirmed) {

               return $.ajax({
                    url: host + "/configuracion/detalle_cotizacion/eliminar_adjuntos/" + valor + "/",
                    method: "GET",
                    dataType: "json",
                    success: function (response) {
                        Swal.fire({
                            title: "Eliminado",
                            text: "Ha sido eliminado correctamente.",
                            icon: "success",
                            confirmButtonColor: "#3085d6",
                            confirmButtonText: "OK"
                        }).then(() => {
                            location.reload(); // Recargar la página o actualizar la tabla
                        });
                    },
                    error: function (xhr, status, error) {
                        Swal.fire({
                            title: "Error",
                            text: "Hubo un problema al eliminar.",
                            icon: "error",
                            confirmButtonColor: "#d33",
                            confirmButtonText: "Cerrar"
                        });
                    }
                });
            }
        });


        });

$(document).on("click", "#cancel-btn-comentarios", function () {

           $("#modal_detalle").removeClass("active");

});


// Si necesitas limpiar Summernote cuando se cierra el modal
$('#modal_detalle').on('hidden.bs.modal', function () {
    $('#comentarea').summernote('destroy');
});



$(document).on("change","#fileInput",function() {
    const fileName = document.getElementById('fileName');

    if (this.files && this.files.length > 0) {
        const file = this.files[0];
        fileName.textContent = `${file.name} (${formatBytes(file.size)})`;

        // Cambiar color del nombre
        fileName.style.color = '#04111C';
        fileName.style.borderColor = '#00ffaa';

        // Feedback visual
        fileName.classList.add('pulse');
        setTimeout(() => fileName.classList.remove('pulse'), 300);
    } else {
        fileName.textContent = 'No se ha seleccionado ningún archivo';
        fileName.style.color = '#00ffff';
        fileName.style.borderColor = '#008866';
    }
});


function formatBytes(bytes, decimals = 2) {
    if (bytes === 0) return '0 Bytes';
    const k = 1024;
    const dm = decimals < 0 ? 0 : decimals;
    const sizes = ['Bytes', 'KB', 'MB', 'GB'];
    const i = Math.floor(Math.log(bytes) / Math.log(k));
    return parseFloat((bytes / Math.pow(k, i)).toFixed(dm)) + ' ' + sizes[i];
}


/************************************* categoria ************************/





});

