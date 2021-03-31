function validateJform(){

    
     let passok=isPassok();
    
    if(passok!=true){
        let node=document.getElementById("invalidPassword");
        node.style.color="red";
        node.innerHTML="Password isn't valid";
        return false;
    }
    let pass1=$("#jPassword").val();
    let pass2=$("#jPassword2").val();
    
    if(pass1 !=pass2){
        let node=document.getElementById("PasswordNotSame");
        node.innerHTML="Password Didn't match";
        return false;
    }
    console.log("Reached at end");
    return true;


}
function isPassok(){
    let password=$("#jPassword").val();
    let alpha=0,num=0;
    let i;
    for(i=0;i<password.length;i++){
        if((password[i]>='a' && password[i]<='z')||(password[i]>='A' && password[i]<='Z')){
            alpha=1;
        }
        if(password[i]>=0 && password[i]<=9){
            num=1;
        }
    }
if(alpha==1 && num==1 && password.length>=8){
    return true;
}
return false;

    }

