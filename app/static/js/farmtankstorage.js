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


function validatedateanimalshoused() {
  let dateanimalshoused= document.getElementById("dateanimalshoused").value
  console.log("ok")
  console.log(dateanimalshoused)
  // // console.log(typeof dateanimalshoused)
  // //Check dates between the 2023-10-15 and 2023-11-31"
  // // const dateanimalshouseddateformat = new Date(dateanimalshoused)
  // // console.log(typeof dateanimalshouseddateformat)
  // let dateanimalshousedformatted = new Date(dateanimalshoused)
  // // dateanimalshousedformatted.split("-").reverse().join("/");
  // console.log(dateanimalshousedformatted)
  // const startdate = new Date("2023-10-15")
  // const enddate = new Date("2023-11-31")
  //   // const startdate = new Date("15/10/2023")
  //   // const enddate = new Date("31/11/2023")
  // if (dateanimalshousedformatted > startdate && dateanimalshousedformatted < enddate ){
  //   console.log('✅ date is between the 2 dates');
  // } else {
  //   console.log('⛔️ date is not in the range');
  //   document.getElementById("date-error-message").innerHTML= "You entered: " + dateanimalshousedformatted + ". Only dates between 15/10/2023 and 30/11/2023 allowed"
  // }
}

function validateforminputs() {
  let dateanimalshoused= document.getElementById("dateanimalshoused").value
  console.log("ok for validateforminput")
  console.log(dateanimalshoused)

}


//Clear the form input data and remove the mesaage again
// document.getElementById("calving_form").reset();
// message.textContent = "";

function onDOMLoaded()
{
  console.log("test")

}


// Function to remove flash messages after 5 seconds
window.onload = function() {
  setTimeout(function() {
      let flashMessages = document.querySelectorAll('.alert');
      console.log(flashMessages)
      flashMessages.forEach(function(message) {
          message.style.display = 'none';
      });
  }, 2000);
};



document.addEventListener("DOMContentLoaded", onDOMLoaded);
