function loginvalidate() {
    var email = document.getElementById("email").value;
    var password = document.getElementById("password").value;
    if (email == null || email == "") {
        alert("Please enter the Email-ID");
        return false;
    }
    if (password == null || password == "") {
        alert("Please enter the password");
        return false;
    }
    alert('Login successful');
    
} 
function loginvalidate1() {
    var email1 = document.getElementById("email1").value;
    var password = document.getElementById("password").value;
    if (email1 == null || email1 == "") {
        alert("Please enter the Email-Id");
        return false;
    }
    alert('Password Sent, Please chek Your Email-ID');
    
} 