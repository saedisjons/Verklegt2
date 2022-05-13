$(document).ready(function() {
    let csrftoken = $.cookie('csrftoken');

    function csrfSafeMethod(method) {
        // these HTTP methods do not require CSRF protection
        return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
    }

    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        }
    });

    let tab = $('#confirm-order-tab');
    tab.click(function() {
        // Get values from the contactInfo, paymentDetails and rating forms
        let streetName = $('#id_streetName').val()
        let houseNumber = $('#id_houseNumber').val()
        let city = $('#id_city').val()
        let postCode = $('#id_postCode').val()
        let country = $('#id_country').val()

        let nameOfCardHolder = $('#id_nameOfCardH').val()
        let cardNumber = $('#id_cardNum').val()
        let expirationDate = $('#id_expDate').val()
        let cvv = $('#id_cvv').val()

        let rating = $('#id_rating').val()

        // Populate the confirm order page with the values from the forms
        $('#contact-info-address-field').text(streetName + " " + houseNumber)
        $('#contact-info-city-field').text(city)
        $('#contact-info-postCode-field').text(postCode)
        $('#contact-info-country-field').text(country)

        $('#payment-details-cardHolder-field').text(nameOfCardHolder)
        $('#payment-details-cardNumber-field').text(cardNumber)
        $('#payment-details-expirationDate-field').text(expirationDate)
        $('#payment-details-cvv-field').text(cvv)

        $('#rating-field').text(rating)

    })

    let confirmOrderBtn = $('#confirm-order-btn');
    confirmOrderBtn.click(function() {
        console.log("confirming order..");
        let url = window.location.href;
        let n = url.lastIndexOf('/');
        let orderId = url.substring(n + 1);
        console.log(orderId);
        // Get values from the contactInfo, paymentDetails and rating forms
        let streetName = $('#id_streetName').val()
        let houseNumber = $('#id_houseNumber').val()
        let city = $('#id_city').val()
        let postCode = $('#id_postCode').val()
        let country = $('#id_country').val()

        let nameOfCardHolder = $('#id_nameOfCardH').val()
        let cardNumber = $('#id_cardNum').val()
        let expirationDate = $('#id_expDate').val()
        let cvv = $('#id_cvv').val()

        let rating = $('#id_rating').val()

        let sellerId = $('#item-userId').text()

        console.log("this is seller: ", sellerId)

        let body = {
            'orderId': orderId,
            'streetName': streetName,
            'houseNumber': houseNumber,
            'city': city,
            'postCode': postCode,
            'country': country,
            'nameOfCardHolder': nameOfCardHolder,
            'cardNumber': cardNumber,
            'expirationDate': expirationDate,
            'cvv': cvv,
            'rating': rating,
            'sellerId': sellerId
        };

        console.log(body)

        // Post to server
        $.ajax({
            url: "/orders/confirm_order",
            type: "POST",
            data: body,
            contentType: "application/json; charset=utf-8",
            dataType: "json",
            success: function () {
            }
        });

});
});