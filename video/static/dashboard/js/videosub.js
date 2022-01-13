var inputNumber = $('#number');
var inputUrl = $('#url');
var videosubInputId = $('#videosub-input-id');

$('.update-video-btn').click(function(){
    var videosubId = $(this).attr('data-id');
    var videosubUrl = $(this).attr('data-url');
    var videosubNumber = parseInt($(this).attr('data-number'));


    inputNumber.val(videosubNumber);
    inputUrl.val(videosubUrl);
    videosubInputId.val(videosubId);

});

var inputName = $('#name');
var inputIdentity = $('#identity');
var videostarId = $('#star-id');

$('.update-star-btn').click(function(){
    var videostarInputId = $(this).attr('data-id');
    var videostarIdentity = $(this).attr('data-identity');
    var videostarName = $(this).attr('data-name');


    inputName.val(videostarName);
    inputIdentity.val(videostarIdentity);
    videostarId.val(videostarInputId);

});