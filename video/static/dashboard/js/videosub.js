
var videoAreaStatus = false;
var videoEditArea = $('#video-edit-star-area');

$('#open-add-star-btn').click(function(){
    if (!videoAreaStatus){
        videoEditArea.show();
        videoAreaStatus = true;
    }else{
        videoEditArea.hide();
        videoAreaStatus = false;
    }
});

var videoAreaStatus2 = false;
var videoEditArea2 = $('#video-edit-video-area');

$('#open-add-video-btn').click(function(){
    if (!videoAreaStatus){
        videoEditArea2.show();
        videoAreaStatus2 = true;
    }else{
        videoEditArea2.hide();
        videoAreaStatus2 = false;
    }
});