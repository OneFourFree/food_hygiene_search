function getUrlVars()
{
    var vars = [], hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for(var i = 0; i < hashes.length; i++)
    {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}

function textFilter() {

  $('input.search-field').keyup(function() {

      $.ajax({
        data: {
            search_text : $('input.search-field').val(),
            pc : getUrlVars()["postcode"]
//            rating : $('fieldset.rating input:checked').val()
        },
        type: "POST",
        url: "/filters",
//        success: searchSuccess,
        dataType: 'html'
      })
      .done(function(data) {
      $('.listings').html(data)
      });
  })
}

function hygieneRating() {
  $("fieldset.rating input").click(function() {

    $.ajax({
        data: {
            search_text : $('input.search-field').val(),
            pc : getUrlVars()["postcode"],
            rating : $('fieldset.rating input:checked').val()
        },
        type: "POST",
        url: "/filters",
//        success: searchSuccess,
        dataType: 'html'
      })
      .done(function(data) {
      $('.listings').html(data)
      });
  });
}

function businessType() {
  $("#ul-business-type li label input").click(function() {

    var typeID = $(this).attr("data-business-type");
    // alert(typeID);
    $('.restaurant-entry').filter(function() {
      $(this).toggle(
        $(this).attr("data-business-type") == typeID)
    });


    // if( $(this).is(':checked') ) alert("checked");
  });
}

$(document).ready(function() {
  textFilter();
  hygieneRating();
  businessType();
});

