// Calculate tank Capacity

document.getElementById("tankheight").addEventListener("input", myFunction);

function myFunction() {
  console.log("Start of Tank Capacity Calculation")
  let tanklength =  document.getElementById("tankheight").value;
  console.log(tanklength)
  let tankwidth =  document.getElementById("tankwidth").value;
  console.log(tankwidth)
  let tankheight =  document.getElementById("tankheight").value;
  console.log(tankheight)
  console.log(tanklength * tankwidth * tankheight)
  document.getElementById("tankcapacity").value = tanklength * tankwidth * tankheight
  document.getElementById("regulatoryfillcapacityallowed").value = (tanklength * tankwidth * (tankheight -0.02))
}
