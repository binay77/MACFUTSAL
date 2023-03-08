# myapp/context_processors.py

def groups(request):
    user = request.user
    return {
        'is_Class_Coordinator': user.groups.filter(name='Class Coordinator').exists(),
        'is_System_Handler': user.groups.filter(name='System Handler').exists(),
        'is_adminpanel': user.groups.filter(name='adminpanel').exists(),
    }
