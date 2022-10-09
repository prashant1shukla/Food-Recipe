from django.shortcuts import render, redirect
from .forms import UploadRecipeForm
from .models import recipe
from profiles.models import Profile
from django.contrib.auth.decorators import login_required
from app.models import recipe
from django.views.generic import TemplateView
from django.utils.decorators import method_decorator
from django.shortcuts import get_object_or_404

# Create your views here.


class Index(TemplateView):
    context = {}
    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        user = request.user.id
        if user:
            return redirect('index')
        data = recipe.objects.all()
        self.context['data'] = data
        return render(request,self.template_name , self.context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class UploadRecipe(TemplateView):
    form_class = UploadRecipeForm
    context = {}
    template_name = 'uploadrecipe.html'

    def get(self,request,*args,**kwargs):
        user = request.user
        self.context['form'] =self.form_class(initial={'created_by': user})
        return render(request,self.template_name, self.context)

    def post(self,request,*args,**kwargs):
        form = self.form_class(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewprofile')
        else:
            self.context['form'] = form
            return render(request,self.template_name,self.context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class Recipe(TemplateView):
    template_name = 'recipe.html'
    context ={}

    def get(self,request,*args,**kwargs):
        id =kwargs.get('id')
        obj = get_object_or_404(recipe,pk=id)
        self.context['obj'] = obj
        user = request.user.id
        if user:
            try:
                profile = Profile.objects.get(user=user)
                self.context['profile'] = 'pro_exist'
                return render(request, self.template_name, self.context)
            except Exception:
                return redirect('createprofile')
        return render(request,self.template_name,self.context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class EditRecipe(TemplateView):
    form_class = UploadRecipeForm
    context = {}
    template_name = 'uploadrecipe.html'

    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        recipes = get_object_or_404(recipe, pk=id)
        form = self.form_class(instance=recipes)
        self.context['form'] = form
        return render(request,self.template_name , self.context)

    def post(self,request,*args,**kwargs):
        id = kwargs.get('id')
        recipes = get_object_or_404(recipe, pk=id)
        form = self.form_class(instance=recipes,data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            return redirect('viewprofile')
        else:
            self.context['form']=form
            return render(request,self.template_name,self.context)


@method_decorator(login_required(login_url='login'), name='dispatch')
class DeleteRecipe(TemplateView):
    def get(self, request, *args, **kwargs):
        id = kwargs.get('id')
        recipes = get_object_or_404(recipe, pk=id)
        recipes.delete()
        return redirect('viewprofile')

