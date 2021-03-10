const api = 'http://localhost:5000';
const HTTPstatus = {
    OK: 200,
    CREATED: 201,
    BADREQUEST: 400,
    NOTFOUND: 404
}
const MessageType = {
    START: 1,
    CONFIRM: 2,
    WELCOME: 3
}

var photoGuid = '';

function test() { 
    fetch(api)
    .then(response => console.log(response.json()))
    .catch(error => console.log(error));
}        

function getMessage(msgType, member) {
    if (member == null || member.language == 'A') {
        switch (msgType) {
            case MessageType.START:
                return 'Kyk asb vir die kamera';
            case MessageType.CONFIRM:
                return 'Bevestig asb...';
            case msgEnum.WELCOME:
                return `Welkom ${member.name}! Jy is geregistreer vir die vergadering.`
        }
    } else {
        switch (msgEnum) {
            case MessageType.START:
                return 'Please look at the camera';
            case MessageType.CONFIRM:
                return `Please confirm that you are `;
            case msgEnum.WELCOME:
                return `Welcome ${member.name}! You are registered for the meeting.`
        }
    }
}

function start() {
    document.getElementById('message').innerText = getMessage(MessageType.START, null);
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
            case HTTPstatus.OK: //Someone was recognised...
                photoGuid = json.photoGuid;
                showMember(json.member);
                break;
            case HTTPstatus.NOTFOUND: //Unknown member in photo
                photoGuid = json.photoGuid;
                getMemberId();
                break;
            case HTTPstatus.BADREQUEST: //Bad photo
                //TODO
                break;
                default:
                    console.log(response);
        }
    })
    .catch(error => console.log(error));
}

//TODO: the next 2 functions must be combined
function showMember(json) {
    member = json.member;
    document.getElementById('message').innerText = getMessage(MessageType.CONFIRM, member);
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
            case HTTPstatus.CREATED: //Attendence recorded
                welcomeMember(json.member);
                break;
            case HTTPstatus.NOTFOUND: //Membership number unknown
                break;
        }
    })
    .catch(error => console.log(error));
    
    start(); //Do it all again...
}

function welcomeMember(member) {

}
