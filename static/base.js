$(function() {
    $.ajax({
        url: "/test/users",
        type: "GET",
        success: function(data) {
            $("#navbar"+data["role"]).css("display", "block");
            $("#username").html(data["username"]);
            var bar = $("#navbar" + data["role"]);
            bar.find("a").each(function() {
                console.log($(this).attr("href"));
                console.log(window.location.pathname);
                var href = $(this).attr("href");
                if (href == window.location.pathname || href+"/" == window.location.pathname) {
                    $(this).addClass("active");
                }
            });
        }
    })
});