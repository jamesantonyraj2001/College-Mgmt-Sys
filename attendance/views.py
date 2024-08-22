# views.py
from django.shortcuts import render, redirect
from .models import Student, Class, Attendance
from .forms import AttendanceForm

def take_attendance(request):
    if request.method == 'POST':
        form = AttendanceForm(request.POST)
        if form.is_valid():
            student_id = form.cleaned_data['student']
            class_id = form.cleaned_data['class_attended']
            date = form.cleaned_data['date']
            is_present = form.cleaned_data['is_present']
            Attendance.objects.create(student_id=student_id, class_attended_id=class_id, date=date, is_present=is_present)
    else:
        form = AttendanceForm()

    return render(request, 'take_attendance.html', {'form': form})

def view_attendance(request):
    # Retrieve and display attendance records
    attendance_records = Attendance.objects.all()
    return render(request, 'view_attendance.html', {'attendance_records': attendance_records})
