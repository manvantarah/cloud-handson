function validateloginform() {
    var x = document.forms["loginform"]["email"].value;
    if (x == "") {
      alert("Email Address must not be empty");
      return false;
    }
    var y = document.forms["loginform"]["password"].value;
    if (y == "") {
      alert("Please Enter Password");
      return false;
    }
  }
  