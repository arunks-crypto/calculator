document.getElementById("signInBtn").addEventListener("click", function() {
    alert("Sign In button clicked!");
});

document.getElementById("signUpBtn").addEventListener("click", function(event) {
    event.preventDefault();
    alert("Sign Up button clicked!");
});
