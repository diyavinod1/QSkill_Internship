const textarea =
document.getElementById("message");

const charCount =
document.getElementById("charCount");

textarea.addEventListener("input",()=>{

charCount.innerText =
`${textarea.value.length} Characters`;

});

function analyzeMessage(){

const message =
textarea.value;

if(message.trim()===""){
return;
}

document.getElementById("loading")
.style.display="block";

fetch("/predict",{

method:"POST",

headers:{
"Content-Type":
"application/x-www-form-urlencoded"
},

body:
"message="+encodeURIComponent(message)

})

.then(res=>res.json())

.then(data=>{

document.getElementById("loading")
.style.display="none";

document.getElementById("resultCard")
.classList.remove("hidden");

let predictionDiv =
document.getElementById("prediction");

if(data.prediction==="Spam"){

predictionDiv.innerHTML =
"🚨 Spam Message";

}
else{

predictionDiv.innerHTML =
"✅ Ham Message";

}

document.getElementById("confidenceText")
.innerHTML =
`${data.confidence}% Confidence`;

document.getElementById("progressBar")
.style.width =
`${data.confidence}%`;

});

}