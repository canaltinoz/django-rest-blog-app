from rest_framework.throttling import AnonRateThrottle,UserRateThrottle
class RegisterThrottle(AnonRateThrottle):
    scope='registerthrottle'
class ViewThrottle(UserRateThrottle):
    scope='viewthrottle'
