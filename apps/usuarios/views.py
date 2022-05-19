from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.contrib.auth.models import User
from .form import UsuarioForm, UsuarioUpdateForm
from django.contrib.auth.views import PasswordChangeView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages

class UsuarioCreate(SuccessMessageMixin, CreateView):
    model = User
    form_class = UsuarioForm
    success_message = 'Usuário cadastrado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Usuários - Queimadas'
        context['descricao'] = 'Cadastro de Usuário'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class PasswordChangeView(PasswordChangeView):
    from_class = PasswordChangeView
    success_message = 'Senha alterada com sucesso!'
    success_url = reverse_lazy('index')

class UsuarioUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = User
    form_class = UsuarioUpdateForm
    success_message = 'Usuário atualizado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Usuários - Queimadas'
        context['descricao'] = 'Editar Usuário'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class UsuarioDetail(DetailView):
    login_url = reverse_lazy('login')
    model = User
    template_name = "cadastros/detalhes/usuario.html"

    def get_object(self, queryset=None):
        return self.request.user

class UsuarioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = User
    template_name = "cadastros/listas/usuarios.html"

    def get_context_data(self, **kwargs):
        context = super(UsuarioList, self).get_context_data(**kwargs)
        context['titulo'] = 'Lista de Usuários - Queimadas'
        return context
