$(document).ready(function () {
  $('#toggle_header').click(function () {
    $('header').toggleClass('red green');
  });
});

// $(document).ready(function () {
//  $('#toggle_header').click(function () {
//    if ($('header').hasClass('green')) {
//      $('header').removeClass('green');
//      $('header').addClass('red');
//    }
//    else {
//      $('header').removeClass('red');
//      $('header').addClass('green');
//    }
//  });
// });
