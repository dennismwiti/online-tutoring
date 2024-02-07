from django.shortcuts import render, redirect
from .forms import ContactForm
from django.contrib import messages


# Create your views here.
def contact_view(request):
				if request == 'POST':
								form = ContactForm(request.POST)
								if form.is_valid():
												form.save()
												messages.success(request, 'Your request has been submitted successfully.')

												return redirect('course-details')
				else:
								form = ContactForm()

				return render(request, 'pages/contact-us.html', {'form': form})
