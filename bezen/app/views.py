from django.shortcuts import render,redirect
from app.models import recipe
from django.views.generic import TemplateView

# Create your views here.


class Index(TemplateView):
    context = {}
    template_name = 'app/index.html'

    def get(self, request, *args, **kwargs):
        user = request.user.id
        if user:
            return redirect('index')
        data = recipe.objects.all()
        self.context['data'] = data
        return render(request,self.template_name , self.context)

