!(function (_window, _document) {
    smartAppBanner = {},
        smartAppBanner.loader = {},
        function (f, w) {
            "use strict";
            function runOnce() {
                if (!executed) {
                    executed = !0;
                    for (var i = 0; i < functions.length; i++) {
                        functions[i].fn.call(_window, functions[i].ctx);
                    }
                    functions = []
                }
            }
            function runOnceAfterComplete() {
                _document.readyState === "complete" && runOnce()
            }
            f = f || "documentReady";
            w = w || _window;
            var functions = [],
                executed = !1,
                setListener = !1;
            w['ccEventFlag'] = false;
            w['ccEvent'] = function () {
                w['ccEventFlag'] = true;
            };
            w[f] = function (f, w) {
                return executed ?
                    void setTimeout(function () {
                        console.log('Already executed!');
                    }, 1) :
                    (functions.push({
                        fn: f,
                        ctx: w
                    }), void(_document.readyState === "complete" || !_document.attachEvent && _document.readyState === "interactive" ?
                        setTimeout(runOnce, 1) :
                        setListener || (_document.addEventListener ?
                            (_document.addEventListener("DOMContentLoaded", runOnce, !1), _window.addEventListener("load", runOnce, !1)) :
                            (_document.attachEvent("onreadystatechange", runOnceAfterComplete), _window.attachEvent("onload", runOnce)), setListener = !0)))
            }
        }("documentReady", _window),
        function (loader) {
            documentReady(function () {
                var obj = document.getElementById('smart_app_widget_script');
                loader.settings.domain = obj.getAttribute('data-domain');
                loader.settings.links = JSON.parse(atob(obj.getAttribute('data-links')));
                loader.functions.prepareStyles(obj);
                loader.functions.loadScript(loader.settings.domain + "/smartapp-widget/js/libs/jquery.min.js", function () {
                    loader.functions.renderWidget();
                }, function () {

                })
            }),
                loader.settings = {
                    domain: '',
                    text: '',
                    links: {},
                    styles: {
                        close: { position: 'absolute', right: '0', 'z-index': '99999', width: '25px', height: '25px' },
                        widget: {position: 'fixed', cursor: 'pointer', left: '0', right: '0', width: '100%', 'box-sizing': 'border-box',  'z-index': '999', padding: '10px', background: '', 'border-color': ''},
                        ico: { display: 'inline-block', 'max-height': '50px', 'width': 'calc(35% - 10px)', float: 'left', 'margin-right': '10px'},
                        text: { position: 'relative', display: 'inline-block', 'float': 'left', 'max-width': '65%', 'font-family': 'Helvetica, OpenSans, PTSans, Roboto, Arial',  'font-weight': '400', 'line-height': '18px', 'font-size': '14px', 'color': '', 'text-align': 'center' }
                    }
                },
                loader.functions = {
                    prepareStyles: function (obj) {
                        if (obj.getAttribute('data-position') === 'bottom'){
                            loader.settings.styles.widget['border-top'] = '5px solid ' + obj.getAttribute('data-border');
                            loader.settings.styles.widget['border-top-left-radius'] = '5px';
                            loader.settings.styles.widget['border-top-right-radius'] = '5px';
                            loader.settings.styles.widget['bottom'] = '0';
                            loader.settings.styles.close['top'] = '-50px';
                        } else {
                            loader.settings.styles.widget['border-bottom'] = '5px solid ' + obj.getAttribute('data-border');
                            loader.settings.styles.widget['border-bottom-left-radius'] = '5px';
                            loader.settings.styles.widget['border-bottom-right-radius'] = '5px';
                            loader.settings.styles.widget['top'] = '0';
                            loader.settings.styles.close['bottom'] = '-50px';
                        }
                        loader.settings.styles.close['background'] = 'url(' + loader.settings.domain + '/smartapp-widget/img/close.png) no-repeat center';
                        loader.settings.styles.close['background-size'] = 'cover';
                        loader.settings.styles.widget.background = obj.getAttribute('data-background');
                        loader.settings.styles.text.color = obj.getAttribute('data-color');
                        loader.settings.text = obj.getAttribute('data-text');
                    },
                    getCookie: function (name) {
                        var matches = document.cookie.match(new RegExp(
                            "(?:^|; )" + name.replace(/([\.$?*|{}\(\)\[\]\\\/\+^])/g, '\\$1') + "=([^;]*)"
                        ));
                        return matches ? decodeURIComponent(matches[1]) : undefined;
                    },
                    setCookie: function (name, value, options) {
                        options = options || {};
                        var expires = options.expires;
                        if (typeof expires === "number" && expires) {
                            var d = new Date();
                            d.setTime(d.getTime() + expires * 1000);
                            expires = options.expires = d;
                        }
                        if (expires && expires.toUTCString) {
                            options.expires = expires.toUTCString();
                        }
                        value = encodeURIComponent(value);
                        var updatedCookie = name + "=" + value;
                        for (var propName in options) {
                            if (options.hasOwnProperty(propName)) {
                                updatedCookie += "; " + propName;
                                var propValue = options[propName];
                                if (propValue !== true) {
                                    updatedCookie += "=" + propValue;
                                }
                            }
                        }
                        document.cookie = updatedCookie;
                    },
                    isMobile: function () {
                        var isMobile = false;
                        if (/(android|bb\d+|meego).+mobile|avantgo|bada\/|blackberry|blazer|compal|elaine|fennec|hiptop|iemobile|ip(hone|od)|ipad|iris|kindle|Android|Silk|lge |maemo|midp|mmp|netfront|opera m(ob|in)i|palm( os)?|phone|p(ixi|re)\/|plucker|pocket|psp|series(4|6)0|symbian|treo|up\.(browser|link)|vodafone|wap|windows (ce|phone)|xda|xiino/i.test(navigator.userAgent)
                            || /1207|6310|6590|3gso|4thp|50[1-6]i|770s|802s|a wa|abac|ac(er|oo|s\-)|ai(ko|rn)|al(av|ca|co)|amoi|an(ex|ny|yw)|aptu|ar(ch|go)|as(te|us)|attw|au(di|\-m|r |s )|avan|be(ck|ll|nq)|bi(lb|rd)|bl(ac|az)|br(e|v)w|bumb|bw\-(n|u)|c55\/|capi|ccwa|cdm\-|cell|chtm|cldc|cmd\-|co(mp|nd)|craw|da(it|ll|ng)|dbte|dc\-s|devi|dica|dmob|do(c|p)o|ds(12|\-d)|el(49|ai)|em(l2|ul)|er(ic|k0)|esl8|ez([4-7]0|os|wa|ze)|fetc|fly(\-|_)|g1 u|g560|gene|gf\-5|g\-mo|go(\.w|od)|gr(ad|un)|haie|hcit|hd\-(m|p|t)|hei\-|hi(pt|ta)|hp( i|ip)|hs\-c|ht(c(\-| |_|a|g|p|s|t)|tp)|hu(aw|tc)|i\-(20|go|ma)|i230|iac( |\-|\/)|ibro|idea|ig01|ikom|im1k|inno|ipaq|iris|ja(t|v)a|jbro|jemu|jigs|kddi|keji|kgt( |\/)|klon|kpt |kwc\-|kyo(c|k)|le(no|xi)|lg( g|\/(k|l|u)|50|54|\-[a-w])|libw|lynx|m1\-w|m3ga|m50\/|ma(te|ui|xo)|mc(01|21|ca)|m\-cr|me(rc|ri)|mi(o8|oa|ts)|mmef|mo(01|02|bi|de|do|t(\-| |o|v)|zz)|mt(50|p1|v )|mwbp|mywa|n10[0-2]|n20[2-3]|n30(0|2)|n50(0|2|5)|n7(0(0|1)|10)|ne((c|m)\-|on|tf|wf|wg|wt)|nok(6|i)|nzph|o2im|op(ti|wv)|oran|owg1|p800|pan(a|d|t)|pdxg|pg(13|\-([1-8]|c))|phil|pire|pl(ay|uc)|pn\-2|po(ck|rt|se)|prox|psio|pt\-g|qa\-a|qc(07|12|21|32|60|\-[2-7]|i\-)|qtek|r380|r600|raks|rim9|ro(ve|zo)|s55\/|sa(ge|ma|mm|ms|ny|va)|sc(01|h\-|oo|p\-)|sdk\/|se(c(\-|0|1)|47|mc|nd|ri)|sgh\-|shar|sie(\-|m)|sk\-0|sl(45|id)|sm(al|ar|b3|it|t5)|so(ft|ny)|sp(01|h\-|v\-|v )|sy(01|mb)|t2(18|50)|t6(00|10|18)|ta(gt|lk)|tcl\-|tdg\-|tel(i|m)|tim\-|t\-mo|to(pl|sh)|ts(70|m\-|m3|m5)|tx\-9|up(\.b|g1|si)|utst|v400|v750|veri|vi(rg|te)|vk(40|5[0-3]|\-v)|vm40|voda|vulc|vx(52|53|60|61|70|80|81|83|85|98)|w3c(\-| )|webc|whit|wi(g |nc|nw)|wmlb|wonu|x700|yas\-|your|zeto|zte\-/i.test(navigator.userAgent.substr(0, 4))) isMobile = true;
                        return isMobile;
                    },
                    isIos: function () {
                        return /iPad|iPhone|iPod/.test(navigator.userAgent) && !window.MSStream;
                    },
                    getIcoUrl: function () {
                        var _base = loader.settings.domain;
                        var _ico = loader.functions.isIos() ? 'appstore.png' : 'google.png';
                        return _base + '//smartapp-widget/img/' + _ico;
                    },
                    renderWidget: function () {
                        if (!loader.functions.isMobile() || loader.functions.getCookie('banner-hide')){
                            return;
                        }
                        var jQ = smartAppBanner.jQuery;
                        var body = jQ('body');
                        var widget = jQ('<div/>', {class: 'smart-app-wrapper'});
                        var close = jQ('<div/>', {class: 'smart-app-close'});
                        var ico = jQ('<img/>', {class: 'smart-app-ico', src: loader.functions.getIcoUrl()});
                        var text = jQ('<div/>', {class: 'smart-app-text', html: loader.settings.text});

                        ico.css(loader.settings.styles.ico);
                        text.css(loader.settings.styles.text);
                        widget.css(loader.settings.styles.widget);
                        close.css(loader.settings.styles.close);

                        close.on('click', function () {
                            loader.functions.setCookie('banner-hide', 'yes', { expires: 86400 * 3 }); //cookie for three days
                            widget.detach();
                        });

                        widget.on('click', function (e) {
                            loader.functions.setCookie('banner-hide', 'yes', { expires: 86400 * 3 }); //cookie for three days
                            widget.detach();
                            if(jQ(e.target).hasClass('smart-app-close')){
                                return;
                            }
                            window.open(loader.functions.isIos() ? loader.settings.links['appStoreUrl'] : loader.settings.links['googlePlayUrl'], '_blank');
                        });

                        text.append(close);
                        widget.append(ico);
                        widget.append(text);
                        widget.append('<div/>', {style: 'clear:both'});
                        body.append(widget);
                    },
                    loadScript: function (src, onLoad, onError) {
                        var script = document.createElement("script");
                        script.type = "text/javascript";
                        script.src = src;
                        script.async = !0;
                        script.charset = "UTF-8";
                        script.onload = onLoad;
                        script.onerror = onError;
                        document.body.appendChild(script)
                    }
                }
        }(smartAppBanner.loader)
})(window, document);