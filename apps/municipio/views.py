from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import Municipio
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin, messages

class MunicipioCreate(SuccessMessageMixin, CreateView):
    model = Municipio
    success_message = 'Município cadastrado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy("index")

    def get_context_data(self, **kwargs):
        context = super(CreateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Municípios - Queimadas'
        context['descricao'] = 'Cadastro de Município'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class MunicipioUpdate(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = reverse_lazy('login')
    model = Municipio
    success_message = 'Município atualizado com sucesso!'
    template_name = "cadastros/form.html"
    success_url = reverse_lazy('index')

    def get_object(self, queryset=None):
        return self.request.user

    def get_context_data(self, **kwargs):
        context = super(UpdateView, self).get_context_data(**kwargs)
        context['titulo'] = 'Municípios - Queimadas'
        context['descricao'] = 'Editar Município'
        context['botao'] = 'Salvar'
        return context

    def form_valid(self, form):
        url = super().form_valid(form)
        return url

class MunicipioDetail(DetailView):
    login_url = reverse_lazy('login')
    model = Municipio
    template_name = "cadastros/detalhes/municipio.html"

    def get_object(self, queryset=None):
        return self.request.user

class MunicipioDelete(LoginRequiredMixin, SuccessMessageMixin, DeleteView):
    login_url = reverse_lazy('login')
    model = Municipio
    success_message = 'Município excluído com sucesso!'
    template_name = "cadastros/form-excluir.html"
    success_url = reverse_lazy("listar_municipios")

class MunicipioList(LoginRequiredMixin, ListView):
    login_url = reverse_lazy('login')
    model = Municipio
    template_name = "cadastros/listas/municipios.html"

    def get_context_data(self, **kwargs):
        context = super(MunicipioList, self).get_context_data(**kwargs)
        context['titulo'] = 'Lista de Municípios - Queimadas'
        return context
