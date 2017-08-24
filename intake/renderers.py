from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.compat import template_render


class TemplateHTMLRendererWithContext(TemplateHTMLRenderer):
    def render(self, data, accepted_media_type=None, renderer_context=None):
        # We can't really call super in this case, since we need to modify the inner working a bit
        renderer_context = renderer_context or {}
        view = renderer_context.pop('view')
        request = renderer_context.pop('request')
        response = renderer_context.pop('response')
        view_kwargs = renderer_context.pop('kwargs')
        view_args = renderer_context.pop('args')

        if response.exception:
            template = self.get_exception_template(response)
        else:
            template_names = self.get_template_names(response, view)
            template = self.resolve_template(template_names)

        context = self.resolve_context(data, request, response, renderer_context)
        return template_render(template, context, request=request)

    def resolve_context(self, data, request, response, render_context):
        if response.exception:
            data['status_code'] = response.status_code
        data.update(render_context)
        return data
