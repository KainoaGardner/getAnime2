from app import app
from app.routes import users, entries, authentication, lists

app.include_router(users.router)
app.include_router(entries.router)
app.include_router(lists.router)
app.include_router(authentication.router)
