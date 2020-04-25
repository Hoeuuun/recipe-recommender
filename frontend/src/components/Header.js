import React from 'react';

export function Header() {
    return (
        <section class="navbar navbar-default navbar-fixed-top" role="navigation">
            <div class="container">
                <div class="navbar-header">
                    <button class="navbar-toggle" data-toggle="collapse" data-target=".navbar-collapse">
                        <span class="icon icon-bar"></span>
                        <span class="icon icon-bar"></span>
                        <span class="icon icon-bar"></span>
                    </button>
                    <a href="#" class="navbar-brand">Recipe Recommender</a>
                </div>
                <div class="collapse navbar-collapse">
                    <ul class="nav navbar-nav navbar-right">
                        <li><a href="#home" class="smoothScroll">HOME</a></li>
                        <li><a href="#recipes" class="smoothScroll">RECIPES</a></li>
                        <li><a href="#contact" class="smoothScroll">CONTACT</a></li>
                    </ul>
                </div>
            </div>
        </section>
    )
}