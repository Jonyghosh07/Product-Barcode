from odoo import models, fields, api
import base64
import requests
from io import BytesIO

class ProductTemplate(models.Model):
    _inherit = 'product.template'
    
    barcode_img = fields.Binary(string="Barcode")
    
    @api.model
    def create(self, values):
        result = super(ProductTemplate, self).create(values)
        default_code = values.get("default_code")
        if default_code:
            self._generate_barcode_image(result, default_code)
        return result
        
    def _generate_barcode_image(self, record, code):
        """Generate a barcode image using Odoo's built-in barcode generator"""
        if not code:
            return
            
        try:
            # Use Odoo's built-in barcode URL
            base_url = self.env['ir.config_parameter'].sudo().get_param('web.base.url')
            barcode_url = f"{base_url}/report/barcode/Code128/{code}"
            
            # Get the image from the URL
            response = requests.get(barcode_url, timeout=5)
            if response.status_code == 200:
                # Convert to base64 string for binary field
                barcode_base64 = base64.b64encode(response.content)
                # Update the record with the generated barcode
                record.write({'barcode_img': barcode_base64})
        except Exception as e:
            # Import logger
            import logging
            _logger = logging.getLogger(__name__)
            _logger.error(f"Failed to generate barcode for {code}: {e}")