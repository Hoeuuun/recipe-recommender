/*
for now, limit to 12 results; later, figure out how to load more
as user clicks/loads next page


			 put all of this in a function using recipes url id; note 3 separate chunks for the 3 columns
			<div class="col-md-4 col-sm-4 wow fadeInUp" data-wow-delay="0.3s">
				<a href="images/gallery-img1.jpg" data-lightbox-gallery="zenda-gallery"><img src="images/gallery-img1.jpg" alt="gallery img"></a>
				<div>
					<h3>Lemon-Rosemary Prawn</h3>
					<span>Seafood / Shrimp / Lemon</span>
				</div>
				<a href="images/gallery-img2.jpg" data-lightbox-gallery="zenda-gallery"><img src="images/gallery-img2.jpg" alt="gallery img"></a>
				<div>
					<h3>Lemon-Rosemary Vegetables</h3>
					<span>Tomato / Rosemary / Lemon</span>
				</div>
			</div>
			<div class="col-md-4 col-sm-4 wow fadeInUp" data-wow-delay="0.6s">
				<!--<a href="images/gallery-img3.jpg" data-lightbox-gallery="zenda-gallery"><img src="images/gallery-img3.jpg" alt="gallery img"></a>-->
				<a href="data/allrecipes/images/userphotos/250x250/398.jpg" data-lightbox-gallery="zenda-gallery"><img src="data/allrecipes/images/userphotos/250x250/398.jpg" alt="gallery img"></a>
				<div>
					<h3>Lemon-Rosemary Bakery</h3>
					<span>Bread / Rosemary / Orange</span>
				</div>
			</div>
			<div class="col-md-4 col-sm-4 wow fadeInUp" data-wow-delay="0.9s">
				<a href="images/gallery-img4.jpg" data-lightbox-gallery="zenda-gallery"><img src="images/gallery-img4.jpg" alt="gallery img"></a>
				<div>
					<h3>Lemon-Rosemary Salad</h3>
					<span>Chicken / Rosemary / Green</span>
				</div>
				<a href="images/gallery-img5.jpg" data-lightbox-gallery="zenda-gallery"><img src="images/gallery-img5.jpg" alt="gallery img"></a>
				<div>
					<h3>Lemon-Rosemary Pizza</h3>
					<span>Pasta / Rosemary / Green</span>
				</div>
			</div>
		</div>
 */

// for-loop to populate the results section with recipes
for (i=0; i<12; i++) {
    document.getElementById("search_results").innerHTML += "<div class=\"col-md-4 col-sm-4 wow fadeInUp\" data-wow-delay=\"0.3s\">" +
                                                                        "<a href=\"images/gallery-img1.jpg\" data-lightbox-gallery=\"zenda-gallery\"><img src="recipes.image.jpg" alt=\"gallery img\"></a>" +
                                                                        "<div>" +
                                                                            "<h3>recipe.title</h3>" +
                                                                            "<span>recipe.ingredients.join("<br>"</span>" +
                                                                        "</div>" +
                                                                    "</div>"

}
