var api = 'http://localhost:5000';
var photoGuid = '';

function test() { 
    fetch(api)
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(data => console.log(data));
}

class Member {
    constructor(id, name, surname) {
        this.id = id;
        this.name = name;
        this.surname = surname;
    }
}

function start() {
    document.getElementById('message').innerText = 'Please look at the camera';
    document.getElementById('userInput').hidden = true;
    document.getElementById('button').hidden = false;
    
    let video = document.getElementById('video');
    navigator.mediaDevices.getUserMedia({video: true})
    .then((stream) => {
        video.srcObject = stream;
        video.play();
    });    
}    

function snapPhoto() {
    let canvas = document.getElementById('canvas');
    canvas.getContext('2d').drawImage(video, 0, 0, 640, 480);
    
    let payload = {
        method: 'post',
        headers: 'application/json',
        body: JSON.stringify(photo=canvas.toDataURL().split(',')[1].replace(' ', '+'))
    };
    fetch(`${api}/v1/identify`, payload)
    .then(response => {
        let json = reponse.json(); 
        switch (response.status) {
            case 200: //Member recognised (but may be wrong...)
                photoGuid = json.photoGuid;
                showMember(json.member);
                break;
            case 404: //Member not recognised
                photoGuid = json.photoGuid;
                getMemberId();
                break;
            case 400: //Bad photo
                //TODO
                break;
                default:
                    console.log(response);
        }
    })
    .catch(error => console.log(error));
}

function showMember(json) {
    member = json.member;
    let message = `Please confirm that you are ${member.name} ${member.surname} (${member.id})`;
    document.getElementById('message').innerText = message;
    let button = document.getElementById('button');
    button.innerText = 'Confirm';
}

function getMemberId() {
    document.getElementById('message').innerText = 'Please enter your membership number';
    let userInput = document.getElementById('userInput');
    userInput.innerText = '';
    userInput.hidden = false;
    
    let button = document.getElementById('button')
    button.innerText = 'Register me!';
    button.onclick = () => {
        button.removeAttribute('onclick');
        registerMember(userInput.innerText);
    }
}

function registerMember(memberId) {
    let payload = {
        method: 'post',
        headers: 'application/json',
        body: JSON.stringify({ photoGuid=photoGuid, memberId=memberId })
        };
    fetch(`${api}/v1/register`, payload)
    .then()
    .catch(error => console.log(error));
    
    start(); //Do it all again...
}
