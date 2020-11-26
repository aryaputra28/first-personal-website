// Untuk accordion

$(document).ready(function(){
    $('.accordion-title').click(function(){
      $(this).next().next().slideToggle();
    });
  });
  

// Untuk up 
$('.accordion-button-up').click(function(){
  var thisAccordion = $(this).parent().parent().parent();
  thisAccordion.insertBefore(thisAccordion.prev()).hide().show('slow');;
})

// Untruk down
$('.accordion-button-down').click(function(){
  var thisAccordion = $(this).parent().parent().parent();
  thisAccordion.insertAfter(thisAccordion.next()).hide().show('slow');;
})

