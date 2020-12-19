# -*- coding: utf-8 -*-

from odoo import models, fields, api

class Compra(models.Model):
    _name='compra.compras'
    _rec_name= 'proveedor_id'
    fecha_compra=fields.Date( string = u'Fecha de emisión', default = fields.Date.context_today)
    observacion=fields.Text(blank=True, null=True)
    nro_factura=fields.Char(max_length=100)
    sub_total=fields.Integer()
    descuento=fields.Integer(default=0)
    total=fields.Integer()
    proveedor_id=fields.Many2one('compra.proveedor', string = "Id del proveedor")
    detalle_ids=fields.One2many('compra.detalle', 'compras_id', string = "Detalle de la compra")

class DetalleCompra(models.Model):
    _name='compra.detalle'
    _rec_name ='compras_id'
    producto=fields.Many2one('inventario.producto', string = "Producto")
    cantidad= fields.Integer()
    precio_compra=fields.Integer()
    sub_total=fields.Integer(string= 'Sub total', compute= '_sub_total')
    descuento=fields.Integer(default=0)
    total=fields.Integer(string= 'Total de la compra', compute= '_total_detalle')
    compras_id=fields.Many2one('compra.compras', string = "Id de la compra")
    @api.one
    def _sub_total(self):
        self.sub_total = (self.cantidad * self.precio_compra)

    @api.one
    def _total_detalle(self):
        self.total = (self.sub_total - ((self.descuento)/100)* self.sub_total)


class Proveedor(models.Model):
    _name = 'compra.proveedor'

    nombre=fields.Text(blank=True, null=True)
    direccion=fields.Text(blank=True, null=True)
    contacto=fields.Text(blank=True, null=True)
    telefono= fields.Integer(default=0)
    email=fields.Text(blank=True, null=True)