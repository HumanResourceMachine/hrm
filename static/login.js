$(function() {
    //alert('ok');
    $("#submit").click(function() {
        $.ajax({
            //------------注意：url最后要改成接口文件中定义的-------------
            url: "/users/login",
            type: "POST",
            data: {
                "username": $("#username").val(),
                "role": $("#role").val(),
                "password": $("#password").val()
            },
            success: function(data) {

                if (data["verdict"]==="error") {
                    alert(data["message"]);
                } else {
                    window.location.href = "/index";
                }

            },
            error: function() {

            }
        });
    });
});