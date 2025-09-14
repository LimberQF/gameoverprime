
from django.views.generic import TemplateView
from django.http import Http404
from django.template.loader import get_template
from django.template import TemplateDoesNotExist

class HomePage(TemplateView):
    template_name = "home_page.html"

class CategoryListPage(TemplateView):

    template_name = "category.html"

class CategoryDetailPage(TemplateView):

    def get_template_names(self):
        slug = self.kwargs["slug"]
        tpl = f"categories/{slug}.html"
        try:
            get_template(tpl)
        except TemplateDoesNotExist:
            raise Http404("Categoría no encontrada")
        return [tpl]

class CarritoPage(TemplateView):
    template_name = "carrito/index.html"

class CajaPage(TemplateView):
    template_name = "caja/index.html"

class LoginPage(TemplateView):
    template_name = "register_login/login.html"

class RegisterPage(TemplateView):

    template_name = "register_login/registro.html"
