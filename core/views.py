from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.contrib import messages
from django.http import JsonResponse
from core.models import Message

def register(request):

    if request.method == "POST":
        user_username = request.POST.get('username')
        user_password = request.POST.get('password')

        if User.objects.filter(username=user_username).exists():
            messages.warning(request, 'User already exists!')

        else:

            User.objects.create_user(username=user_username, password=user_password)
            messages.info(request, 'Account created successfully!')
        return redirect('register')  

    return render(request, 'core/register.html')

def user_login(request):
    if request.method == "POST":
        user_username = request.POST.get('username')
        user_password = request.POST.get('password')

        user = authenticate(username=user_username, password=user_password)
        if user is not None:
            login(request, user)
            return redirect('home')  
        else:
            messages.warning(request, 'Wrong credentials!')
            return redirect('user_login')  
    return render(request, 'core/login.html')




def user_logout(request):
    logout(request)
    messages.info(request, 'User has been logged out!')
    return redirect(user_login)

def fetch_users(request, key):
    queryset = User.objects.filter(username__startswith=key)
    result = list(queryset.values("id", "username"))
    return JsonResponse(result, safe=False)

def user_detail(request, user_username):
    user = User.objects.get( username =user_username )

    


    context = {
        'user': user,
    }

    return render(request, 'core/home.html', context)

def send(request):
    if request.method == 'POST':
        user_message = request.POST.get('message')
        user_sender = request.user
        receiver_username = request.POST.get('receiver_username')
        user_receiver = get_object_or_404(User, username=receiver_username)
        
        # Create the message
        create_message = Message.objects.create(
            sender=user_sender,
            receiver=user_receiver,
            message=user_message
        )
        
        # Return sender and receiver as part of the response
        return JsonResponse({
            'status': 'Message sent successfully',
            'user_sender': user_sender.username,
            'user_receiver': user_receiver.username
        })
    
    return HttpResponse('Invalid request')


@login_required
def home(request):
    sender = request.GET.get('sender')
    receiver = request.GET.get('receiver')

    print(sender)
    return render(request, 'core/home.html')

def fetch_messages(request):
    sender = request.GET.get('sender')
    receiver = request.GET.get('receiver')
    
    if sender and receiver:
        # Get messages exchanged between sender and receiver ordered by date
        messages = Message.objects.filter(
            sender__username=sender, receiver__username=receiver
        ).union(
            Message.objects.filter(sender__username=receiver, receiver__username=sender)
        ).order_by('date_posted')
        
        message_list = list(messages.values('sender__username', 'receiver__username', 'message', 'date_posted'))
        
        return JsonResponse({
            'status': 'Success',
            'messages': message_list
        })
    
    return JsonResponse({'status': 'Invalid request'}, status=400)

def login_ajax(request):
    if request.method == 'POST':
        user_username = request.POST.get('username')
        user_password = request.POST.get('password')

        user = authenticate(username=user_username, password=user_password)
        if user is not None:
            login(request, user)
            return JsonResponse({'status': 'success', 'message': 'Login successful!'})
        else:
            return JsonResponse({'status': 'fail', 'message': 'Invalid credentials. Please try again.'})
    else:
        return JsonResponse({'status': 'fail', 'message': 'Invalid request method.'})
    