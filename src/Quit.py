import SignIn

def quit(window, user):
	""" This method takes a window and current user and destroys the current window,
	then redirects to the transition screen based on the current user. """
    # destroy this window
    window.destroy()
    # call the transition screen
    SignIn.goToTransitionScreen(user)