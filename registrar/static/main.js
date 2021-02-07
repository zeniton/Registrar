//Show video
let video = document.getElementById("video");
navigator.mediaDevices
.getUserMedia({ video: true })
.then((stream) => {
    video.srcObject = stream;
    video.play();
})
.catch((err) => {
    console.log(err.name + ": " + err.message);
});

//Take photo (from video stream)
let canvas = document.getElementById("canvas");
let context = canvas.getContext('2d');
let snap = document.getElementById("snap");
snap.addEventListener('click', () => {
    context.drawImage(video, 0, 0, 640, 480);
})