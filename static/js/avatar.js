

$(function(){
    $('#id_foto').change(function(e){
        handleFileSelect(e);
    });
    $("#avatar").click(function() {
        $('#id_foto').click();
    });

});

function handleFileSelect(evt) {

    var files = evt.target.files[0]; // FileList object

    if (files.type == 'image/jpg' || files.type == 'image/jpeg' || files.type == 'image/png' || files.type == 'image/gif') {
        var reader = new FileReader();
        // Closure to capture the file information.
        reader.onload = (function (theFile) {
            return function (e) {
                var image = new Image();
                image.src = e.target.result;
                image.onload = function () {
                    var canvas = document.createElement('canvas');
                    var ctx = canvas.getContext("2d");
                    ctx.drawImage(image, 0, 0);
                    var MAX_WIDTH = 800;
                    var MAX_HEIGHT = 800;
                    var width = image.width;
                    var height = image.height;

                    if (width > height) {
                        if (width > MAX_WIDTH) {
                            height *= MAX_WIDTH / width;
                            width = MAX_WIDTH;
                        }
                    } else {
                        if (height > MAX_HEIGHT) {
                            width *= MAX_HEIGHT / height;
                            height = MAX_HEIGHT;
                        }
                    }
                    canvas.width = width;
                    canvas.height = height;
                    var ctx = canvas.getContext("2d");
                    ctx.drawImage(this, 0, 0, width, height);

                    var dataurl = canvas.toDataURL("image/jpg");
                    /*es la imagen que se muestra en el primer momento que cargan el formulario de subir imagenes*/

                    $('#avatar').attr('src', dataurl);

                    document.getElementById('hidden_avatar').value = dataurl;


                };
            };
        })(files);
        // Read in the image file as a data URL.
        reader.readAsDataURL(files);

        //}
    }else{
        toastr.error("Archivo no soportado")
    }

}