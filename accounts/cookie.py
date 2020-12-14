from django.conf import settings
import datetime

### set the token into cookie
def setCookie(request,key, value):
        request.session.set_test_cookie()
        # This will delete this test cookie when the user's browser is closed.
        request.session.set_expiry(0)
        request.session[key] = value


### check token is exits or not
def getCookie(request,key):
    try:
        value = request.session.get(key)
        return value
    except Exception as e:
        return None

### delete the token 
def deleteCookies(request):
    # Checking if there is test cookie created and stored in user's browser
    if (request.session.test_cookie_worked()):
        print("Yes, there was a test cookie in your browser")
        request.session.flush()
        return True