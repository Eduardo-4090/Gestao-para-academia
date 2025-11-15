from django.shortcuts import render,redirect , get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import AlunoForms
from .models import Alunos
from django.contrib import messages 

@login_required
def home (request):
    alunos = Alunos.objects.filter(dono = request.user).order_by('data_vencimento')
    return render(request, 'home.html',{'alunos':alunos})

@login_required
def add_aluno(request):
    limite = Alunos.objects.filter(dono=request.user).count()
    if request.method == 'POST':
        forms = AlunoForms(request.POST)
        if forms.is_valid():
            aluno = forms.save(commit=False)
            aluno.dono = request.user
            aluno.save()
            messages.success( request,'Aluno Adicionado com succeso')
            return redirect('home')
        else:
          forms=AlunoForms()
          messages.error(request , 'Dados invalidos , Tente novamente')
          return redirect('add')
    elif limite >= 5:
        messages.error(request ,'Você Atingiu seu limite  De Alunos No Plano de Teste')
        return redirect('home')
    else:
        forms=AlunoForms()
        return render(request, 'add.html', {'forms':forms})

@login_required
def detalhe_aluno(request,aluno_id):
    aluno = get_object_or_404(Alunos, id=aluno_id , dono=request.user)
    if request.method == "POST":
        form = AlunoForms(request.POST , instance=aluno)
        if form.is_valid():
            form.save()
            messages.success(request,'Aluno Editado com Succeso')
            return redirect('home')
        else:
            edicao = AlunoForms(instance=aluno)
            messages.error(request,'dados invalidos , tente novamente')
            return render(request,'detalhe_aluno.html',{'edicao':edicao,'aluno':aluno}) 
    else:   
        edicao = AlunoForms(instance=aluno)
        return render(request,'detalhe_aluno.html',{'edicao':edicao,'aluno':aluno})

@login_required
def Excluir(request, aluno_id):
    aluno = get_object_or_404(Alunos , id=aluno_id , dono=request.user)
    aluno.delete()
    messages.success(request, 'Aluno deletado com success')
    return redirect('home')