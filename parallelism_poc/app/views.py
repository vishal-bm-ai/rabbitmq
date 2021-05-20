from django.contrib.auth.models import User
from django.contrib import messages
from django.views.generic.edit import FormView
from django.shortcuts import redirect
from rest_framework.views import APIView
from rest_framework.response import Response
from .forms import GenerateForm
from .tasks import process_job

class GenerateJobView(FormView):
    template_name = 'process_job.html'
    form_class = GenerateForm

    def form_valid(self, form):
        job_id = form.cleaned_data.get('job_id')
        process_job.delay(job_id)
        messages.success(self.request, 'We are processing your job! Wait a moment and refresh this page.')
        return redirect('admin')

class Process(APIView):

    def post(self,request):
        job_id = request.data.get('job_id')
        process_job.delay(job_id)
        messages.success(self.request, 'We are processing your job! Wait a moment and refresh this page.')
        return Response(data={'message':'Job sumitted'},status=200)
