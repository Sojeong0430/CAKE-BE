from rest_framework import permissions

class IsOwnerDeleteOnly (permissions.BasePermission):
    """
    오직 파티룸 오너만 해당 메시지를 삭제할 수 있는 권한 부여 클래스 입니다.
    메시지를 작성한 당사자(방문자)는 본인이 작성한 메시지를 삭제할 수 없습니다.

    """
    def has_object_permission(self, request, view, obj):
        if request.user.is_ :
            pass
        return super().has_object_permission(request, view, obj)