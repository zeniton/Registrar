var api = 'http://localhost:5000';

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
    let msg = document.getElementById('message');
    let userInput = document.getElementById('userInput');
    let button = document.getElementById('button');
    let video = document.getElementById('video');
    
    msg.innerText = 'Please look at the camera';
    userInput.hidden = true;
    button.hidden = false;
    
    navigator.mediaDevices.getUserMedia({video: true})
    .then((stream) => {
        video.srcObject = stream;
        video.play();
    });    
}    

function snapPhoto() {
    let canvas = document.getElementById('canvas');
    canvas.getContext('2d').drawImage(video, 0, 0, 640, 480);
    
    fetch(`${api}/v1/identify`, {
        method: 'post',
        body: JSON.stringify({ photo: canvas.toDataURL().split(',')[1].replace(' ', '+') }),
    })
    .then(response => response.json())
    .then(json => showMember(json))
    .catch(data => console.log(data));
}

function showMember(json) {
    let msg = document.getElementById('message');
    let button = document.getElementById('button');
    member = json.member;
    msg.innerText = `Please confirm that you are ${member.name} ${member.surname} (${member.id})`;
    button.innerText = 'Confirm';
}
