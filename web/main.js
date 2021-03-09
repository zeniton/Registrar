var api = 'http://localhost:5000';
var photoGuid = '';

class Member {
    constructor(id, name, surname, language, phone, email) {
        this.id = id;
        this.name = name;
        this.surname = surname;
        this.language = language;
        this.phone = phone;
        this.email = email;
    }
}

function test() { 
    fetch(api)
    .then(response => console.log(response.json()))
    .catch(data => console.log(data));
}    

const MsgEnum = {
    START: 1,
    CONFIRM: 2,
    WELCOME: 3
}
Object.freeze(MsgEnum);

function getMessage(msgEnum, member) {
    if (member == null || member.language == 'A') {
        switch (msgEnum) {
            case MsgEnum.START:
                return 'Kyk asb vir die kamera';
            case MsgEnum.CONFIRM:
                return 'Bevestig asb...';
            case msgEnum.WELCOME:
                return `Welkom ${member.name}! Jy is geregistreer vir die vergadering.`
        }
    } else {
        switch (msgEnum) {
            case MsgEnum.START:
                return 'Please look at the camera';
            case MsgEnum.CONFIRM:
                return `Please confirm that you are `;
            case msgEnum.WELCOME:
                return `Welcome ${member.name}! You are registered for the meeting.`
        }
    }
}

function start() {
    document.getElementById('message').innerText = getMessage(MsgEnum.START, null);
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
    let photo = canvas.toDataURL().split(',')[1].replace(' ', '+');
    
    fetch(`${api}/v1/identify`, {
        method: 'post',
        headers: 'application/json',
        body: JSON.stringify(photo = photo)
    })
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
    let message = `${getMessage(MsgEnum.CONFIRM)} ${member.name} ${member.surname} (${member.id})`;
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
    fetch(`${api}/v1/register`, {
        method: 'post',
        headers: 'application/json',
        body: JSON.stringify(photoGuid = photoGuid, memberId = memberId)
    })
    .then(response => {
        let json = response.json(); 
        switch (response.status) {
            case 200: //All good
                welcomeMember(json.member);
                break;
            case 404: //Member not on record
                break;
        }
    })
    .catch(error => console.log(error));
    
    start(); //Do it all again...
}

function welcomeMember(member) {

}
