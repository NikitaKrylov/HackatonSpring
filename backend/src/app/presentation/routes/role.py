from fastapi import APIRouter, Depends

from app.presentation.dependencies import require_permissions
from app.repository.role import RoleRepository
from app.schemas.user import RoleChangeDTO, RoleCreateDTO, RoleOutDTO

router = APIRouter(prefix="/roles")

role_repository = RoleRepository()


@router.get('', response_model=list[RoleOutDTO])
async def get_all_roles():
    return await role_repository.get_all()


@router.post('', response_model=RoleOutDTO)
async def create_role(data: RoleCreateDTO):
    return await role_repository.create(data)


@router.patch('')
async def update_role(data: RoleChangeDTO):
    await role_repository.update(data)


@router.post('/test')
async def test_roles(curent_user=Depends(require_permissions('is_admin'))):
    return curent_user

