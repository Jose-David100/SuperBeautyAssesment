from django.views.generic import TemplateView

from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
# Create your views here.

class Dashboard(TemplateView):
	template_name = "ListaEquipo.html"

	@method_decorator(csrf_exempt)
	def dispatch(self, request, *args, **kwargs):
		return super().dispatch(request, *args, **kwargs)

	def post(self, request, *args, **kwargs):
		data = {}
		try:
			action = request.POST['action']
			if action == 'change_password':
				#user = User.objects.get(username= request.POST['username'])
				username = request.POST['username']
				pass_actual = request.POST['password_actual']

				user = authenticate(request, username=username, password=pass_actual)
				if user is not None:
					user_done = User.objects.get(username= username)
					new_password = request.POST['password']
					user_done.set_password(new_password)
					user_done.save()
					
					motivo = request.POST['motivo']
					r = Auditoria_sis()
					r.usuario = request.user
					r.titulo = 'Cambiar constraseña'
					r.descripcion = f'un cambio de contraseña con motivo de: {motivo}, a su cuenta'
					r.tipo_entidad = 'usuarios'
					r.tipo_accion = 'change_pass'
					r.tipo_color = 'change_pass'
					r.entidad_id = user_done.username
					r.save()
					
					logout(request)
					data['success'] = "Contraseña actualizada correctamente"
					
				else:
					data['error'] = "La contraseña que ingreso no coincide con la contraseña actual"      
			else:
				data['error'] = 'Ha ocurrido un error'           

		except Exception as e:
			data['error'] = str(e)
		return JsonResponse(data, safe=False)

	def get_context_data(self, **kwargs):
		context = super(Dashboard, self).get_context_data(**kwargs)
		return context