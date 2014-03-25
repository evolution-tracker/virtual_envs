
     $(document).ready(function () {
            var top = $('#comment').offset().top - parseFloat($('#comment').css('marginTop').replace(/auto/, 0));
            $(window).scroll(function (event) {
                // what the y position of the scroll is
                var y = $(this).scrollTop();

                // whether that's below the form
                if (y >= top) {
                    // if so, ad the fixed class
                    $('#comment').addClass('fixed');
                } else {
                    // otherwise remove it
                    $('#comment').removeClass('fixed');
                }
             });
        });

    $( document ).ready( function() {
	    $( '.error_row' ).click( function() {

	        $(this).addClass('info').siblings().removeClass('info');
		    code = d3.select(this).attr('id');
		    $( '#cc' ).html( '&nbsp;' ).load( '{% url "draw_chart" %}?code=' + code+'&type=do_ec_errors' );
	    });
    });


    row_details = '{{ record_details|safe }}';

    row_details = JSON.parse(row_details);

    row_details.forEach(function(d){
        id = "#"+d.id;
        color = d.color;
        d3.select(id).classed(color,"true");
    });

