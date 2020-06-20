$("document").ready(function () {
    let id;
    // console.log("Privet from JS!");
    $(".like").on("click", function () {
        // console.log("Click!");
        id = $(this).attr("id");
        // console.log(id);
        $.ajax("/hello/ajax/add_like/",
            {"data":{"id":id},
                "method":"get",
                "success":function (data) {
                    // console.log(data);
                    $("#" + id).html("Likes: " + data)
                }
        })
        })

    $(".btn-primary").on("click", function () {
        let id = $(this).attr("id");
        let val = $("#textarea" + id).val();
        // if (val.lenght > 0){} else {}
        $("#textarea" + id).val("");
        $.ajax("/hello/add_ajax_comment/",
            {"data":{"id":id, "val":val},
                "method":"get",
                "success":function (data) {
                    data = $.parseJSON(data);
                    console.log(data);
                    let row = "<i>" + val + "</i>" + "<h6>" + data['date'] + "</h6>";

                    $("#comment-container" + id).append(row)
                }});
            console.log(val)
        })




})
