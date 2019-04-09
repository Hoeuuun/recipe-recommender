var API_URL = "http://localhost:5000/";

const delay1 = "0.3s";
const delay2 = "0.6s";
const delay3 = "0.9s";

function onSearch() {
    var userQuery = $("#search").val().split(" ").join(",");
    $.ajax(
        {
            url: API_URL + "search?q=" + userQuery,
            crossDomain: true,
            beforeSend: function(xhr){
                xhr.withCredentials = true;
            }
        }).done(function(results) {
        console.log(results);
        console.log(typeof results);

        var html;

        results.forEach(function(recipe, i) {
            html += "<div class=\"col-md-4 col-sm-4 wow fadeInUp\" data-wow-delay=\"";

            // first column
            if (i == 0 || i == 3 || i == 6) {
                html += delay1;
            }
            // second column
            if (i == 1 || i == 4 || i == 7) {
                html += delay2;
            }
            // third column
            if (i == 2 || i == 5 || i == 8) {
                html += delay3;
            }

            html += "\">" +
            "</a><img src=\"" +
            "../data/allrecipes/images/userphotos/" + recipe.image + "\" alt=\"" + recipe.title + "\" height=\"250\" width=\"250\">" +
            "<div><h2><a href=" + recipe.url + " target=\"_blank\"> " + recipe.title + "</a>"  +
            "</h2>" +
            "<h3> Rating: " + recipe.rating + "/100  " + "   Time: " + recipe.time + " M</h3>" +
            "<span>" + recipe.ingredients.join("<br>") + "</span>" +
            "</div></div>";

        });

        $("#search_results").html(html);
    });
}
