function getUrlVars() {
    var vars = [],
        hash;
    var hashes = window.location.href.slice(window.location.href.indexOf('?') + 1).split('&');
    for (var i = 0; i < hashes.length; i++) {
        hash = hashes[i].split('=');
        vars.push(hash[0]);
        vars[hash[0]] = hash[1];
    }
    return vars;
}

// Call the function view and update page HTML
function filterResults() {
    // check that the rating key actually contains data
    var ratingKey;
    if ($('fieldset.rating input:checked').val()) {
        ratingKey = $('fieldset.rating input:checked').val();
    } else {
        ratingKey = '';
    }

    //

    //  Fetch new data and replace HTML results
    $.ajax({
            data: {
                search_text: $('input.search-field').val(),
                pc: getUrlVars()["postcode"],
                rating: ratingKey
            },
            type: "POST",
            url: "/filters",
            //        success: searchSuccess,
            dataType: 'html'
        })
        .done(function(data) {
            $('.results-container').html(data);
            updateTotalCount();
        });


}

function updateTotalCount() {
    var total_count = $('div.results-list').attr("data-total-restaurants");
    $("strong#total-count").text(total_count);
};

$('input.search-field').keyup(function() {
    filterResults();
});

$("fieldset.rating input").click(function() {
    filterResults();
});

// Uncheck any checked ratings checkboxes
$("#js-reset-rating").click(function() {
    $('fieldset.rating input:checked').each(
        function() {
            $(this).attr("checked", false);
        }
    );
    filterResults();
});