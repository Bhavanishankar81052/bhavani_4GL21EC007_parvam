from django.shortcuts import render

def index(request):
    return render(request,'students/index.html')

def about(request):
    return render(request,'students/about.html')

def services(request):
    return render(request,'students/services.html')

def contact(request):
    return render(request,'students/contact.html')

# Create a new student
def student_create(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Student added successfully!')
            return redirect('student_list')
    else:
        form = StudentForm()
    return render(request, 'student_app/student_form.html', {'form': form})