function init() {
    console.log('init...');
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
}

function boo() {
    alert('Boo!');
}

//Take photo (from video stream)
function snapPhoto() {
    boo();
    // let canvas = document.getElementById("canvas");
    // let photo = document.getElementById("photo");

    // canvas.getContext('2d').drawImage(video, 0, 0, 640, 480);
    // photo.innerText = canvas.toDataURL();
}
