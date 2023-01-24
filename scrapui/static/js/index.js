'use strict';

var but = document.getElementById('but-chat') ;
const botnput = document.querySelector('.input-bot');
const botsub = document.querySelector('.reply');
const botmessage = document.querySelector('.right');
const usermessage = document.querySelector('.left');
let message = [] ; 

window.onload = function(){
    try {
        if( but !== null) {
            setInterval(displaychat,1000) ;
        }
    } catch (err) {
        console.log( err.message )
    }
}

document.addEventListener(
    'keypress',
    event =>{
        if( event.which === 13){
            //alert('press')
            Chatus();
        }
    }
)

function displaychat(){
    but.style.display = 'block' ;
}
function getText(text) {
    const textnode = document.createTextNode(text);
    return textnode ;
}

function getRandomWord(arr)
{
    const r = Math.floor(Math.random() * arr.length) ;
    const data = arr[r];
    return data
}

function Chatus(){
    let usertext = botnput.value.toLowerCase() ;
    let bottext = '' ;
    const usernode = document.createElement("li");
    const botnode = document.createElement("li");
    const link = document.createElement('a')
    let data = {
        reqis : ['signup','register','regis'],
        signin: ['signin','login'],
        gretting: ['hi','hey','hello'],
    } 
    botnode.className = 'message right';
    usernode.className = 'message left';
    if(usertext === ''){
        return 
    }else if( usertext !== '')
    {
        if (data.reqis.includes(usertext)) {
            link.title = 'signup this link' ;
            link.text = 'register'
            link.setAttribute('target','_blank')
            link.setAttribute('href',"http://127.0.0.1:8000/register/")
            link.click() ;
            bottext = link;
        }else if(data.signin.includes(usertext)) {
            link.title = 'signin this link' ;
            link.text = 'signin'
            link.setAttribute('target','_blank')
            link.setAttribute('href',"http://127.0.0.1:8000/signin/")
            link.click() ;
            bottext = link;

        }else if(data.gretting.includes(usertext)) {
            message = ['hi welcome to scrapui?','hello,nice to meet you sir/madam','hi,Thanks for being here']
            bottext = getRandomWord(message);

        }else{
            usertext = botnput.value;
            bottext = 'please contact the admin@gmail.com for more details!';
        }
    }


    // api 
    // let user = {
    //     'bot':'signup'
    //     }
    //     let options = {
    //     method: 'POST',
    //     headers: {
    //         'Content-Type':'application/json'
    //     },

    // }
    // let fetchRes = fetch(
    //     "http://127.0.0.1:8000/bot/",options);
    //     fetchRes.then(res =>
    //     res.json()).then(d => {
    //         console.log(d.message)
    //     })

    usertext = getText(usertext) ;
    bottext = getText(bottext);
    //usermessage.innerHTML = usertext;
    botnode.appendChild(bottext);
    usernode.appendChild(usertext);

    setTimeout(
        function(){
            document.getElementById("chatbot").appendChild(usernode);
            document.getElementById("chatbot").appendChild(botnode);
            var a =  document.getElementsByClassName('body-bot')[0].scrollHeight ;
            document.getElementsByClassName('body-bot')[0].scrollTop = a + 100;
            console.log( a);
        },1000)
    resetinput()
}


function resetinput(){
    if(botnput !== ''){
        botnput.value = '';
    }
}

function showPass(){
    if(password.type === 'password'){
        password.type = 'text'
    }else{
        password.type = 'password'
    }
    console.log( password )
}



function disapearTime(id , mess , value ) {
    setTimeout(
        function() {
            id.innerHTML = mess ;

        }
    , value ) ;

    setTimeout(
        function() {
            id.classList.remove('error') ;

        }
    , value ) ;
    //id.classList.remove('error') ;
}


function ValidateEmail( value ) 
{
 if (/^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/.test(value ))
  {
    return value;
  }
    return (false)
}

function ValidatePhone ( value ) {
    if (/^(0|91)?[6-9][0-9]{9}$/.test( value )) {
        return  value;
    }
    else{
        return false;

    }
}

function contactusww( ) {
    let message = document.getElementById('mess') ;

    let email = contact_email.value;
    let phone = detail.value ;


    if( email === '' || phone === '' ) {
        message.classList.add("error");
        message.innerHTML = 'Input cannot be Empty ' ;
        disapearTime( message , ' ' , 4000 ) ;  
    }

    else { 
        if( (!ValidateEmail( email ) ) || (!ValidatePhone( phone ) ) ){
            message.classList.add("error");
            message.textContent = 'invalid Email and Phone number ' ;
            disapearTime( message , ' ' , 4000 ) ; 
        }else{
            message.classList.add("error");
            message.textContent = 'Thanks' ;
            disapearTime( message , ' ' , 4000 ) ; 

            location.href = `https://wa.me/6009188445?text=This is my Gmail=${email}+ and this is my phone number =${ phone }`

        }
    }

    console.log( ValidateEmail( email ) , ValidatePhone( phone ) ) ;

    //location.href = `https://wa.me/6009188445?text=This is my Gmail=${email}+ and this is my phone number =${detail}`
}