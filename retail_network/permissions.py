from rest_framework.permissions import IsAuthenticated


class IsActiveEmployee(IsAuthenticated):

    def has_permission(self, request, view):
        user = request.user
        return user.is_active and user.is_staff
