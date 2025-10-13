import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
from models import User
import pytest
from models import User
from pydantic import ValidationError

def test_valid_user():
    u = User(name="Salah", email="salah@gmail.com", account_id=1)
    assert u.account_id == 1

def test_invalid_email():
    with pytest.raises(ValidationError):
        User(name="X", email="not-an-email", account_id=2)

def test_negative_account():
    with pytest.raises(ValidationError):
        User(name="X", email="x@y.com", account_id=-5)

