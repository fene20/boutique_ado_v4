from django.forms.widgets import ClearableFileInput
# using "as _" can now call gettext_lazy() using _(). i.e. an alias.
from django.utils.translation import gettext_lazy as _


class CustomClearableFileInput(ClearableFileInput):
    clear_checkbox_label = _('Remove')  # override
    initial_text = _('Current Image')  # override
    input_text = _('')   # override
    template_name = 'products/custom_widget_templates/custom_clearable_file_input.html'
