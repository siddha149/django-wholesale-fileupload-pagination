$( document ).ready(function() {
    $("td").blur(function(){
        var handle = $(this);
        var id = handle.attr("id");
        var oid = id.substr(3);
        var qty = document.getElementById(id).innerHTML;
        //alert("oid=" + oid + " qty=" +qty);
        $.ajax({
                url : "/wholesale/customer/changeorder/",
                type: "POST",
                data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
                        oid : oid,
                        qty : qty,
                        },
                success: function( str ){
                            qty = str.substr(0,str.indexOf(' '));
                            Total = str.substr(str.indexOf(' ')+1);
                            //alert("Successfully changed order quantity to " + qty);
                            $("#Amount"+oid).html(Total);
                        },
                error: function(xhr, textStatus, errorThrown) {
                            alert("Please report this error: "+errorThrown+xhr.status+xhr.responseText);
                        }
                });
    });
});

function deleterow(num,cid){
        $("#ord"+num).hide();
        oid = document.getElementById("id"+num).innerHTML;
        pname = document.getElementById("Pid"+num).innerHTML;
        qty = document.getElementById("Qty"+num).innerHTML;
        //alert("Deleting Oid=" + oid + " Pname=" + pname + " qty=" + qty);
        $.ajax({
            url : "/wholesale/customer/deleteorder/",
            type: "POST",
            data : {csrfmiddlewaretoken: document.getElementsByName('csrfmiddlewaretoken')[0].value,
                    oid : oid,
                    },
            success: function( oid ){
                alert("Successfully deleted order " + oid);
                },
             error: function(xhr, textStatus, errorThrown) {
                alert("Please report this error: "+errorThrown+xhr.status+xhr.responseText);
                }
            });
     };


