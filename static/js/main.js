/*  ---------------------------------------------------
    Template Name: Ogani
    Description:  Ogani eCommerce  HTML Template
    Author: Colorlib
    Author URI: https://colorlib.com
    Version: 1.0
    Created: Colorlib
---------------------------------------------------------  */

'use strict';

(function ($) {

    /*------------------
        Preloader
    --------------------*/
    $(window).on('load', function () {
        $(".loader").fadeOut();
        $("#preloder").delay(200).fadeOut("slow");

        /*------------------
            Gallery filter
        --------------------*/
        $('.featured__controls li').on('click', function () {
            $('.featured__controls li').removeClass('active');
            $(this).addClass('active');
        });
        if ($('.featured__filter').length > 0) {
            var containerEl = document.querySelector('.featured__filter');
            var mixer = mixitup(containerEl);
        }
    });

    /*------------------
        Background Set
    --------------------*/
    $('.set-bg').each(function () {
        var bg = $(this).data('setbg');
        $(this).css('background-image', 'url(' + bg + ')');
    });

    //Humberger Menu
    $(".humberger__open").on('click', function () {
        $(".humberger__menu__wrapper").addClass("show__humberger__menu__wrapper");
        $(".humberger__menu__overlay").addClass("active");
        $("body").addClass("over_hid");
    });

    $(".humberger__menu__overlay").on('click', function () {
        $(".humberger__menu__wrapper").removeClass("show__humberger__menu__wrapper");
        $(".humberger__menu__overlay").removeClass("active");
        $("body").removeClass("over_hid");
    });

    /*------------------
		Navigation
	--------------------*/
    $(".mobile-menu").slicknav({
        prependTo: '#mobile-menu-wrap',
        allowParentLinks: true
    });

    /*-----------------------
        Categories Slider
    ------------------------*/
    $(".categories__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 4,
        dots: false,
        nav: true,
        navText: ["<span class='fa fa-angle-left'><span/>", "<span class='fa fa-angle-right'><span/>"],
        animateOut: 'fadeOut',
        animateIn: 'fadeIn',
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        responsive: {

            0: {
                items: 1,
            },

            480: {
                items: 2,
            },

            768: {
                items: 3,
            },

            992: {
                items: 4,
            }
        }
    });


    $('.hero__categories__all').on('click', function () {
        $('.hero__categories ul').slideToggle(400);
    });

    /*--------------------------
        Latest Product Slider
    ----------------------------*/
    $(".latest-product__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 1,
        dots: false,
        nav: true,
        navText: ["<span class='fa fa-angle-left'><span/>", "<span class='fa fa-angle-right'><span/>"],
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true
    });

    /*-----------------------------
        Product Discount Slider
    -------------------------------*/
    $(".product__discount__slider").owlCarousel({
        loop: true,
        margin: 0,
        items: 3,
        dots: true,
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true,
        responsive: {

            320: {
                items: 1,
            },

            480: {
                items: 2,
            },

            768: {
                items: 2,
            },

            992: {
                items: 3,
            }
        }
    });

    /*---------------------------------
        Product Details Pic Slider
    ----------------------------------*/
    $(".product__details__pic__slider").owlCarousel({
        loop: true,
        margin: 20,
        items: 4,
        dots: true,
        smartSpeed: 1200,
        autoHeight: false,
        autoplay: true
    });

    /*-----------------------
		Price Range Slider
	------------------------ */
    var rangeSlider = $(".price-range"),
        minamount = $("#minamount"),
        maxamount = $("#maxamount"),
        minPrice = rangeSlider.data('min'),
        maxPrice = rangeSlider.data('max');
    rangeSlider.slider({
        range: true,
        min: minPrice,
        max: maxPrice,
        values: [minPrice, maxPrice],
        slide: function (event, ui) {
            minamount.val('$' + ui.values[0]);
            maxamount.val('$' + ui.values[1]);
        }
    });
    minamount.val('$' + rangeSlider.slider("values", 0));
    maxamount.val('$' + rangeSlider.slider("values", 1));

    /*--------------------------
        Select
    ----------------------------*/
    $("select").niceSelect();

    /*------------------
		Single Product
	--------------------*/
    $('.product__details__pic__slider img').on('click', function () {

        var imgurl = $(this).data('imgbigurl');
        var bigImg = $('.product__details__pic__item--large').attr('src');
        if (imgurl != bigImg) {
            $('.product__details__pic__item--large').attr({
                src: imgurl
            });
        }
    });

    /*-------------------
		Quantity change
	--------------------- */
    var proQty = $('.pro-qty');
    proQty.prepend('<span class="dec qtybtn">-</span>');
    proQty.append('<span class="inc qtybtn">+</span>');
    proQty.on('click', '.qtybtn', function () {
        var $button = $(this);
        var oldValue = $button.parent().find('input').val();
        if ($button.hasClass('inc')) {
            var newVal = parseFloat(oldValue) + 1;
        } else {
            // Don't allow decrementing below zero
            if (oldValue > 0) {
                var newVal = parseFloat(oldValue) - 1;
            } else {
                newVal = 0;
            }
        }
        let input = $button.parent().find('input')
        input.val(newVal);

        // my
        let cartProductId = input.data('cart-product-id')
        if (cartProductId) {
            updateCartProductRequest(cartProductId, newVal).done(function (response) {
                updateProductTotalPrice(cartProductId, response)
                updateCartTotal()
            }).fail(ajaxErrorHandler)
        }
    });

    // my code start
    /*
    * csrf
    * */
    function getCookie(name) {
        var cookieValue = null;
        if (document.cookie && document.cookie !== '') {
            var cookies = document.cookie.split(';');
            for (var i = 0; i < cookies.length; i++) {
                var cookie = cookies[i].trim();
                // Does this cookie string begin with the name we want?
                if (cookie.substring(0, name.length + 1) === (name + '=')) {
                    cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                    break;
                }
            }
        }
        return cookieValue;
    }

    var csrftoken = getCookie('csrftoken');

    /*
    * ajax setup
    * */
    $.ajaxSetup({
        beforeSend: function (xhr) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    });

    function ajaxErrorHandler(xhr, status, error) {
        if (xhr.status === 403)
            alert('Пожалуйста авторизуйтесь')
        else {
            alert(xhr.responseJSON)
        }
    }

    const cartEndpoint = '/api/cart-products/'
    const favoriteEndpoint = '/api/favorite/'

    // обновим информацию о корзине вверху страницы
    function updateTopCartInformation(count, total) {
        $('span#cart-products-count').text(count)
        $('span#cart-products-total').text(formatToDecimal(total))
    }

    // запрос добавления товара в корзину
    function addToCartRequest(productId, qty) {
        return $.ajax({
                url: cartEndpoint,
                type: 'POST',
                data: {
                    product: productId,
                    count: qty
                }
            }
        )
    }

    // запрос получения информации о корзине
    function getCartInformationRequest() {
        return $.ajax({
                url: cartEndpoint + 'count/',
                type: 'GET',
            }
        )
    }

    function updateCartTotal() {
        getCartInformationRequest().done(function (response) {
            if (response) {
                const cartTotal = formatToDecimal(response.total)
                const cartCount = response.count
                $('#cart-total').text(cartTotal)
                updateTopCartInformation(cartCount, cartTotal)
            }
        })
    }

    /* *
    * Add product to Cart
    * */

    // from product details page
    let addToCartButton = $('#add-to-cart')
    addToCartButton.on('click', function (e) {
        e.preventDefault()
        addToCartRequest(
            $(this).data('product-id'),
            $('#qty-input').val()
        ).done(function (response) {
                updateTopCartInformation(response.count, response.total)
            }
        ).fail(ajaxErrorHandler)
    })

    // from products list page
    let addToCartLink = $('.add-to-cart')
    addToCartLink.on('click', function (e) {
        e.preventDefault()
        addToCartRequest(
            $(this).data('product-id'), 1
        ).done(function (response) {
                updateTopCartInformation(response.count, response.total)
            }
        ).fail(ajaxErrorHandler)
    })

    /*
    * Remove from cart
    * */
    let removeButton = $('.shoping__cart__item__close span.icon_close')

    function removeCartProductRequest(productId) {
        return $.ajax({
            url: cartEndpoint + productId + '/',
            type: 'DELETE',
        })
    }

    removeButton.on('click', function (e) {
        const productId = $(this).data('product-id')

        removeCartProductRequest(productId).done(function (response) {
            updateTopCartInformation(response.count, response.total)
            $('tr#product-' + productId).hide(100, function () {
                $(this).remove()
            })
            updateCartTotal()
        }).fail(ajaxErrorHandler)
    })

    /*
    * Update product cart count
    * */
    function updateCartProductRequest(productId, count) {
        return $.ajax({
            url: cartEndpoint + productId + '/',
            type: 'PATCH',
            data: {
                count: count
            }
        })
    }

    function formatToDecimal(digit) {
        return digit.toFixed(2).toString().replace(/\./g, ",")
    }

    /*
    * Recalculate cart product total
    * */

    function updateProductTotalPrice(productId, data) {
        if (data && data.product) {
            let productTotal = data.product.price * data.count
            productTotal = formatToDecimal(productTotal)
            $('tr#product-' + productId + '>td.shoping__cart__total > span').text(productTotal)
        }
    }

    // изменение количества товара в корзине
    let qtyInput = $('.pro-qty.cart input')
    qtyInput.on('paste keyup', function (e) {
        let cartProductId = $(this).data('cart-product-id')
        let count = $(this).val()

        updateCartProductRequest(cartProductId, count).done(function (response) {
            updateProductTotalPrice(cartProductId, response)
            updateCartTotal()
        }).fail(ajaxErrorHandler)
    })

    // сортировка товаров в списке
    let sortProducts = $('select#products-sort')
    sortProducts.change(function (e) {
        // https://developer.mozilla.org/en-US/docs/Web/API/URL
        const url = new URL(window.location.href)
        url.searchParams.set('sort', $(this).val())
        document.location.href = url
    })

    // подписка на новости
    function subscribeRequest(email) {
        return $.ajax({
            url: '/api/subscribe/',
            type: 'POST',
            data: {
                email: email
            }
        })
    }

    let subscribeForm = $('.footer__widget form')
    subscribeForm.on('submit', function (e) {
        e.preventDefault()
        const email = $(this).find('input').val()
        subscribeRequest(email).done(function (response) {
            alert('Вы подписались')
        }).fail(function (response) {
            alert(response.responseJSON.email)
        })
    })

    // сообщение админу
    let contactsForm = $('#contact-form')

    function leaveMessageRequest(formData) {
        return $.ajax({
            url: '/api/leave-message/',
            type: 'POST',
            data: formData
        })
    }

    contactsForm.on('submit', function (e) {
        e.preventDefault()
        let formData = contactsForm.find('input, textarea').serialize()

        leaveMessageRequest(formData).done(function (response) {
            contactsForm.find('input, textarea').val('')
            alert('Сообщение отправлено')
        }).fail(function (response) {
            alert('Ошибка при отправке сообщения')
        })
    })

    // добавление товара в избранное
    function toggleToFavoriteRequest(product_id) {
        return $.ajax({
            url: favoriteEndpoint,
            type: 'POST',
            data: {
                product: product_id
            }
        })
    }

    let favorites = $('.add-to-favorite')
    favorites.on('click', function (e) {
        e.preventDefault()
        const productId = $(this).data('product-id')
        toggleToFavoriteRequest(productId).done(function (response) {
            $('#favorites').text(response.count)
        })
    })

})(jQuery);