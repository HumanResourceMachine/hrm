$(function() {
    $("#submit").submit(function() {
        $.ajax({
            url: "/users",
            type: "POST",
            data: {
                "username": $("#username").val(),
                "password": $("#password").val(),
                "email": $("#email").val()
            },
            success: function(data) {
                if (data["verdict"]==="error") {
                    alert(message);
                }
            },
            error: function() {

            }
        });
    });
});