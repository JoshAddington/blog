$(".signin-button").click(function(){
        $(".signin-button").hide();
        $(".signin-options").show();
});


//Google Login
(function() {
    var po = document.createElement('script'); po.type = 'text/javascript'; po.async = true;
    po.src = 'https://apis.google.com/js/client:plusone.js';
    var s = document.getElementsByTagName('script')[0]; s.parentNode.insertBefore(po, s);
})();

var signInCallback = function (result) {
    if (result['error']) {
        console.log('An error happened:', result['error']);
    } else {
        $('#code').attr('value', result['code']);
        $('#at').attr('value', result['access_token']);
        $('#google-plus').submit();
    }
};
