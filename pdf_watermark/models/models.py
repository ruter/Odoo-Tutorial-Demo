import io
import base64
import logging
from reportlab.pdfbase import pdfmetrics, ttfonts
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm
from PyPDF2 import PdfFileWriter, PdfFileReader

from odoo import fields, models

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

    def _get_watermark(self):
        """
        获取水印文本
        :return:
        """
        return f'{self.env.company.name} {fields.Date.context_today(self)}'

    def _generate_watermark(self):
        """
        生成水印
        :return:
        """
        # 水印文件临时存储路径
        filename = f'/tmp/watermark.pdf'
        watermark = self._get_watermark()
        # 获取画布并修改原点坐标
        c = canvas.Canvas(filename)
        c.translate(1.5 * cm, -3 * cm)

        try:
            font_name = 'SimSun'
            # 从系统路径中引入中文字体(新宋)
            pdfmetrics.registerFont(ttfonts.TTFont('SimSun', 'SimSun.ttf'))
        except Exception as e:
            # 默认字体，不支持中文
            font_name = 'Helvetica'
            _logger.error(f'Register Font Error: {e}')

        # 设置字体及大小，旋转 -20 度并设置颜色和透明度
        c.setFont(font_name, 16)
        c.rotate(20)
        c.setFillColorRGB(0, 0, 0)
        c.setFillColor('#27334C', 0.2)
        # 平铺写入水印
        for i in range(0, 30, 6):
            for j in range(0, 35, 5):
                c.drawString(i * cm, j * cm, watermark)
        c.save()
        return filename

    def add_watermark(self, content):
        """
        添加水印
        :param content:
        :return:
        """
        watermark = self._generate_watermark()
        pdf_input = PdfFileReader(io.BytesIO(content), strict=False)
        watermark = PdfFileReader(open(watermark, "rb"), strict=False)
        pdf_output = PdfFileWriter()
        page_count = pdf_input.getNumPages()
        for page_number in range(page_count):
            input_page = pdf_input.getPage(page_number)
            input_page.mergePage(watermark.getPage(0))
            pdf_output.addPage(input_page)
        stream = io.BytesIO()
        pdf_output.write(stream)
        data = stream.getvalue()
        return data
