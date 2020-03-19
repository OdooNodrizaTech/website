odoo.define('website.index_noindex', function (require) {
"use strict";

	var ajax = require('web.ajax');

	$(document).on('click', '.js_index_noindex', function(event) {
            event.preventDefault();

            var link = $(this);
            var action = link.attr('data-index');
            
            ajax.jsonRpc('/website/index_noindex', 'call', {'index': action})
            .then(function (result) {
                
                if (action == 'index'){
                    link.attr('data-index', 'no-index');
                    $('#oe_systray .no-index').addClass('hidden');
                    $('.oe_promote_menu .no-indexed').removeClass('hidden');
                    $('.oe_promote_menu .indexed').addClass('hidden');
                }else{
                    link.attr('data-index', 'index');
                    $('#oe_systray .no-index').removeClass('hidden');
                    $('.oe_promote_menu .no-indexed').addClass('hidden');
                    $('.oe_promote_menu .indexed').removeClass('hidden');
                }
            }).fail(function (err, data) {
                
            });
    });

});