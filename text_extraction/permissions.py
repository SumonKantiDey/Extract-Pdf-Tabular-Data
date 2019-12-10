from rest_framework import permissions


class IsAnalyticsView(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='AnalyticsView'):
            return True
        return False


class IsBrokerView(permissions.BasePermission):
    def has_permission(self, request, view):
        if request.user and request.user.groups.filter(name='BrokerView'):
            return True
        return False
