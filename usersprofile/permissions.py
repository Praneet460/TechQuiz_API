from rest_framework import permissions

class CustomUpdatePermission(permissions.BasePermission):
    """
    Permission class to check that a user can update 
    his own resource only.
    """

    def has_permission(self, request, view):
        # check that its an update request and 
        # user is modifying his resource only

        if request.method not in permissions.SAFE_METHODS and view.kwargs['username'] != request.user.user_name:
            # SAFE_METHODS = 'GET', 'OPTIONS', 'HEAD'
            print("This executed")
            return False
        return True