// Get the sign in modal
var signinModal = document.getElementById('signinModal');

// Get the link that opens the sign in modal
var signin = document.getElementById('signin');

// Get the <span> element that closes the sign in modal
var closesignin = document.getElementsByClassName('close')[0];

// When the user clicks the button, open the sign in modal
function showSignInModal() {
	signinModal.style.display = 'block';
}

// When the user clicks on <span> (x), close the sign in modal
closesignin.onclick = function() {
	signinModal.style.display = 'none';
};

// When the user clicks anywhere outside of the sign in modal, close it
window.onclick = function(event) {
	if (event.target == signinModal) {
		signinModal.style.display = 'none';
	}
};

// Get the sign up modal
var signupModal = document.getElementById('signupModal');

// Get the link that opens the sign up modal
var signup = document.getElementById('signup');

// Get the <span> element that closes the sign up modal
var closesignup = document.getElementsByClassName('close')[1];

// When the user clicks the button, open the sign up modal
function showSignUpModal() {
	signupModal.style.display = 'block';
}

// When the user clicks on <span> (x), close the sign up modal
closesignup.onclick = function() {
	signupModal.style.display = 'none';
};

// When the user clicks anywhere outside of the sign up modal, close it
window.onclick = function(event) {
	if (event.target == signupModal) {
		signupModal.style.display = 'none';
	}
};
