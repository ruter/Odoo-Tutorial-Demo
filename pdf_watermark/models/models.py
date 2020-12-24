import base64
import logging

from odoo import models

_logger = logging.getLogger(__name__)


class IrHttp(models.AbstractModel):
    _inherit = 'ir.http'

    def binary_content(self, *args, **kwargs):
        status, headers, content = super(IrHttp, self).binary_content(*args, **kwargs)

        content_type = dict(headers).get('Content-Type')
        if content_type == 'application/pdf':
            content = self.add_watermark(base64.b64decode(content))
            content = base64.b64encode(content)

        return status, headers, content
