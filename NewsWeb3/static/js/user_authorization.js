//用户订阅
function SubscriptionEmail() {
    var email = document.getElementById("email").value;
    $.post(url_link, {
            email: email,
        },
        function (result) {

        });
}

// 用户找回密码提示
function ForgotMail() {
    alert("您的服务提交成功，若没有收到邮件请检查邮箱是否填写正确！！");
}


function add_fav_org(current_elem, article_slug,) {
    var url_ = addfav_link + "?article_slug= " + article_slug
    $.ajax({
        cache: false,
        type: "GET",
        url: url_,
        async: true,
        beforeSend: function (xhr, settings) {
            xhr.setRequestHeader("X-CSRFToken", "{{ csrf_token }}");
        },
        success: function (data) {
            if (data.status === 'success') {
                current_elem.text(data.msg);
                if (data.msg === '取消收藏') {
                    document.getElementById('add_fav_org_button').style.background = '#FFA042';
                } else if (data.msg === '收藏成功') {
                    document.getElementById('add_fav_org_button').style.background = '#02DF82';
                }
            }
        },
    });
}

$('#add_fav_org_button').on('click', function () {
    add_fav_org($(this), article_slug,);
});

