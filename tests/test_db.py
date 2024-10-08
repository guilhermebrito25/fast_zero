from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session

from fast_zero.models import User, table_registry


def test_creat_user():
    engine = create_engine('sqlite:///:memory:')

    table_registry.metadata.create_all(engine)

    with Session(engine) as session:
        user = User(
            username='Guilherme',
            email='guilherme2@gmail.com',
            password='Minha-Senha@123',
        )

        session.add(user)
        session.commit()

        result = session.scalar(
            select(User).where(User.email == 'guilherme2@gmail.com')
        )

    assert result.username == 'Guilherme'
