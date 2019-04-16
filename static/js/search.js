var API_URL = "http://localhost:5000/";

const delay1 = "0.3s";
const delay2 = "0.6s";
const delay3 = "0.9s";

function onSearch() {
    var userQuery = $("#search").val().split(" ").join(",");

    // var timeFilter = $("#time").change(function(e) {
    //     var text = $("#time :selected").text();
    //     $("#DropDownList2").html(options);
    //     if(text == "All") return;
    //     $('#DropDownList2 :not([value^="' + text.substr(0, 3) + '"])').remove();
    // });​

    // search?q=foo&time=123

    var INF = 9999;

    var time_option = {
        "1" : [0, 29],
        "2": [0, 59],
        "3": [0, INF]
    };

    var time_filter = [0, INF];

    console.log(time_filter);

    var minTime = time_filter[0];
    var maxTime = time_filter[1];

    var rating = 1;
    var review_count = 1;

    $.ajax(
        {
            url: API_URL + "search?q=" + userQuery + "&minTime=" + minTime + "&maxTime="+ maxTime + "&rating=" + rating + "&review_count=" + review_count,
            crossDomain: true,
            beforeSend: function(xhr){
                xhr.withCredentials = true;
            }
        }).done(function(results) {
        console.log(results);
        console.log(typeof results);

        var html = "";

        html += "<h2>Found " + results['total'] + " recipes</h2>"


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
                    "../data/allrecipes/images/userphotos/" + recipe.image + "\" alt=\"" + recipe.title + "\" height=\"250\" width=\"250\">" +
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
