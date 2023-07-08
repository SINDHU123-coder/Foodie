import typer
from peewee import *
from foodie.models import create_tables
from foodie.services.authentication import UserSession, AuthenticationService
from foodie.services.restuarants import restuarantsService
from foodie.exceptions import FoodieExit

from foodie.commands import users, restuarants, cart, order

app = typer.Typer()

user_session = users.user_session
auth = users.auth

app.add_typer(users.app, name="users")
app.add_typer(restuarants.app, name="restuarants")
app.add_typer(cart.app, name="cart")
app.add_typer(order.app, name="order")


if __name__ == "__main__":
    create_tables() 
    with user_session:
        try:
            auth.load_session()
            app()
        except Exception as e:
            pass