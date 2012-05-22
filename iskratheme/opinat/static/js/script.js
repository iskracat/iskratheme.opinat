/* Author: 

*/


$(document).ready(function() {
    // $(".section-front-page .blocsGrans").hover(
    //     function () {
    //         var png = $(this).attr("id");
    //         $("#fotoGran").css('background-image', 'url("++theme++iskratheme.opinat/imatges/'+png+'")');
    //     });
    $(".section-front-page .blocsGrans").hover(
        function () {
            $(".rodonaFletxa", this).removeClass("hidden");
            $(".lema", this).removeClass("hidden")
        },
        function () {
            $(".rodonaFletxa", this).addClass("hidden");
            $(".lema", this).addClass("hidden")
        });
    
    $(".desplegable").hover(
        function () {
          $("ul", this).removeClass("hidden");
          $("a", this).addClass("negatiu");
        },
        function () {
          $("ul", this).addClass("hidden");
          $("a", this).removeClass("negatiu");
        });

    $('#slider').nivoSlider({
        controlNav: true,
        pauseTime: 4000
    });
     $('#slider_exit').nivoSlider({
        controlNav: true,
        pauseTime: 4000
    });

});




















