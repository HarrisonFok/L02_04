import SignIn

def quit(window, user):
    # destroy this window
    window.destroy()
    # call the transition screen
    SignIn.goToTransitionScreen(user)