var API_URL = "./";

// different delays depending on image's column
const delay1 = "0.3s";
const delay2 = "0.6s";
const delay3 = "0.9s";

function onSearch() {
    var userQuery = $("#search").val().split(" ").join(",");

    var INF = 9999;

    var time_option = {
        "1": [0, 29],  // < 30 mins
        "2": [0, 59],   // < 60 mins
        "3": [0, INF]   //   60+ mins
    };

    var time_filter = $("#time_drop_down").prop('selectedIndex');
    if (time_filter == 0) {
        time_filter = [0, INF];  // default time filter
    } else {
        time_filter = time_option[time_filter];
    }

    console.log(time_filter);

    var minTime = time_filter[0];
    var maxTime = time_filter[1];

    var rating = $("#rating_drop_down").prop('selectedIndex');
    var review_count = $("#review_drop_down").prop('selectedIndex');

    var URL = API_URL + "search?q=" + userQuery + "&minTime=" + minTime + "&maxTime=" + maxTime

    if (rating != 0) {
        URL += "&rating=" + rating;
    }
    if (review_count != 0) {
        URL += "&review_count=" + review_count;
    }

    var ajaxCall = $.ajax({
            url: URL
        });

    ajaxCall.done(function (results) {
        console.log(results);
        console.log(typeof results);

        var html = "";

        $("#result_count").text("Found " + results['total'] + " recipes");


        if (results['data']) {
            results['data'].forEach(function (recipe, i) {
                html += "<div class=\"col-md-4 col-sm-4 wow fadeInUp\" data-wow-delay=\"";

                // first column
                if (i % 3 == 0) {
                    html += delay1;
                }
                // second column
                if (i % 3 == 1) {
                    html += delay2;
                }
                // third column
                if (i % 3 == 2) {
                    html += delay3;
                }

                html += "\">" +
                    "</a><img src=\"" +
                    "./data/allrecipes/images/userphotos/" + recipe.image + "\" alt=\"" + recipe.title + "\" height=\"250\" width=\"250\">" +
                    "<div><h2><a href=" + recipe.url + " target=\"_blank\"> " + recipe.title + "</a>" +
                    "</h2>" +
                    "<h4> Rating: " + recipe.rating + "/100  " + "<br>" + "Time: " + recipe.time + " M " + "<br>" + "Reviews: " + recipe.review_count + "</h4>" +
                    "<span>" + recipe.ingredients.join("<br>") + "</span>" +
                    "</div></div>";

            });
        }

        $("#search_results").html(html);
    });
}

// triggers search on pressing enter key
function onSearchTyped(e) {
    if (!e) e = window.event;
    var keyCode = e.keyCode || e.which;
    //alert(keyCode);
    if (keyCode == '13') {
        onSearch();
    }
}
