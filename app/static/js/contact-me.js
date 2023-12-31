$(document).ready(function() {
    $("#contact-form [type='submit']").click(function(e) {
        e.preventDefault();
        var user_name = $('input[name=name]').val();
        var user_email = $('input[name=email]').val();
        var user_subject = $('input[name=subject]').val();
        var user_message = $('textarea[name=message]').val();
        post_data = {
            'userName': user_name,
            'userEmail': user_email,
            'userSubject': user_subject,
            'userMessage': user_message
        };
        $.post('/senf-email/', post_data, function(response) {
            if (response.type == 'error') {
                output = '<div class="error-message"><p>' + response.text + '</p></div>';
            } else {
                output = '<div class="success-message"><p>' + response.text + '</p></div>';
                $('#contact-form input').val('');
                $('#contact-form textarea').val('');
            }
            $("#answer").hide().html(output).fadeIn();
        }, 'json');
    });
    $("#contact-form input, #contact-form textarea").keyup(function() {
        $("#answer").fadeOut();
    });
});