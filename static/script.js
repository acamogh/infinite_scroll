    var tot_pag = 0;
    function myFunction() {
        $.ajax({
        url: 'http://127.0.0.1:8000/api/theme/?page=1',
        method: 'get',
        contentType: "application/json",
        success: function (res) {
            tot_pag=res.total_pages;
            for (var i = 0; i <= res.data.length; i++) {
                $("#posts").each(function (index) {
                    $(this).append("<li>" + res.data[i].theme_name + "</li>");
                });
            }
        },
            async:false,
    })
    }
    myFunction();

    // console.log(tot_pag);
    // console.log('hi')
    //
    // var win = $(window);
    // win.scroll(function () {
    //     if ($(document).height() - win.height() == win.scrollTop()) {
    //
    //     }
    // });