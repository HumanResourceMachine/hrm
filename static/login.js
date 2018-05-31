$(function() {
    $("#submit").submit(function() {
        $.ajax({
            url: "/users/login",
            type: "POST",
            data: {
                "username": $("#username").val(),
                "role": $("#role").val(),
                "password": $("#password").val()
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