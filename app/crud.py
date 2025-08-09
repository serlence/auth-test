from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, update, delete
from sqlalchemy.exc import IntegrityError
from app.models import User
from app.schemas import UserCreate
from app.utils import get_password_hash

class UserCRUD:
    
    @staticmethod
    async def get_user_by_id(db: AsyncSession, user_id: int) -> Optional[User]:
        stmt = select(User).where(User.id == user_id)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_user_by_email(db: AsyncSession, email: str) -> Optional[User]:
        stmt = select(User).where(User.email == email)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()
    
    @staticmethod
    async def get_user_by_username(db: AsyncSession, username: str) -> Optional[User]:
        stmt = select(User).where(User.username == username)
        result = await db.execute(stmt)
        return result.scalar_one_or_none()
    
    @staticmethod
    async def create_user(db: AsyncSession, user: UserCreate) -> User:
        hashed_password = get_password_hash(user.password)
        db_user = User(
            email=user.email,
            username=user.username,
            hashed_password=hashed_password
        )
        
        try:
            db.add(db_user)
            await db.commit()
            await db.refresh(db_user)
            return db_user
        except IntegrityError:
            await db.rollback()
            raise
    
    @staticmethod
    async def update_user_active_status(
        db: AsyncSession, 
        user_id: int, 
        is_active: bool
    ) -> Optional[User]:
        stmt = (
            update(User)
            .where(User.id == user_id)
            .values(is_active=is_active)
            .returning(User)
        )
        result = await db.execute(stmt)
        await db.commit()
        return result.scalar_one_or_none()
    
    @staticmethod
    async def delete_user(db: AsyncSession, user_id: int) -> bool:
        stmt = delete(User).where(User.id == user_id)
        result = await db.execute(stmt)
        await db.commit()
        return result.rowcount > 0

user_crud = UserCRUD()
