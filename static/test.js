function a() {

}
$(function() {
    alert("test");
    var a = {};
    a[0] = 1;
    a[1] = 2;
    $.ajax({
        url: "/x",
        type: "POST",
        data: {
            "username": "test",
            "password": "test",
            "email": "test"
        },
        success: function(data) {
            data["message"];
        },
        error: function() {

        }
    });
    alert("1");
});