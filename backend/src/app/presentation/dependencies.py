from fastapi import Depends, HTTPException
from starlette import status

from app.services.auth import get_current_user_with_role


def require_permissions(*permissions):
    async def wrap(user=Depends(get_current_user_with_role)):
        for permission in permissions:
            if not getattr(user.role, permission, False):
                raise HTTPException(status.HTTP_403_FORBIDDEN, f'Требуются разрешения: {", ".join(permissions)}')
    return wrap


