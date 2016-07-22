/**
 * Created by dauglas on 16/7/14.
 */

$(document).ready(function () {
    // When we're using HTTPS, use WSS too.
    var scheme = window.location.protocol == 'https:' ? 'wss' : 'ws';
    var socket = new ReconnectingWebSocket(scheme + '://' + window.location.host + '/conc/');

    socket.onmessage = function (e) {
        var current = $("h2[cursor=current]");
        var newItem = $("<h2></h2>").text(e.data);
        newItem.attr({"cursor": "current"})
        current.before(newItem);
        current.removeAttr("cursor")
    }

    socket.onopen = function () {
    }
});