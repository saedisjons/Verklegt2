$(document).ready(function() {
    $('search-btn').on( 'click', function(e) {
        e.preventDefault();
        var searchText = $('#search-box').val();
        $.ajax({
            url: '/items?search_filter=' + searchText,
            type: 'GET',
            success: function(resp) {
                var newHTML = resp.data.map(d => {
                    return `<div class="well item">
                                <a href="/items/${d.id}">
                                    <img class="item-img" src="${d.firstImage}" />
                                    <h4>${d.name}</h4>
                                    <p>${d.description}</p>
                                </a>
                            </div>`
                });
                $('.items').html(newHTML.join(''));
                $('search-box').val('');
            },
            error: function(xhr, status, error) {
                // TODO: show toastr
                console.error(error);
            }
        })
    });
});