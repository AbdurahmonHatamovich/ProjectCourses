from django.shortcuts import render, redirect
from django.views import View
from .models import Course, Teacher


class CourseListView(View):
    def get(self, request):
        search = request.GET.get('search')
        if not search:
            courses = Course.objects.all()
            context = {
                'courses': courses,
                'res' : search,
            }
            return render(request, 'main/course.html', context)
        else:
            courses = Course.objects.filter(title__icontains=search)
            if courses:
                context = {
                    'courses': courses,
                    'res': search,
                }
                return render(request, 'main/course.html', context)
            else:
                context = {
                    'courses': courses,
                    'res': search,
                }
                return render(request, 'main/course.html', context)





class TeacherListView(View):
    def get(self, request):
        teachers = Teacher.objects.all()
        context = {
            'teachers': teachers,
        }
        return render(request, 'main/teacher.html', context)


class CourseDetailView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        return render(request, 'main/course_detail.html', {'course': course})


class CourseUpdateView(View):
    def get(self, request, id):
        return render(request, 'main/course_update.html')

    def post(self, request, id):
        new_title = request.POST.get('title')
        new_description = request.POST.get('description')
        new_price = request.POST.get('price')

        course = Course.objects.get(id=id)
        course.title = new_title
        course.description = new_description
        course.price = new_price
        course.save()
        return redirect("courses")


class CourseDeleteView(View):
    def get(self, request, id):
        course = Course.objects.get(id=id)
        course.delete()
        return redirect('courses')


class AddCourseView(View):
    def get(self, request):
        return render(request, 'main/add_course.html')

    def post(self, request):
        title = request.POST.get('title')
        description = request.POST.get('description')
        price = request.POST.get('price')
        image = request.POST.get('image')

        course = Course(title=title, description=description, price=price, image=f"course/course/{image}")
        course.save()

        return redirect("courses")
