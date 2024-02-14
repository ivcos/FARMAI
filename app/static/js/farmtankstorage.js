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
