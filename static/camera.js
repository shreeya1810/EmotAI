import Webcam from './webcam-easy/src/webcam-easy.js';

let cam = $(".cam")[0];
const canvas = $('canvas')[0];

const webcam = new Webcam(cam, 'user', canvas);

webcam.start()
   .then(result =>{
      console.log("webcam started");
   })
   .catch(err => {
       console.log(err);
   });

canvas.addEventListener("click", click);

function click(){
   const picture = webcam.snap();
   console.log(picture)
   $.ajax({ 
            url: '/getData', 
            type: 'POST', 
            contentType: 'application/json', 
            data: JSON.stringify({ 'value': picture }), 
            success: function(response) { 
               console.log("success!")
            }, 
            error: function(error) { 
               console.log("error", error); 
            } 
         });
}

$("form")[0].addEventListener("onsubmit", console.log("submitted"));