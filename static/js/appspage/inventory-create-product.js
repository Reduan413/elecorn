// Default and Convert to Decimal Value
$(document).ready(function() {

    $("#selling_price-id").val("0.00");
    $("#purchase_price-id").val("0.00");
    $("#selling_price-id").on('change', function() {
        let selling_price = $("#selling_price-id").val();
        if (selling_price == "") {
            $("#selling_price-id").val("0.00");
        } else {
            $('#selling_price-id').val(parseInt(selling_price).toFixed(2));
        }
    });
    $("#purchase_price-id").on('change', function() {
        let purchase_price = $("#purchase_price-id").val();
        if (purchase_price == "") {
            $("#purchase_price-id").val("0.00");
        } else {
            $('#purchase_price-id').val(parseInt(purchase_price).toFixed(2));
        }
    });

    // Ajax POST Request
    $("#post-form-data").on('submit', function(e) {
        e.preventDefault();
        let csrf = $("input[name=csrfmiddlewaretoken]").val();
        let postContentForm = $("#post-form-data").serializeArray();
        let data = {};
        $.each(postContentForm, function() {
            data[this.name] = this.value;
        })
        console.log(data)
        post_data = { csrfmiddlewaretoken: csrf, 'data': data }
        $.ajax({
            url: "{% url 'create_inventory_product' %}",
            method: 'POST',
            data: post_data,
            async: true,
            success: function(result) {
                console.log(data)
            }
        })
    });

    // Clear on click New
    $("#form_clear").on('click', function(e) {
        e.preventDefault();
        $('form').trigger('reset');
        let selling_price = $("#selling_price-id").val();
        if (selling_price == "") {
            $("#selling_price-id").val("0.00");
        } else {
            $('#selling_price-id').val(parseInt(selling_price).toFixed(2));
        }

        let purchase_price = $("#purchase_price-id").val();
        if (purchase_price == "") {
            $("#purchase_price-id").val("0.00");
        } else {
            $('#purchase_price-id').val(parseInt(purchase_price).toFixed(2));
        }
    });

    // End Document.Ready


});
