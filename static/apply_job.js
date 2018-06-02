$(function() {
    alert('ok');
    $("#submit").click(function() {
        $.ajax({
            url: "/users/apply_job",
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