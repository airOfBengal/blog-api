from rest_framework import permissions

class IsAuthorOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow authors of a post to edit it.
    Others can only read the post.
    """

    def has_permission(self, request, view):
        if request.user.is_authenticated:
            # Allow read access to all authenticated users
            return True
        return False

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Allow read access to all users
            return True
        
        return obj.author == request.user
