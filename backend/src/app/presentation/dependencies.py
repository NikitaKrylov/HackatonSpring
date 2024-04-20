from fastapi import HTTPException
from starlette import status

from app.schemas.user import UserOutWithRoleDTO


def check_permissions(user: UserOutWithRoleDTO, *permissions):# -> Callable[..., Coroutine[Any, Any, UserOutWithRoleDTO]]:
    for permission in permissions:
        if not getattr(user.role, permission, False):
            raise HTTPException(status.HTTP_403_FORBIDDEN, f'Permission {", ".join(permission)} forbidden')


