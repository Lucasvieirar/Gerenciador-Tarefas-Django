# from django import forms
# from .models import TarefaModel

# class TarefaForm(forms.ModelForm):
#     class Meta:
#         model = TarefaModel
#         fields = ['nome', 'descricao', 'completo']

from django import forms
from .models import TarefaModel, Categoria

CSS = "w-full bg-white/5 border border-white/10 rounded-xl px-4 py-3 text-white placeholder-slate-400 focus:outline-none focus:border-indigo-500 focus:ring-2 focus:ring-indigo-500/30 transition"

class TarefaForm(forms.ModelForm):
    class Meta:
        model = TarefaModel
        fields = ["nome", "descricao", "prioridade", "status", "categoria", "prazo", "completo"]
        widgets = {
            "nome": forms.TextInput(attrs={
                "class": CSS,
                "placeholder": "Nome da Tarefa....",
            }),
            "descricao": forms.Textarea(attrs={
                "class": CSS + " resize-none",
                "rows": 4,
                "placeholder": "Descricão (opcional)...",
            }),
            "prioridade": forms.Select(attrs={"class":CSS}),
            "status": forms.Select(attrs={"class": CSS}),
            "categoria": forms.Select(attrs={"class": CSS}),
            "prazo": forms.DateInput(attrs={
                "class": CSS,
                "type": "date",
            }),
            "completo": forms.CheckboxInput(attrs={
                "class": "w-5 h-5 rounded accent-indigo-500 cursor-pointer",
            }),
        }

