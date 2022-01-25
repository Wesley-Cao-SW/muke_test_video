$('.user-status-submit').click(function(){
    var url = $(this).attr('data-url');
    var userId = $(this).attr('data-user-id');
    var csrfToken = $('#django-csrf-token').val();

    $.ajax({
        url:url,
        type: 'post',
        data: {
            userId: userId,
            csrfmiddlewaretoken: csrfToken
        },
        success:function(data){
            if (data.code ==0){
               alert(data.msg);
               window.location.href = window.location.href;
            }else{
                alert(data.msg)
            }
        },
        fail:function(e){
            console.log('error:%s', e);
        }
    })
});