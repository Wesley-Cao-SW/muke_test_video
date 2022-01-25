$('#regist-submit').click(function(){
    var username = $('#username').val();
    var password = $('#password').val();
    var url = $(this).attr('data-url');
    // 通过对应ID， 获取csrf值
    var csrfToken = $('#django-csrf-token').val();

    if (!username || !password){
        alert('缺少必要字段');
        return;
    }


    $.ajax({
        url: url,
        type: 'post',
        data: {
            username: username,
            password: password,
            csrfmiddlewaretoken: csrfToken
        },
        success:function(data){
            alert(data.msg)
        },
        fail:function(e){
            console.log('error:%s', e)
        }
    });
});


$('#login-submit').click(function(){
    var username = $('#username').val();
    var password = $('#password').val();
    var url = $(this).attr('data-url');
    var csrfToken = $('#django-csrf-token').val();

    if (!username || !password){
        alert('缺少必要字段');
        return;
    }


    $.ajax({
        url: url,
        type: 'post',
        data: {
            username: username,
            password: password,
            csrfmiddlewaretoken: csrfToken
        },
        // 数据传输成功执行动作
        success:function(data){
            // 对返回的字符串进行处理、判断
            if (data.code){
                alert(data.msg)
            }else{
                // 成功进行页面跳转
                window.location.href='/client/index/exvideo';
            }
        },
        fail:function(e){
            console.log('error:%s', e)
        }
    });
});