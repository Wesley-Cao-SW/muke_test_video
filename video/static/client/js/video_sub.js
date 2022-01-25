var ajax_comment_show = $('#ajax-comment-show');
var comment_content = $('#comment-content');

$('#comment-submit').click(function(){
    var content = $('#comment-content').val();
    var csrfToken = $('#django-csrf-token').val();
    var videoId = $(this).attr('data-video-id');
    var userId = $(this).attr('data-user-id');
    var url = $(this).attr('data-url');

    if(!content){
        alert('评论不能为空');
        return;
    };

    $.ajax({
        url: url,
        type: 'post',
        data: {
            content: content,
            videoId: videoId,
            userId: userId,
            csrfmiddlewaretoken: csrfToken
        },
        success:function(data){
            if (data.code ==0){
                ajax_comment_show.html('');
                var comment = data.data.comment;
                var username = comment.username;
                var content = comment.content;

                var str = content + ' ' + username;
                ajax_comment_show.html(str);
                comment_content.val('');
            }
        },
        fail:function(e){
            console.log('error:%s', e);
        }
    });
});