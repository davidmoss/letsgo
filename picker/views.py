from django.views.generic import TemplateView

from .utils import filter_venues, process_users, process_venues

users = process_users('./data/users.json')
venues = process_venues('./data/venues.json')


class PickerView(TemplateView):
    template_name = 'users.html'
    extra_context = {'users': users}

    def post(self, request, *args, **kwargs):
        # Get the list of users chosen by their index
        selection = request.POST.getlist('user')
        selected_users = [users[int(i)-1] for i in selection]
        selected_venues, rejected_venues = filter_venues(
            venues=venues, users=selected_users
        )

        # Add the results to the context
        context = self.get_context_data(**kwargs)
        context['venues'] = selected_venues
        context['rejects'] = dict(rejected_venues)
        context['selected'] = selection

        return self.render_to_response(context)
