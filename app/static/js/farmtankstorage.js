// Calculate tank Capacity

document.getElementById("tankheight").addEventListener("input", myFunction);

function myFunction() {
  console.log("Start of Tank Capacity Calculation")
  let tanklength =  parseFloat(document.getElementById("tanklength").value);
  console.log(tanklength)
  let tankwidth =  parseFloat(document.getElementById("tankwidth").value);
  console.log(tankwidth)
  let tankheight =  parseFloat(document.getElementById("tankheight").value);
  console.log(tankheight)
  console.log(tanklength * tankwidth * tankheight)
  document.getElementById("tankcapacity").value = 1000 * (tanklength) * (tankwidth) * (tankheight) 
  document.getElementById("regulatoryfillcapacityallowed").value = 1000 * (tanklength * tankwidth * (tankheight -0.02))
}

function validateAlphanumeric(input) {
  const alphanumericRegex = /^[a-zA-Z0-9]+$/;
  return alphanumericRegex.test(input);
}


function validatefarmnumber () {
  let farmnumber = document.getElementById("farmnumber").value
  console.log(farmnumber)
  if (!validateAlphanumeric(farmnumber)){
    document.getElementById("farm-number-error-message").innerHTML= "You entered: " + farmnumber + ". Only numbers and letters allowed" 
  }
 else {
  document.getElementById("farm-number-error-message").innerHTML=" "
}
}


function validatetanklength () {
  let tanklength = document.getElementById("tanklength").value
  console.log(tanklength)
  if (Number.parseFloat(tanklength) > 18 && Number.parseFloat(tanklength) < 22) {
      document.getElementById("tank-length-error-message").innerHTML=" "
    }
  else {
  document.getElementById("tank-length-error-message").innerHTML= "You entered: " + tanklength + ". Only numbers allowed between 18 and 22" 
}
}

function validatetankwidth () {
  let tankwidth = document.getElementById("tankwidth").value
  console.log(tankwidth)
  console.log(Number.parseFloat(tankwidth))
  if (Number.parseFloat(tankwidth) > 9 && Number.parseFloat(tankwidth) < 13) {
    console.log("ok")
    document.getElementById("tank-width-error-message").innerHTML=" "
  }
  else {
  console.log("ok1")
  console.log(Number.parseFloat(tankwidth))
  document.getElementById("tank-width-error-message").innerHTML= "You entered: " + tankwidth + ". Only numbers allowed 9 and 12" 
}
}

function validatetankheight () {
let tankheight = document.getElementById("tankheight").value
console.log(tankheight)
if (Number.parseFloat(tankheight) > 2.0 && Number.parseFloat(tankheight) < 2.5) {
  document.getElementById("tank-height-error-message").innerHTML=" "
}
else {
document.getElementById("tank-height-error-message").innerHTML= "You entered: " + tankheight + ". Only numbers allowed between 2.0 and 2.4" 
}
}


//Clear the form input data and remove the mesaage again
// document.getElementById("calving_form").reset();
// message.textContent = "";

function onDOMLoaded()
{
  console.log("test")

}


document.addEventListener("DOMContentLoaded", onDOMLoaded);
