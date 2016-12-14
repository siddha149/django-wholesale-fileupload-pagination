$(document).ready(function() {
$("img").hide();
$('#myfile').change(function() {
    var file_size = this.files[0].size;
    var file_type = this.files[0].type;

    $.ajax({
                url : "/wholesale/customer/fileupload/validate/",
                type: "POST",
                data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
                        file_size : file_size,
                        file_type : file_type,
                        },
                success: function( str ){
                            $('#file_err').text(str);
                        },
                error: function(xhr, textStatus, errorThrown) {
                            alert("Please report this error: "+errorThrown+xhr.status+xhr.responseText);
                        }
                });

   });

$('#submit_file').click(function(){
$("img").show();
});
});



