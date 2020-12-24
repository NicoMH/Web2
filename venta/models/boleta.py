# -*- coding: utf-8 -*-

from odoo import models, fields, api
import random


class Boleta(models.Model):
    _name = 'venta.boleta'
    _rec_name = "codigo_boleta"
    codigo_boleta = fields.Char(max_length=20, unique=True, string="Código Boleta", compute="_codigo")
    fecha = fields.Date( string = u'Fecha de emisión ', default = fields.Date.context_today)
    clientes_id = fields.Many2one('venta.clientes', string="Cliente ID")
   
    detalle_boleta_ids = fields.One2many('venta.detalle_boleta', 'boleta_id', string="Detalle de la Boleta")

    sub_total = fields.Integer(compute="_sub_total")
    descuento = fields.Float(default=0)
    total = fields.Float(string= 'Total Venta', compute= '_total_venta')

    @api.one
    def _codigo(self):
        self.codigo_boleta = random.randint(0,999999999)

    @api.one
    @api.depends('detalle_boleta_ids')
    def _sub_total(self):
        for detalle_boleta in self.detalle_boleta_ids:
            self.sub_total+=detalle_boleta.total

    @api.one
    def _total_venta(self):
        self.total = (self.sub_total - ((self.descuento)/100)* self.sub_total)
        return self.total


class Clientes(models.Model):
    _name = 'venta.clientes'
    _rec_name = 'nombre'
    nombre = fields.Char(default= "ingrese el nombre del cliente")
    telefono = fields.Integer(max_length=10,null=True,blank=True)


class DetalleBoleta(models.Model):
    _name = 'venta.detalle_boleta'
    _rec_name = 'total'    
    producto_id = fields.Many2one('inventario.producto', string = "Producto")
    cantidad = fields.Integer(default=1)
    precio = fields.Integer(related='producto_id.precio_venta')
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


