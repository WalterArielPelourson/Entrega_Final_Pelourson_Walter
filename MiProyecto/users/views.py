from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from users.forms import UserRegisterForm
from django.contrib.auth.decorators import login_required
from .forms import UserEditForm
from django.contrib.auth.views import PasswordChangeView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from .forms import UserEditForm
from .models import Avatar
from django.contrib import messages


#Logueo
def login_request(request):
    
    msg_login = " "
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form. is_valid():
            
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')
            
            user = authenticate(username=usuario, password=contrasenia)
            
            if user is not None:
                login(request, user)
                return render(request, "MiAppMedicos/TempBaseCargaDatos.html")
        
        msg_login = "Usuario o contraseña invalido"
    form = AuthenticationForm()
    
    return render(request, "users/login.html", {"form": form, "msg_login": msg_login})    


#registro 
def register (request):
    
    msg_register = ""
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        
        if form. is_valid():
           #form.save()
           user = form.save() 
           avatar = Avatar(user=user)
           if form.cleaned_data.get('imagen'):
               avatar.imagen = form.cleaned_data.get('imagen')
           avatar.save() 
           messages.success(request, f'Tu cuenta ha sido creada. ¡Ahora puedes iniciar sesión!')  
           
           return render(request, "MiAppMedicos/TempBaseCargaDatos.html")
        
       # msg_register = "Error en datos ingresados"
    else:   
        form = UserRegisterForm()
    return render(request, "users/registro.html", {"form": form, "msg_register": msg_register})        


#Editar Usuario
@login_required
def editar_perfil(request):
    
    usuario = request.user
    try:
        avatar = usuario.avatar
       
    except Avatar.DoesNotExist:
        avatar=None

    
    if request.method == 'POST':
        
        form = UserEditForm(request.POST, request.FILES, instance=request.user)
        
        if form.is_valid():
            form.save()
            if avatar:
                avatar.imagen = form.cleaned_data.get('imagen')
                avatar.save()
                
            else:
                Avatar.objects.create(user=usuario, imagen=form.cleaned_data.get('imagen'))
            return render(request, "MiAppMedicos/TempBaseCargaDatos.html")  # Redirige a la página de perfil después de guardar
    else:
        form = UserEditForm(instance=usuario)
       # form = UserEditForm(initial={'imagen': usuario.avatar.imagen}, instance=request.user)
    
    return render(request, 'users/editar_usuario.html', {'form': form, 'usuario': usuario})
                
                
#Cambiar Clave
class CambiarPassView (LoginRequiredMixin, PasswordChangeView):
    template_name = "users/cambiar_clave.html"
    success_url = reverse_lazy("EditarPerfil")
                    
                
                
                

                      
                      
        
            
    