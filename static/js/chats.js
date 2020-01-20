$('#chat-form').on('submit', function(event) {
    event.preventDefault();

    $.ajax({
        url: 'blog/post/',
        type: 'POST',
        data: { msgbox: $('#chat-msg').val() },

        success: function(json) {
            console.log(json);
            $('#chat-msg').val('');
            $('#msg-list').append('<li class="text-right list-group-item">' + json.msg + '</li>');
            var chatlist = document.getElementById('msg-list-div');
            //chatlist.scrollTop = chatlist.scrollHeight;
        }
    });
});

function getMessages() {
    if (!scrolling) {
        $.get('blog/messages/', function(messages) {
            console.log(messages);
            $('#msg-list').html(messages);
            var chatlist = document.getElementById('msg-list-div');
            //chatlist.scrollTop = chatlist.scrollHeight;
        });
    }
    scrolling = false;
}

var scrolling = false;
$(function() {
    /*$('#msg-list-div').on('scroll', function(){
        scrolling = true;
    });*/
    refreshTimer = setInterval(getMessages, 5000); //0.5 seconds
});

$(document).ready(function() {
    $('#send').attr('disabled', 'disabled');
    $('#chat-msg').keyup(function() {
        if ($(this).val() != '') {
            $('#send').removeAttr('disabled');
        } else {
            $('#send').attr('disabled', 'disabled');
        }
    });
});

//using JQuery
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie != '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = jQuery.trim(cookies[i]);

            if (cookie.substring(0, name.length + 1) == (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

var csrftoken = getCookie('csrftoken');

function csrfSafeMethod(method) {
    // these http methodes don't need CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});