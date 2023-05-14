from models.base_model import BaseModel


class User(BaseModel):
    """user class that inherits from BaseModel"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""

    def __init__(self, *args, **kwargs):
        """Initialization of the user class"""
        super().__init__(*args, **kwargs)
