import $ from "jquery";
import "slick-carousel";

$('.slick-slider').slick({
  infinity: true,
  autoplay: true,
  dots: false,
  speed: 300,
  slidesToShow: 3,
  slidesToScroll: 1,
  arrows: false,
    responsive: [
    {
      breakpoint: 1024,
      settings: {
        slidesToShow: 3,
        slidesToScroll: 1,
        infinite: true,
        dots: false
      }
    },
    {
      breakpoint: 600,
      settings: {
        infinite: true,
        dots: false,
        autoplay: true,
        slidesToShow: 1,
        slidesToScroll: 1
      }
    },
    {
      breakpoint: 480,
      settings: {
        infinite: true,
        dots: false,
        autoplay: true,
        slidesToShow: 1,
        slidesToScroll: 1
      }
    }
  ]
});
		