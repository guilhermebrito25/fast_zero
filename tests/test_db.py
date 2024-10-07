from fast_zero.models import User

def test_creat_user():
    user = User(
        username = 'Guilherme',
        email = 'guilherme2@gmail.com',
        password = 'Minha-Senha@123'
    )
    assert user.username == 'Guilherme'