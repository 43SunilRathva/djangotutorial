from django.shortcuts import render
from django.contrib.auth.decorators import login_required, permission_required
from .forms import ContactForm

@login_required
def secret_page(request):
    # Only logged in users see this
    return render(request, 'secret.html')

def contact_view(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # In a real app, you would save data here
            # For now, we just print "Success" to the terminal
            print("VALIDATION SUCCESS!")
        else:
            form = ContactForm()
    else:
        # If the user is just visiting the page (GET request)
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})
                                                                                        