from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.conf import settings
from django.core.mail import send_mail

from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

from .models import Subscriber
from .forms import SubscriberForm
from .helpers import random_digits

# Create your views here.

# ------------------------
@csrf_exempt
def subscribe_view(request):
    context = {}
    form = SubscriberForm()

    if request.POST:
        # Form submitted.
        context['email'] = request.POST['email']

        # Check if email is already subscribed.
        exists = False
        confirmed = False
        sub = Subscriber.objects.filter(email=request.POST['email'])
        if len(sub):
            exists = True
            sub = sub[0]
            if sub.confirmed:
                confirmed = True
                context['subscriber_form'] = form
                context['denied'] = True

        if not exists:
            sub = Subscriber(email=request.POST['email'], conf_num=random_digits())
            sub.save()

        if not confirmed:
            message = Mail(from_email = settings.NOREPLY_EMAIL,
                    to_emails = sub.email,
                    subject = 'Confirmación de Subscripción a Boletín de Pictea.me',
                    html_content = '<strong>¡Gracias por suscribirte a nuestro boletín!</strong><p>Por favor completa el proceso dando <a href="{}/confirm/?email={}&conf_num={}">click aquí</a> para confirmar tu registro.</p><p>No queremos que alguien esté registrando tu correo sin tu consentimiento.</p><small><a href="{}/unsubscribe/?email={}&conf_num={}">Date the baja</a></small>'.format(request.build_absolute_uri('localhost:8000/newsletter'), sub.email, sub.conf_num, request.build_absolute_uri('localhost:8000/newsletter'), sub.email, sub.conf_num))
            try:
                sg = SendGridAPIClient(settings.SENDGRID_API_KEY)
                response = sg.send(message)
                print(response.status_code)
                print(response.body)
                print(response.headers)
            except Exception as e:
                print(e.message)
    else:
        # GET request
        context['subscriber_form'] = form

    return render(request, 'newsletter/subscribe.html', context)


# ------------------------
def confirm_view(request):
    context = {}
    context['email'] = request.GET['email']
    try:
        sub = Subscriber.objects.get(email=request.GET['email'])

        # Confirmation number from url matches that of DB.
        if sub.conf_num == request.GET['conf_num']:
            sub.confirmed = True
            sub.save()
            return render(request, 'newsletter/confirmed.html', context)

        # Confirmation number does not match.
        else:
            return render(request, 'newsletter/denied.html', context)
    except:
        return render(request, 'newsletter/denied.html', context)


# ------------------------
def unsubscribe_view(request):
    context = {}
    sub = Subscriber.objects.get(email=request.GET['email'])
    context['email'] = sub.email
    if sub.conf_num == request.GET['conf_num']:
        sub.delete()
        return render(request, 'newsletter/unsubscribed.html', context)
    else:
        return render(request, 'newsletter/denied.html', context)
