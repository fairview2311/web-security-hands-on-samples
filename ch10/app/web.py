from fastapi.templating import Jinja2Templates
from app.peek import peek
from app.session import current_user

templates = Jinja2Templates(directory="app/templates")


def render(request, name, context=None, status_code=200):
    response = templates.TemplateResponse(
        request=request, name=name,
        context={"user": current_user(request), **(context or {})},
        status_code=status_code,
    )
    return peek(response, "html", response.body.decode("utf-8"))
