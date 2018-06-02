$(function() {
    //alert('ok');
    $("#submit").click(function() {
        $.ajax({
            //------------注意：url最后要改成接口文件中定义的-------------
            url: "/users",
            type: "POST",
            data: {
                "username": $("#username").val(),
                "password": $("#password").val(),
                "email": $("#email").val()
            },
            success: function(data) {
                if (data["verdict"]==="error") {
                    alert(data["message"]);
                } else {
                    alert('Registration successful!')
                    window.location.href = "/login";
                }
            },
            error: function() {

            }
        });
    });
});