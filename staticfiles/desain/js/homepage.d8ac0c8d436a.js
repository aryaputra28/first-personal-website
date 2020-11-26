$(document).ready(function(){
    $('.accordion-title').click(function(){
      $(this).children(".arrow").children('.fa-angle-down').toggleClass('rotate-icon');
      $(this).next().slideToggle();
    });
  });
  