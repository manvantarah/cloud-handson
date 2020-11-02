function loginpage() { 
  var email =  
      document.forms["loginform"]["email"]; 
  var password =  
      document.forms["loginform"]["password"]; 
  if (email.value == "") { 
      window.alert("Please enter your Email-ID."); 
      email.focus(); 
      return false; 
  } 
  if (password.value == "") { 
      window.alert("Please enter password."); 
      password.focus(); 
      return false; 
  } 
  return true; 
} 