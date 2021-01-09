$("#eUsername").change(function(){
    let username=$(this).val();
    let validusername=document.getElementById('eUsernamevalid');
    $.ajax({
        url:'/validate_username/',
        data:{
            'username':username
        },
        dataType:'json',
        success:function(data){
            if(!data.is_ok){
                validusername.style.color="green";
                validusername.innerHTML="Username available";
            }
            else{
                validusername.style.color="red";
                validusername.innerHTML="username not available";
            }
        }
    });
});