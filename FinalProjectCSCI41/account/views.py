from django.shortcuts import redirect, render
from .forms import OrganizerForm, ParticipantForm
from .models import User, Organizer, Participant

def profile_view(request):
    """Renders the view for profile.html using the context user"""
    user = request.user

    ctx = {'profile': user}
    return render(request, 'profile.html', ctx)


def register_organizer(request):
    if request.method == "POST":
        register_form = OrganizerForm(request.POST)

        if register_form.is_valid():
            id_number = register_form.cleaned_data["id_number"]
            password = register_form.cleaned_data["password2"]
            name = register_form.cleaned_data["name"]

            user = User()
            user.username = id_number
            user.first_name = name
            user.set_password(password)
            user.save()

            organizer = Organizer()
            organizer.user = user
            organizer.organizer_type = request.POST.get("organizer_type")
            organizer.save()
            return redirect("/account/login/")
    else:
        register_form = OrganizerForm()

    ctx = {
        'register_form': register_form,
    }

    return render(request, 'registration/registerOrganizer.html', ctx)


def register_participant(request):
    if request.method == "POST":
        register_form = ParticipantForm(request.POST)

        if register_form.is_valid():
            id_number = register_form.cleaned_data["id_number"]
            password = register_form.cleaned_data["password2"]
            name = register_form.cleaned_data["name"]

            user = User()
            user.username = id_number
            user.first_name = name
            user.set_password(password)
            user.save()

            participant = Participant()
            participant.user = user
            participant.participant_type = request.POST.get("participant_type")
            participant.birthdate = request.POST.get("birthdate")
            participant.department = request.POST.get("department")
            participant.save()
            return redirect("/account/login/")
    else:
        register_form = ParticipantForm()

    ctx = {
        'register_form': register_form,
    }

    return render(request, 'registration/registerParticipant.html', ctx)
