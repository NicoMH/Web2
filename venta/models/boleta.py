# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Boleta(models.Model):
    _name = 'venta.boleta'
    fecha = fields.Date( string = u'Fecha de emisión ', default = fields.Date.context_today)
    sub_total = fields.Integer(default=0)
    descuento = fields.Float(default=0)
    total = fields.Float(default=0)


    detalle_boleta_ids = fields.One2many('venta.detalle_boleta', 'boleta_id', string="Detalle de la Boleta")
    clientes_ids = fields.One2many('venta.clientes', 'boleta_id', string="cliente")

class Clientes(models.Model):
    _name = 'venta.clientes'
    nombres = fields.Char(default= "ingrese el nombre del cliente")
    apellidos = fields.Char(default= "ingrese el apellido del cliente")
    telefono = fields.Integer(max_length=20,null=True,blank=True)
    tipo =fields.Selection(
        [
            (1, 'Natural'),
            (2, 'Jurídica')
            ]
    )
    boleta_id = fields.Many2one('venta.boleta',string="boleta")


class DetalleBoleta(models.Model):
    _name = 'venta.detalle_boleta'
    cantidad = fields.Integer(default=1)
    precio = fields.Integer()
    sub_total = fields.Integer(string="Sub Total", compute="_sub_total")
    descuento = fields.Integer(default=0)
    total = fields.Integer(string="Total", compute="_total_det_boleta")
    boleta_id = fields.Many2one('venta.boleta',string="boleta")
    
    @api.one
    def _sub_total(self):
        self.sub_total = (self.cantidad * self.precio)

    @api.one
    def _total_det_boleta(self):
        self.total = (self.sub_total - ((self.descuento/100) * self.sub_total))


