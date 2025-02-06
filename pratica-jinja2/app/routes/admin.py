from datetime import timedelta

from fastapi import Depends, HTTPException, status, APIRouter, Response
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import Session

from .. import models, schemas
from ..Auth import Auth
from ..config import settings
from ..database import get_db
from ..security import create_access_token

router = APIRouter()

@router.post('/admin', status_code=status.HTTP_201_CREATED)
def create_admin(payload: schemas.Admin, db: Session = Depends(get_db)):

    new_admin = models.Admin(**payload.model_dump())
    try:
        db.add(new_admin)
        db.commit()
        db.refresh(new_admin)

        access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = create_access_token(
            data={"sub": new_admin.email, "id": str(new_admin.id)},
            expires_delta=access_token_expires
        )

        return {
            "admin": new_admin,
            "access_token": access_token,
        }

    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Erro no banco de dados"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocorreu um erro inesperado. {e}"
        )


@router.get('/admin')
def get_admin(id: int, db: Session = Depends(get_db)):
    admin = db.query(models.Admin).filter(models.Admin.id == id).first()
    if not admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f"Admin não encontrado")
    return {"status": "success", "admin": admin}


@router.patch('/admin')
def update_admin(id: int, payload: schemas.Admin, db: Session = Depends(get_db)):
    admin_query = db.query(models.Admin).filter(models.Admin.id == id)
    db_admin = admin_query.first()

    if not db_admin:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Admin não encontrado')
    update_data = payload.model_dump(exclude_unset=True)
    admin_query.update(update_data, synchronize_session=False)
    try:
        db.commit()
        db.refresh(db_admin)
        return {"status": "success", "admin": db_admin}
    except IntegrityError:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Erro no banco de dados"
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail=f"Ocorreu um erro inesperado. {e}"
        )

@router.post('/admin/login')
def auth_admin(
        payload: Auth,
        db: Session = Depends(get_db),
        response: Response = None
):
    admin = db.query(models.Admin).filter(models.Admin.email == payload.email).first()
    if not admin or not payload.senha == admin.senha:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Credenciais inválidas"
        )

    access_token_expires = timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(
        data={"sub": admin.email, "id": str(admin.id)},
        expires_delta=access_token_expires
    )

    response.headers["Authorization"] = f"Bearer {access_token}"

    return {"access_token": access_token, "token_type": "bearer"}
