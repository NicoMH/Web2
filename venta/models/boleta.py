# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Boleta(models.Model):
    _name = 'venta.boleta'
    _rec_name = "codigo_boleta"
    #_rec_name = ''
    codigo_boleta = fields.Integer(unique=True, string= "Código de Boleta")
    fecha = fields.Date( string = u'Fecha de emisión ', default = fields.Date.context_today)
    total = fields.Float(default=0)
    clientes_id = fields.Many2one('venta.clientes', string="Cliente ID")
    sub_total = fields.Integer(default=0)
    descuento = fields.Float(default=0)
    
    detalle_boleta_ids = fields.One2many('venta.detalle_boleta', 'boleta_id', string="Detalle de la Boleta")
    
class Clientes(models.Model):
    _name = 'venta.clientes'
    _rec_name = 'nombre'
    nombre = fields.Char(default= "ingrese el nombre del cliente")
    telefono = fields.Integer(max_length=10,null=True,blank=True)


class DetalleBoleta(models.Model):
    _name = 'venta.detalle_boleta'
    _rec_name = 'total'    
    producto=fields.Many2one('inventario.producto', string = "Producto")
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


