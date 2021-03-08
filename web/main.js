var domain = 'http://localhost:5000';

function start() {
    let msg = document.getElementById('message');
    let userInput = document.getElementById('userInput');
    let button = document.getElementById('button');
    let video = document.getElementById('video');
    let canvas = document.getElementById('canvas');
    
    msg.innerText = 'Please look at the camera';
    userInput.hidden = true;
    button.hidden = false;
    
    navigator.mediaDevices.getUserMedia({video: true})
    .then((stream) => {
        video.srcObject = stream;
        video.play();
    });
}

function test() { 
    fetch(domain)
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(data => console.log(data));
}

function snapPhoto() {
    let canvas = document.getElementById('canvas');
    canvas.getContext('2d').drawImage(video, 0, 0, 640, 480);
    
    console.log('Calling API...');
    fetch(domain + '/v1/identify'
    , {
        method: 'post',
        body: JSON.stringify({ photo: canvas.toDataURL().split(',')[1].replace(' ', '+') }),
        headers: {"Content-type": "application/json; charset=UTF-8"}
    }
    )
    .then(response => response.json())
    .then(json => console.log(json))
    .catch(data => console.log(data));
}

function status(response) {
    if (response.status >= 200 && response.status < 300) {
        return Promise.resolve(response)
    } else {
        return Promise.reject(new Error(response.statusText))
    }
}

function json(response) {
    return response.json()
}