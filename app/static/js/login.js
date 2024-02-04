// window.onload(function()
// {
//   console.log(document.getElementById("username").value);
//   console.log(document.getElementById("password").value);
//   document.getElementById("username").value="";
//   document.getElementById("password").value="";
// });


function onDOMLoaded()
{
  console.log("test")
  let username_id = document.getElementById("username").id;
  console.log(username_id)
  let username_value = document.getElementById("username").value;
  console.log("username value" + username_value)
  // console.log(document.getElementById("password").value);
  console.log("test end")
}

// Attach the onDOMLoaded function to the DOMContentLoaded event
document.addEventListener("DOMContentLoaded", onDOMLoaded);


// window.onload = function() {
//   var refButton = document.getElementById( 'userna' );
//   refButton.onclick = function() {
//      alert( 'I am clicked!' );
//   }
//   }