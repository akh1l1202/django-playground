from django.shortcuts import render
from django.views.generic import TemplateView


# Function Based View
def home(request):

    context = {
        'name': 'Akhil Tyagi',
        'course': 'Computer Engineering',
        'status': True
    }

    return render(request, 'myapp/home.html', context)


# Class Based View
class StudentView(TemplateView):

    template_name = 'myapp/student.html'

    def get_context_data(self, **kwargs):

        context = super().get_context_data(**kwargs)

        context['student_name'] = 'Akhil Tyagi'
        context['roll_no'] = '101'
        context['department'] = 'Computer Engineering'

        return context